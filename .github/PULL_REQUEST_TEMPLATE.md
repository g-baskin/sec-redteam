## What and why

Describe the change, its purpose, and any related issue.

## Implementation and scope

Describe important decisions, limitations, and anything intentionally deferred.

## Verification

List the commands actually run and their results. CI is intentionally inactive for billing reasons; do not claim a hosted check ran. Mark unrun checks explicitly.

## Checklist

- [ ] Existing tests pass locally (`python3 -m pytest` with development dependencies installed), or I explained why they could not run
- [ ] Relevant documentation and notable `Unreleased` changelog entries are updated
- [ ] No credentials, .env values, or collected corpus data appear in the diff
- [ ] CI, CodeQL and dependency automation remain inactive unless separately approved
- [ ] Required review is complete; passing checks alone are not merge approval
