# example_incident_postmortem.md

## Incident Postmortem Example

Incident:
RAG assistant returned stale architectural guidance after outdated chunks dominated retrieval.

Impact:
Incorrect guidance shown internally.
No customer harm.

Root Cause:
Chunk refresh pipeline had silently failed.

Contributing Factors:

* missing freshness checks
* weak monitoring
* overconfidence in retrieval quality

Resolution:

* fixed ingest job
* added freshness metadata
* added retrieval evaluation checks

Lessons:
Retrieval quality is an operational concern, not only model concern.

Blameless Note:
Failure emerged from system gaps, not individual negligence.
