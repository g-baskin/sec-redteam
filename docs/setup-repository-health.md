# Repository setup health follow-up

**Data collection mode:** Local clone plus authenticated `gh` REST API reads. No credentials were printed or token scope introspection performed. Date: 2026-10-19 local. Source HEAD: `1e71d28b23881f5d1c76849003cd144cfe545947`.

**Coverage:** bounded Get Started follow-up, not a full repository, application-security or release audit. This read-only health pass follows [Security](setup-security-review.md) and [Quality](setup-quality-review.md); it changes no repository settings or implementation. The earlier, separately approved private-reporting enablement is recorded in [Get Started](get-started.md).

## Eight-dimension observations

| Dimension | Observed state and evidence |
| --- | --- |
| Branch protection / rulesets | `GET /repos/g-baskin/sec-redteam/branches/main/protection` returned `Branch not protected`; rulesets returned `[]`. No required checks or enforced code-owner gate established. [Branch settings](https://github.com/g-baskin/sec-redteam/settings/branches). |
| Commit quality | `git log -100` contains only one commit: `chore: publish AGPL-3.0-only source baseline`. It follows Conventional Commit form; a one-commit sample cannot establish an ongoing practice. |
| CODEOWNERS | Local [CODEOWNERS](../.github/CODEOWNERS) has a catch-all and governance patterns for verified repository owner `@g-baskin`. It is not yet published and branch enforcement is absent. Individual ownership is appropriate to the observed user-owned repository; no team was invented. |
| CI workflow density | Zero active local YAML workflows and zero hosted workflows. [CI starter](../.github/workflows/ci.yml.disabled) and [Dependabot starter](../.github/dependabot.yml.disabled) are inactive by filename. Default CodeQL is `not-configured`. Billing pause is owner-directed, not an accidental omission; do not activate or require checks now. |
| Docs presence | Local README, CONTRIBUTING, SECURITY, CHANGELOG, LICENSE, Library and wiki/graph are present. No code of conduct was adopted. Local presence is not remote publication. [Library](../library/README.md). |
| Repository settings | API reports all three merge strategies allowed and auto-delete-head-branches false. Secret scanning and push protection are enabled. Private vulnerability reporting is now enabled; Dependabot security updates remain disabled. No settings were changed in this follow-up. [General settings](https://github.com/g-baskin/sec-redteam/settings), [security settings](https://github.com/g-baskin/sec-redteam/settings/security_analysis). |
| Issue / PR templates | Substantive local bug, feature and PR templates exist under [`.github/`](../.github/README.md); they request synthetic, sanitized evidence and actual local checks. |
| Ignore coverage | Existing [`.gitignore`](../.gitignore) retained. `git check-ignore` confirms `.env`, `.env.local`, corpus data, pytest cache and Python egg metadata excluded; `.env.example` remains includable. Tracked-file name sweep found no matching environment/cache/build artifacts. This is not a history secret scan. |

This scoped pass is **unscored**. GitHub's remote community profile remains **42%**, measured before these uncommitted files are published; no improved remote score is claimed.

## Prioritized owner decisions

1. **Choose default-branch review protections.** Observed absence permits bypass of the proposed review workflow. Impact 5 / effort 1 = priority 5.0. Human owner should choose PR review, code-owner enforcement and force-push rules separately. Do not require inactive CI checks during the billing pause. Team workflow preferences remain unknown.
2. **Choose merge and branch-cleanup policy.** All merge methods are enabled and automatic branch deletion is off. Impact 2 / effort 1 = priority 2.0. Human owner should decide based on the desired history and feature-worktree lifecycle; this is a policy choice, not a security defect by itself.
3. **Adopt a community conduct policy if needed.** `CODE_OF_CONDUCT.md` is absent. Impact 2 / effort 2 = priority 1.0. Human owner must choose wording and a real enforcement contact rather than an agent inventing one.
4. **After billing is resolved, revisit automation.** Inactive CI/CodeQL/dependency updates are an accepted deferral. The CI Release Wasp owns future workflow design; activation, installs, costs and required-check changes need explicit authorization. No running-workflow or cost-savings claim is made here.

## Completion and preservation

The documentation candidate reviewed by Security and Quality has fingerprint `67b07ad844c94a203da2591f53c6f4fa692d3a581ac357760b3bf92c9020e668`. Their 105-file input manifest excludes review reports and local checklist state. The app source remains unchanged.

Whole-domain verification after the wiki writer's handoff covers all 61 wiki Markdown pages, 466 wikilinks, 573 source-coordinate occurrences, 21 source hashes and the 58-node/87-edge graph. Quality independently repeated declaration and link/source-identity checks. The existing test suite passed 18/18 with networking denied; hosted CI, fresh installation, Mermaid rendering and live Exa remain unrun.

The pre-existing `.gg-checklist.json` is retained and augmented with the completed docs/test/CI checks; earlier records are not replaced wholesale. Pre-existing `CLAUDE.md` and `docs/reviews/` are untouched. No notes contents, secrets or collected corpus were inspected. No app code, package manifest, dependency, ignore rule, license or Git configuration was changed.

`wasp-nest.lock` remains intentionally absent for the partial setup described in [Get Started](get-started.md). No commit, push, merge, deployment or cleanup was performed. These reports are review evidence, not permission to perform those actions.
