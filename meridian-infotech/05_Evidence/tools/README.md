# Evidence tools

Scripts that collect evidence automatically instead of by hand (MIC-MTH-002, section 3).

## root_activity.py

Lists every change the AWS root user made in the last 14 days, in US East (N. Virginia), where identity and sign-in events are recorded, and in Asia Pacific (Mumbai). It saves the result as a dated JSON file and prints its SHA-256 fingerprint, which is recorded in MIC-EVD-001.

```bash
python -m venv .venv
source .venv/Scripts/activate        # Windows Git Bash; on Linux or macOS: source .venv/bin/activate
pip install -r requirements.txt
aws login --region ap-south-1
python root_activity.py
```

`botocore[crt]` is needed so that Python can use the keyless `aws login` session.

**Known limitation (v1):** read-only events are skipped by name prefix (Get, List, Describe). Events such as `Preferences_ListPaymentProfiles`, and console `Search` events, still appear. Version 2 will use CloudTrail's own read-only flag instead.

**Verified:** the first run (EV-013) reproduced every root event found by the manual audit of 24 September (EV-012), and found an earlier session that audit had only partly seen.
