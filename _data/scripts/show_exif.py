#!/usr/bin/env python3

import yaml
import subprocess

with open("_data/gallery.yml", "r", encoding="utf-8") as f:
    photos = yaml.safe_load(f)

for photo in photos:

    if not photo.get("exif"):
        continue

    image = f"assets/images/gallery/{photo['file']}"

    try:
        result = subprocess.run(
            [
                "exiftool",
                "-DateTimeOriginal",
                "-Model",
                "-GPSPosition",
                image
            ],
            capture_output=True,
            text=True,
            check=True
        )

        print("=" * 60)
        print(photo["id"])
        print(photo["file"])

        output = result.stdout.strip()

        if output:
            print(output)
        else:
            print("No useful EXIF metadata found")

    except Exception as e:
        print("=" * 60)
        print(photo["id"])
        print(f"ERROR: {e}")