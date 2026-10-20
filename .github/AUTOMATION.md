# Repository automation and review

**CI is intentionally inactive while billing is unresolved.**

`workflows/ci.yml.disabled` is a future manual-only test workflow, not an active GitHub Actions workflow. Do not remove the suffix, add automatic triggers, or enable CodeQL runs without owner approval. `dependabot.yml.disabled` is also inactive; it does not enable dependency update jobs or security-update PRs.

Run `python3 -m pytest` locally with the development dependencies available. Record results in the PR; there are no configured lint/type-check commands to claim as passing.

The starter uses full action commit SHAs verified against the official GitHub repositories, read-only permissions, no persisted checkout credentials, no provider secrets, and a ten-minute timeout. It performs no live Exa ingestion, publishing, or deployment. These controls limit credential exposure if the workflow is activated later. The hosted job and fresh installation have not been run.

After billing is resolved, review dependency installation, supported action/Python versions, runner costs, and local test parity before renaming the workflow. Then test a manual dispatch before considering push/PR triggers or required status checks. Do not require a status check while its workflow is inactive.

[CODEOWNERS](CODEOWNERS) assigns the repository owner, `@g-baskin`, to all paths and explicitly to governance files. It does not itself enforce merge approval. Repository settings and rulesets require a separate owner decision.

See [CONTRIBUTING.md](../CONTRIBUTING.md) and [SECURITY.md](../SECURITY.md).
