"""Root activity report.

Lists every change the AWS root user made in recent days, across the regions we use,
saves the result as an evidence file, and prints the file's SHA-256 fingerprint.
"""

import hashlib
import json
from datetime import datetime, timedelta, timezone

import boto3

# Identity and sign-in events are recorded in N. Virginia; our resources live in Mumbai.
REGIONS = ["us-east-1", "ap-south-1"]
DAYS_BACK = 14
READ_ONLY_PREFIXES = ("Get", "List", "Describe")  # these only look, they don't change anything


def root_changes(region, start, end):
    """Return the root user's non-read-only events in one region."""
    client = boto3.client("cloudtrail", region_name=region)
    paginator = client.get_paginator("lookup_events")  # results come in pages; this fetches them all
    pages = paginator.paginate(
        LookupAttributes=[{"AttributeKey": "Username", "AttributeValue": "root"}],
        StartTime=start,
        EndTime=end,
    )

    changes = []
    for page in pages:
        for event in page["Events"]:
            name = event["EventName"]
            if name.startswith(READ_ONLY_PREFIXES):
                continue  # skip anything that only reads
            changes.append({
                "time": event["EventTime"].astimezone(timezone.utc).isoformat(),
                "region": region,
                "event": name,
            })
    return changes


def main():
    end = datetime.now(timezone.utc)
    start = end - timedelta(days=DAYS_BACK)

    all_changes = []
    for region in REGIONS:
        all_changes.extend(root_changes(region, start, end))
    all_changes.sort(key=lambda change: change["time"])

    print(f"Root activity, last {DAYS_BACK} days: {len(all_changes)} change events\n")
    for change in all_changes:
        print(f"{change['time']}  {change['region']:<11}  {change['event']}")

    # Save the evidence. It holds times, regions and event names only: no account ID.
    report = {
        "generated_at": end.isoformat(),
        "window_days": DAYS_BACK,
        "regions": REGIONS,
        "events": all_changes,
    }
    filename = f"root_activity_{end:%Y-%m-%d}.json"
    data = json.dumps(report, indent=2).encode("utf-8")
    with open(filename, "wb") as evidence_file:
        evidence_file.write(data)

    # Seal it: if anyone later changes a single character, this fingerprint won't match.
    fingerprint = hashlib.sha256(data).hexdigest()
    print(f"\nSaved {filename}")
    print(f"SHA-256: {fingerprint}")


if __name__ == "__main__":
    main()
