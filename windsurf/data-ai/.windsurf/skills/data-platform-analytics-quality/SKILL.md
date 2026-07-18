---
name: data-platform-analytics-quality
description: Review data products, pipelines, quality, reliability, lineage, observability, governed metrics, semantic layers, BI, and decision intelligence.
---

# Data Platform and Analytics Quality

## Use When

- Ingestion, batch/stream processing, transformations, storage design, data products, marts, semantic layers, dashboards, governed metrics, quality, lineage, or observability are in scope.

## Procedure

1. Confirm product owner, upstream/downstream contracts, processing mode, storage boundary, recoverability target, freshness SLO, and consumer impact.
2. Review transformations, orchestration dependencies, reconciliation, idempotency, schema evolution, backfill behavior, performance, lineage, alert ownership, incident diagnosis, and rollback criteria.
3. Validate metric definitions, semantic layer mappings, dashboard logic, filters, cohorts, aggregation grains, decision use, reproducibility, and change control.
4. Separate builder evidence from independent quality and metric certification.
5. Return `PASS`, `FAIL`, or `BLOCKED` with unverified claims, failed checks, monitoring needs, and human-review gates.
