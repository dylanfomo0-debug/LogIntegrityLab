from .generate_logs import normal_events, tamper
from .detect_tampering import check

def main():
    print("Tampering scenario    Findings")
    print("-" * 34)
    for scenario in ("normal", "duplicate", "reordered", "gap", "invalid_user", "new_ip"):
        rows = normal_events() if scenario == "normal" else tamper(normal_events(), scenario)
        print(f"{scenario:<21} {len(check(rows))}")
    print("\nA finding is evidence for review, not proof of malicious intent.")

if __name__ == "__main__": main()
