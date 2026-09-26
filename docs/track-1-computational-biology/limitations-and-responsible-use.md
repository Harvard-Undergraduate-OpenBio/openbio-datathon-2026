# Limitations and Responsible Use

## What scRNA-seq Communication Inference Can and Cannot Do

### Can

- Predict potential ligand-receptor interactions based on co-expression patterns.
- Identify cell types that express signaling molecules and their receptors.
- Generate hypotheses about altered communication in disease.

### Cannot

- Directly measure physical cell-cell contact.
- Confirm that ligand proteins are secreted and reach the receiver cell.
- Confirm that receptor proteins are activated.
- Measure extracellular vesicle (EV) exchange.
- Establish causality from observational transcriptomics.
- Capture post-transcriptional or post-translational regulation.

## Responsible Reporting

Teams should:

1. **State the limitation explicitly** in their submission: "scRNA-seq ligand-receptor inference predicts potential communication from expression patterns and does not directly measure physical contact, ligand secretion, receptor activation, or causality."

2. **Distinguish predicted from validated interactions.**

3. **Acknowledge confounders:** gestational age, batch effects, cell-type composition, donor-level variation.

4. **Avoid overstatement:** Use language like "our analysis suggests" or "these results are consistent with" rather than "we show that" or "this proves."

5. **Propose validation:** Suggest a concrete experimental or computational follow-up that could test the hypothesis.

## Data Use

- Do not redistribute raw datasets outside their licensed terms.
- HCA data is governed by the HCA Data Release Policy and CC BY 4.0.
- GEO data is subject to NCBI data use terms.
- Cite all data sources in your submission.
