---
name: data-contract-dataset-readiness
description: Review data contracts, schemas, semantics, sourcing, labeling, annotation, leakage controls, dataset versioning, and acceptance evidence.
---

# Data Contract and Dataset Readiness

## Use When

- Source onboarding, schema/modeling work, semantic design, dataset construction, annotation review, synthetic-data control, or dataset acceptance.

## Procedure

1. Confirm source owner, steward, provenance, permitted use, classification, retention, consent basis, access policy, and policy exceptions.
2. Review conceptual, logical, and physical models; schemas; glossary terms; master/reference data; taxonomies; ontologies; knowledge graphs; and semantic interoperability.
3. Check contract fields, types, constraints, freshness, completeness, quality rules, change policy, versioning, lineage, and downstream owners.
4. Evaluate collection, labeling, annotation rubric, inter-annotator quality, deduplication, representativeness, imbalance, synthetic-data controls, leakage, contamination, splits, and holdouts.
5. Return `PASS`, `FAIL`, or `BLOCKED` with required remediation, evidence gaps, and owners.
