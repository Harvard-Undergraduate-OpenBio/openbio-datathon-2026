# Hypothesis Card

## Title

Many Preeclampsia Genes Hold Up After Matching for Delivery Timing; a Minority Look Timing-Driven

**In plain words:** Many of the gene differences between early-onset preeclampsia placentas and controls persist when delivery timing is matched. A smaller share (about a quarter) looks driven by preterm versus term delivery.

**Underlying question (starter question 6):** How much of the preeclampsia signal could be explained by when delivery happened?

**Testable hypothesis:** FLT1, ENG, LEP and PAPPA2 are higher in early-onset preeclampsia mainly because of the disease, not delivery timing. Timing may contribute a modest share for FLT1 and LEP.

## Clinical/Biological Problem

Early-onset preeclampsia forces preterm delivery. Comparing these placentas with term placentas mixes the disease with the extra weeks of pregnancy. We ask which gene differences reflect preeclampsia and which reflect delivery timing.

## Dataset(s) and Relevant Cells

GSE203507 villous-tissue bulk RNA-seq: 15 preeclampsia (EOPE and EOPE+FGR), 5 preterm controls and 5 term controls.

The Zeisel/Admati gene browser and a marker table give cell-type context. Bulk data cannot say which cells a change comes from. In the browser, FLT1 is highest in extravillous trophoblast (also other trophoblast and vessel cells), ENG in endothelial cells (broad), PAPPA2 in trophoblast, and HLA-G only in extravillous trophoblast.

## Observed Result

- Preeclampsia vs preterm controls (two-group model): 472 genes differ at least 2-fold (283 higher, 189 lower), including FLT1, ENG, LEP and PAPPA2 (all higher).
- In the three-group model, similar numbers of genes differ against term and preterm controls (532 and 522), but only 235 are shared.
- Of the 532 genes that differ from term controls, 52% (279) still differ against preterm controls, 28% (151) look driven by timing (e.g. HLA-G, FN1, PRG2) and 19% (102) are unclear. For the typical gene, timing accounts for about 30% of the difference.
- In equal 5-vs-5 tests, preterm vs term controls differ in 86 genes: more than random splits of the controls (0 to 17) but fewer than preeclampsia vs preterm (232 to 763, median 537.5).
- In the three-group model, ENG and PAPPA2 differ little between preterm and term controls (log2FC about 0.2), FLT1 modestly (0.71) and LEP more (1.79, not significant with 5 vs 5), against preeclampsia effects of 1.8 to 5.4.
- Only 2 of 36 markers pass (KIT, CGA), so there is no clear sign of a cell-mix shift (whole marker classes were not tested).
- Fold changes are stable across robustness checks (correlation 0.99 to 1.0). Against an 89% no-covariate baseline, 87% of the 522 main genes stay significant with delivery week, 85% without S01 and S12, 78% with fetal sex and 53% with growth restriction.

## Proposed Mechanism

FLT1 and ENG encode anti-angiogenic proteins, so higher placental expression is consistent with the vascular imbalance described in preeclampsia. HLA-G and PRG2 are associated with extravillous trophoblast, so their apparent difference from term controls might reflect different amounts of that tissue in preterm and term samples. This second part is speculation.

## Why the Result Is Biologically Plausible

Excess sFlt-1 and soluble endoglin are linked to preeclampsia (Maynard et al., *J Clin Invest* 2003; Levine et al., *N Engl J Med* 2006). Extravillous trophoblast invasion and spiral artery remodeling are central to placentation, which makes tissue-mix differences plausible.

## Alternative Explanations/Confounders

- **Imperfect preterm controls.** Spontaneous preterm births often involve inflammation, so they are not healthy placentas.
- **Remaining timing gap.** Cases were delivered about 1.3 weeks earlier than preterm controls. A delivery-week covariate kept 87% of the 522 main genes (baseline 89%), but a small effect could remain.
- **Growth restriction.** 7 of 15 cases have it and no control does. Adjusting kept 53% of the 522 main genes, with fold changes unchanged.
- **Cell mix.** Bulk tissue cannot separate a change in cell mix from a change within cells.
- **Small groups.** With 5 controls per group, individual genes are noisy, and the 28% "looks driven by timing" share is a rough estimate.
- **Scope.** All cases are early onset and from one cohort.

## Proposed Validation Experiment or Follow-up Analysis

**Hypothesis to test:** FLT1, ENG, LEP and PAPPA2 are higher in early-onset preeclampsia mainly because of the disease, not delivery timing.

**Computational:**

1. **Independent cohort.** Repeat preeclampsia vs preterm in another placental RNA-seq dataset with medically indicated preterm controls. *Supported if* the four genes stay higher.
2. **Cell-type test.** Use the single-cell pseudobulk data to check whether these genes differ within specific cell types (exploratory, few control donors).
3. **Late-onset preeclampsia.** Repeat in late-onset cases, where timing is less of a confounder.

**Experimental:**

4. **Protein level.** Measure sFlt-1 and soluble endoglin by ELISA in preeclampsia, preterm and term pregnancies. *Supported if* higher in preeclampsia than in both control groups.
5. **Spatial location.** Stain placental sections for FLT1 and ENG to see which cells carry the signal.

**What would prove us wrong:** large fold changes for these genes between preterm and term controls, or loss of their difference in the independent cohort.

## Potential Intervention Relevance

FLT1 and ENG are already studied as diagnostic markers. Our result is consistent with their higher expression reflecting preeclampsia rather than preterm delivery, but it does not establish a therapeutic target (small cohort, RNA only, association only).

## Confidence Level and Limitations

**Overall confidence: medium.** The core finding (many genes, including FLT1, ENG, LEP and PAPPA2, differ between preeclampsia and delivery-matched preterm controls) is well supported. The finer claims about how much of the signal is timing, and which cells are involved, are less certain.

| Finding | Confidence | Why |
|---|---|---|
| Many genes (472 at 2-fold), including FLT1, ENG, LEP and PAPPA2, differ between preeclampsia and delivery-matched preterm controls | **Medium to high** | Large effects, consistent across models and robustness checks. Limited by one cohort and 5 controls. Timing may contribute a modest share for FLT1 and LEP. |
| Timing has a real effect, smaller than the disease effect (86 vs 232 to 763 genes) | **Medium** | Equal-size 5-vs-5 tests, but small groups. |
| About half persist, about a quarter look timing-driven | **Low to medium** | Approximate: depends on cutoffs and a noisy 5-vs-5 contrast. |
| HLA-G and PRG2 reflect extravillous trophoblast content | **Low** | One browser lookup from another study, plus speculation. |
| Cell mix does not change | **Low** | Only individual markers tested. |
| Results apply to all preeclampsia | **Low** | Early-onset cases only. |

**What expression data cannot establish:**

- **Cause.** We show association, not that these genes drive the disease.
- **Protein level or activity.** RNA does not always translate into protein.
- **Which cell a change comes from.** Bulk tissue mixes many cell types.
- **Therapeutic relevance.** We tested no intervention.

**What would raise confidence:** independent replication (ideally with medically indicated preterm controls), more samples per group, a closer gestational-age match, cases with and without growth restriction, single-cell or spatial data for cell mix, protein validation (ELISA), and late-onset cases.
