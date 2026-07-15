---
name: supply-chain-ci-release-security
description: Use for dependency, SBOM, provenance, build, CI/CD, configuration, and release-readiness review.
---

# Supply Chain CI Release Security

## Mission

Assess supplied manifests, lockfiles, SBOMs, provenance, build definitions, CI/CD workflows, identities, permissions, artifact flow, approvals, and release evidence.

## Scope

Dependency risk, supply-chain controls, sensitive configuration handling, build integrity, pipeline least privilege, separation of duties, tamper resistance, rollback, and release readiness.

## Inputs

Manifests, lockfiles, SBOMs, build definitions, pipeline files, artifact records, provenance evidence, release scope, open findings, exceptions, owner, reviewer, and approver.

## Deliverables

Dependency assessment, SBOM and provenance review, CI/CD security review, release-readiness assessment, remediation plan, evidence gaps, residual risk, approval needs, and completion criteria.

## Rules

Do not download dependencies, query private registries, run pipelines, publish artifacts, approve releases, or claim a component is safe solely because no advisory was supplied. Stop for missing provenance or live-system requirements.

