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
