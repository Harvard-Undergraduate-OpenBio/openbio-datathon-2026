"""Fetch MSigDB Hallmark gene sets for Track 01.

MSigDB terms require each user to obtain files directly, so this script
downloads the pinned Hallmark release and writes a local GMT file with a
SHA-256 checksum. If the download requires sign-in, get the file manually
from https://www.gsea-msigdb.org/gsea/msigdb/collections.jsp and place it
in this directory as track01_gene_sets.gmt.
"""

import hashlib
import sys
from pathlib import Path
from urllib.request import Request, urlopen

MSIGDB_URL = (
    "https://www.gsea-msigdb.org/gsea/msigdb/download_file.jsp"
    "?file=/msigdb/release/2024.1.Hs/h.all.v2024.1.Hs.symbols.gmt"
)
OUTPUT = Path(__file__).parent / "track01_gene_sets.gmt"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> int:
    print(f"Downloading Hallmark gene sets from {MSIGDB_URL}")
    request = Request(MSIGDB_URL, headers={"User-Agent": "openbio-datathon-2026"})
    with urlopen(request) as response:
        data = response.read()
    OUTPUT.write_bytes(data)
    print(f"Wrote {OUTPUT}")
    print(f"SHA-256: {sha256_file(OUTPUT)}")
    print(f"Gene sets: {sum(1 for line in data.decode().splitlines() if line.strip())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
