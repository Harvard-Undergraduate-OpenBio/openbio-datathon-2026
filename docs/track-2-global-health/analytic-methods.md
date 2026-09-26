# Track 2: Analytic Methods

## Overview

This document provides a decision framework for analyzing health-system data related to preeclampsia care. It does not prescribe a single pipeline.

## Suggested Approaches

### Descriptive Analysis
- Summarize key indicators by country, region, and urban/rural context.
- Visualize variation in ANC coverage, facility readiness, and treatment availability.
- Identify countries or regions with the largest gaps.

### Context Identification
- Cluster countries or regions by health-system characteristics (e.g., using k-means or hierarchical clustering on standardized indicators).
- Label clusters with meaningful health-system context names (e.g., "high-coverage urban", "low-coverage rural").

### Bottleneck Analysis
- Apply the Three Delays framework: identify which delay (seek, reach, receive) is most prominent in each context.
- Rank intervention points by estimated potential impact.

### Intervention Modeling
- Model the potential effect of specific interventions (e.g., increasing ANC visits, ensuring MgSO4 availability, reducing referral time).
- Use simple models (e.g., LiST tool, regression-based projections) rather than complex simulations.
- Clearly state assumptions and limitations.

## Pitfalls

- **Ecological fallacy:** Country-level data cannot be used to infer individual-level risk.
- **Data gaps:** Not all countries have DHS data; missing data is not random.
- **Comparability:** Survey methods and years differ across countries; standardize before comparison.
- **Over-modeling:** Do not lean too heavily toward consulting/strategy. Focus on identifying important intervention points with appropriate evidence.
