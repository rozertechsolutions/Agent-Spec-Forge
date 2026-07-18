---
name: analytics-experiment-review
description: Review analytics studies, causal inference, statistical design, uncertainty, calibration, segmentation, experiments, and metric certification.
---

# Analytics and Experiment Review

## Use When

- Exploratory analysis, governed metrics, statistical studies, causal inference, controlled experiments, uncertainty analysis, calibration, or segmentation are in scope.

## Procedure

1. State hypothesis, decision, metric, population, treatment or exposure, comparison, time window, unit of analysis, exclusion criteria, and business consequence.
2. Review design assumptions, causal identification, randomization or quasi-experimental method, sample size, power, guardrails, sequential testing, segmentation, missing data, and multiple-comparison handling.
3. Require reproducible queries or notebooks, data version, metric definitions, uncertainty intervals, sensitivity checks, and limits on causal claims.
4. Require human review when analytics affects prioritization, eligibility, access, pricing, safety, or user rights.
5. Return `PASS`, `FAIL`, or `BLOCKED` with evidence, caveats, and required independent certification.
