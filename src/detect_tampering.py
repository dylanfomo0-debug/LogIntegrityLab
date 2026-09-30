from __future__ import annotations
from datetime import datetime

KNOWN_USERS = {"alice", "bob"}
KNOWN_IPS = {"203.0.113.10"}

def check(rows):
    findings = []
    previous = None
    seen_sequences = set()
    for row in rows:
        seq = int(row["sequence"]); current = datetime.fromisoformat(row["timestamp"])
        if seq in seen_sequences: findings.append((seq, "duplicate_sequence"))
        seen_sequences.add(seq)
        if previous and current < previous: findings.append((seq, "timestamp_reversed"))
        if row["username"] not in KNOWN_USERS: findings.append((seq, "unknown_user"))
        if row["ip"] not in KNOWN_IPS: findings.append((seq, "new_source_ip"))
        previous = current
    expected = set(range(1, max(seen_sequences) + 1)) if seen_sequences else set()
    for missing in sorted(expected - seen_sequences): findings.append((missing, "missing_sequence"))
    return findings
