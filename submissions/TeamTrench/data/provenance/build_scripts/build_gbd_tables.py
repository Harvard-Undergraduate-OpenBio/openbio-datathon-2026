"""Extract Supplementary Tables S1 and S2 from the article's supplement (Word file)
into CSV grids, cell for cell. No values are cleaned, renamed or reordered.

Usage: python build_gbd_tables.py medi-104-e43215-s001.docx OUT_DIR

Rules (see transformation_log.md):
- One CSV row per Word table row, one CSV column per Word grid column.
- A cell merged across columns or rows keeps its text in the first (top-left) position;
  the other positions it covered are left empty, as a spreadsheet would show them.
- A line break inside a cell becomes a single space.
- Cell text is otherwise kept exactly, including leading and trailing spaces.
"""
import csv, sys
from pathlib import Path
import docx
from docx.oxml.ns import qn

W_T, W_BR, W_CR, W_TAB = qn("w:t"), qn("w:br"), qn("w:cr"), qn("w:tab")

def cell_text(tc):
    paras = []
    for p in tc.iterchildren(qn("w:p")):
        parts = []
        for node in p.iter():
            if node.tag == W_T:
                parts.append(node.text or "")
            elif node.tag in (W_BR, W_CR):
                parts.append(" ")
            elif node.tag == W_TAB:
                parts.append("\t")
        paras.append("".join(parts))
    return " ".join(paras)

def table_grid(tbl):
    ncols = len(tbl.tblGrid.findall(qn("w:gridCol")))
    grid = []
    for tr in tbl.iterchildren(qn("w:tr")):
        row = []
        trPr = tr.find(qn("w:trPr"))
        if trPr is not None:                      # cells skipped at the start of a row
            gb = trPr.find(qn("w:gridBefore"))
            if gb is not None:
                row.extend([""] * int(gb.get(qn("w:val"))))
        for tc in tr.iterchildren(qn("w:tc")):
            span, vmerge = 1, None
            pr = tc.tcPr
            if pr is not None:
                g = pr.find(qn("w:gridSpan"))
                if g is not None:
                    span = int(g.get(qn("w:val")))
                v = pr.find(qn("w:vMerge"))
                if v is not None:
                    vmerge = v.get(qn("w:val")) or "continue"
            text = "" if vmerge == "continue" else cell_text(tc)
            row.append(text)
            row.extend([""] * (span - 1))
        if len(row) > ncols:
            raise ValueError(f"row has {len(row)} cells, grid has {ncols}")
        row.extend([""] * (ncols - len(row)))
        grid.append(row)
    return grid

def main(src, out_dir):
    doc = docx.Document(src)
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    wanted = {"Table S1.": "table_s1.csv", "Table S2.": "table_s2.csv"}
    done = {}
    for table in doc.tables:
        grid = table_grid(table._tbl)
        caption = grid[0][0].strip()
        for prefix, fname in wanted.items():
            if caption.startswith(prefix):
                if fname in done:
                    raise ValueError(f"two tables match {prefix}")
                with open(out / fname, "w", newline="", encoding="utf-8") as f:
                    csv.writer(f, lineterminator="\n").writerows(grid)
                done[fname] = (len(grid), len(grid[0]))
    for fname in wanted.values():
        if fname not in done:
            raise ValueError(f"{fname} not found in {src}")
        print(fname, "rows x columns:", done[fname])

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
