from __future__ import annotations
from datetime import datetime, timedelta
from pathlib import Path
import csv


def normal_events():
    start = datetime(2026, 9, 1, 9, 0, 0)
    rows = []
    for i in range(12):
        rows.append({"sequence": i + 1, "timestamp": (start + timedelta(minutes=5*i)).isoformat(), "username": "alice" if i % 2 else "bob", "ip": "203.0.113.10", "status": "Success"})
    return rows

def tamper(rows, scenario):
    result = [dict(r) for r in rows]
    if scenario == "duplicate": result.insert(5, dict(result[4]))
    elif scenario == "reordered": result[3], result[4] = result[4], result[3]
    elif scenario == "gap": result.pop(6)
    elif scenario == "invalid_user": result[7]["username"] = "unknown-admin"
    elif scenario == "new_ip": result[8]["ip"] = "198.51.100.77"
    else: raise ValueError(scenario)
    return result

def write(path, rows):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["sequence", "timestamp", "username", "ip", "status"]); writer.writeheader(); writer.writerows(rows)

if __name__ == "__main__": write(Path(__file__).resolve().parents[1] / "data/normal.csv", normal_events())
