# good_pull_request_example.md

## Example of Strong Pull Request

Title:
feat: add fallback response when retrieval returns no context

Summary:
Adds guarded fallback behavior so assistant returns uncertainty response rather than hallucinated answer when retrieval yields empty results.

Why:
Observed failure mode during testing.

Testing:

* unit test added
* empty-context scenario tested
* regression check passed

Risks:
Minimal, touches response routing only.

Why this is good:

* focused scope
* explains intent
* documents risk
* includes validation

Reviewer note:
Good example of small, reviewable change.
