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

def get_exif_field(image_path, tag):
    """Helper to fetch a single tag value cleanly using exiftool."""
    result = subprocess.run(
        ["exiftool", "-s3", tag, image_path],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

for photo in photos:
    # Only target records explicitly marked for EXIF parsing
    if not photo.get("exif"):
        continue

    # Gate: Only process if at least one target field is missing
    has_date = bool(photo.get("date"))
    has_camera = bool(photo.get("camera"))
    has_gps = bool(photo.get("coordinates"))

    if has_date and has_camera and has_gps:
        continue

    image = f"assets/images/gallery/{photo['file']}"
    record_updated = False
    log_details = []

    # 1. Extract Date (only if missing)
    if not has_date:
        exif_date = get_exif_field(image, "-DateTimeOriginal")
        if exif_date:
            photo["date"] = exif_date[:10].replace(":", "-", 2)
            record_updated = True
            log_details.append(f"Date: {photo['date']}")

    # 2. Extract Camera Model (only if missing)
    if not has_camera:
        camera_model = get_exif_field(image, "-Model")
        if camera_model:
            photo["camera"] = camera_model
            record_updated = True
            log_details.append(f"Cam: {photo['camera']}")

    # 3. Extract GPS Coordinates (only if missing)
    if not has_gps:
        gps_lat = get_exif_field(image, "-GPSLatitude#")
        gps_lon = get_exif_field(image, "-GPSLongitude#")
        
        if gps_lat and gps_lon:
            try:
                lat_float = round(float(gps_lat), 6)
                lon_float = round(float(gps_lon), 6)
                photo["coordinates"] = [lat_float, lon_float]
                record_updated = True
                log_details.append(f"GPS: {photo['coordinates']}")
            except ValueError:
                pass

    if record_updated:
        updated += 1
        print(f"{photo['id']} -> {' | '.join(log_details)}")

with open("_data/gallery.yml", "w", encoding="utf-8") as f:
    yaml.dump(photos, f)

print()
print(f"Updated {updated} records")