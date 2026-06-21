#!/usr/bin/env python3

import subprocess
from ruamel.yaml import YAML

# Initialize the YAML round-trip parser
yaml = YAML()
yaml.preserve_quotes = False  # Drops unnecessary quotes for strings
yaml.default_style = None     # Prevents quotes around plain strings/dates
yaml.width = 4096             # Prevents automatic line wrapping for long strings

with open("_data/gallery.yml", "r", encoding="utf-8") as f:
    photos = yaml.load(f)

updated = 0

for photo in photos:
    
    if not photo.get("exif"):
        continue

    if photo.get("date"):
        continue

    image = f"assets/images/gallery/{photo['file']}"

    result = subprocess.run(
        [
            "exiftool",
            "-s3",
            "-DateTimeOriginal",
            image
        ],
        capture_output=True,
        text=True
    )

    exif_date = result.stdout.strip()

    if exif_date:
        photo["date"] = exif_date[:10].replace(":", "-", 2)
        updated += 1
        print(f"{photo['id']} -> {photo['date']}")

with open("_data/gallery.yml", "w", encoding="utf-8") as f:
    yaml.dump(photos, f)

print()
print(f"Updated {updated} records")