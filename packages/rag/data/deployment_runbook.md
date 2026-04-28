# deployment_runbook.md

## Deployment Runbook

# Before Deploy

Verify:

* tests green
* config reviewed
* rollback path known
* monitoring available

---

## Deploy Sequence

1. Announce if needed
2. Deploy
3. Verify health
4. Check logs/metrics
5. Watch for regressions

Deploy is not finished at step 2.

---

## If Things Go Wrong

* Stabilize
* Roll back if needed
* Escalate early
* Capture facts

Do not improvise heroically.

---

## The Calm Rule

Move deliberately.
Fast panic is slower than calm action.

---

## Friday Rule

Be extra skeptical of risky Friday deploys.
The rule exists because history exists.
