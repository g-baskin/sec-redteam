# Security Policy

## Scope and support

This policy covers the sec-redteam source repository and its Python CLI. It does not authorize testing third-party systems. The current manifest version is `0.1.0`; no supported-release matrix, response-time SLA, or hosted scanning service is promised by this policy.

## Report a vulnerability privately

Use [GitHub private vulnerability reporting](https://github.com/g-baskin/sec-redteam/security/advisories/new). This channel was enabled and verified on 2026-10-19 with the repository owner's approval.

Do not disclose vulnerabilities through public issues, discussions, or pull requests. If the private channel is unavailable, do not post sensitive details publicly; request a private contact method from the maintainer without describing the vulnerability.

Include:

- Affected version or commit and relevant source paths.
- Expected versus observed behavior and potential impact.
- Minimal reproduction using synthetic data in an environment you control.
- Sanitized logs and possible mitigations, if available.

Never submit API keys, `.env` contents, customer records, or private corpus data. Reports can be assessed and disclosure coordinated through the private advisory thread; no fixed response deadline is guaranteed.

## Operational boundaries

Live ingestion sends configured queries to Exa and can incur charges. Budget flags are estimates after fetching, not hard provider limits. Generated workflow plans do not execute exercises or enforce the printed authorization/scope assumptions. See the [CLI guide](library/knowledge/public/usage/cli-guide.md) and [runbook](library/knowledge/private/operations/runbook.md).

CI and CodeQL execution remain inactive for billing reasons. Private reporting and secret-scanning settings are separate from CI; their presence is not proof that the application has been comprehensively security-tested.
