---
name: supply-chain-ci-release-security
description: Use for dependency, SBOM, provenance, build, CI/CD, configuration, and release-readiness review.
---

# supply-chain-ci-release-security

1. Confirm manifests, lockfiles, SBOMs, build definitions, artifact sources, provenance, pipeline scope, and release scope.
2. Identify unsupported, unpinned, untrusted, vulnerable, abandoned, or opaque components from supplied evidence.
3. Assess build identity, artifact integrity, signing, promotion controls, pipeline permissions, runner isolation, rollback, and approval gates.
4. Record uncertainty where external verification was not performed.
5. Separate blocking, conditional, accepted, and informational release items.
6. Route release recommendation and exceptions to humans.

Do not download dependencies, query private registries, run pipelines, publish artifacts, or approve release.

