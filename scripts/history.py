"""List relevant recent themes and today's files without mutating them."""
import argparse
import json
import re
from datetime import date, timedelta
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("directory", type=Path)
parser.add_argument("--date", default=date.today().isoformat())
parser.add_argument("--days", type=int, default=14)
args = parser.parse_args()
today = date.fromisoformat(args.date)
start = today - timedelta(days=args.days)
records = {}
for path in sorted(args.directory.iterdir()) if args.directory.exists() else []:
    if not path.is_file():
        continue
    match = re.match(r"^(\d{4}-\d{2}-\d{2})_(.+?)(?:_caption\.txt|_\d{2}(?:_.+)?\.png)$", path.name)
    if not match:
        continue
    used = date.fromisoformat(match[1])
    if start <= used <= today:
        key = (match[1], match[2])
        item = records.setdefault(key, {"date": match[1], "theme": match[2], "files": []})
        item["files"].append(str(path))
        if path.name.endswith("_caption.txt"):
            item["caption"] = path.read_text(encoding="utf-8-sig", errors="replace")
print(json.dumps({"today": today.isoformat(), "records": list(records.values())}, ensure_ascii=False, indent=2))

