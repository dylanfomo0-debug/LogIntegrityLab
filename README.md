# Can Security Logs Reveal Their Own Tampering?

A synthetic log-integrity lab that creates normal authentication logs, injects controlled manipulation, and tests simple detection checks.

## Research question

> Which forms of log manipulation are easiest to detect using timestamps, sequence checks, and event consistency?

## Tampering scenarios

- duplicate events
- impossible timestamp order
- missing time gaps
- invalid usernames
- sudden source-IP changes

## Run it

```bash
python3 -m src.evaluate
python3 -m unittest discover -s tests -v
```

No real logs are used. The generator produces toy data locally.

## Curiosity prompts

- Can a missing event be detected without a trusted sequence number?
- Which checks create false positives during legitimate maintenance?
- Does adding a hash chain make edits easier to identify?
- What evidence should be stored outside the system being monitored?

## Limitations

This is an educational model, not a replacement for a SIEM or forensic process. Real systems need synchronized clocks, access controls, retention policies, and an external trust anchor.
## Project reflection

- **What I personally implemented:** I wrote the normal-log generator, controlled tampering functions, sequence/timestamp/user/IP consistency checks, evaluation script, and unit tests.
- **One actual result:** All **4 tests passed**; the evaluation produced **0 findings for normal logs** and **1 finding for each** injected duplicate, reordered event, gap, invalid user, and new-IP scenario.
- **One unexpected result:** Reordering two events produced one timestamp-reversal finding rather than a separate sequence-order finding, because the current checker detects duplicate sequence numbers but does not require sequence numbers to arrive in order.
- **One limitation:** The implementation cannot prove that a log was untampered with; it only flags inconsistencies and cannot detect a carefully edited event that remains internally consistent.
- **Next iteration:** I intend to add a hash chain with an external checkpoint and test whether it detects edits that preserve timestamps and sequence numbers.
