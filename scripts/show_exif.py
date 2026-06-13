#!/usr/bin/env python3

import yaml
import subprocess

with open("_data/gallery.yml", "r", encoding="utf-8") as f:
    photos = yaml.safe_load(f)

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
    yaml.dump(
        photos,
        f,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False
    )

print()
print(f"Updated {updated} records")