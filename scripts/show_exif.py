#!/usr/bin/env python3

import subprocess
import os
import re
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

    # Gate: Check exactly what keys are already present
    has_date = bool(photo.get("date"))
    has_time = bool(photo.get("time"))
    has_camera = bool(photo.get("camera"))
    has_gps = bool(photo.get("coordinates"))

    # If everything is already filled, move to the next file safely
    if has_date and has_time and has_camera and has_gps:
        continue

    image = f"assets/images/gallery/{photo['file']}"
    record_updated = False
    log_details = []

    # 1. Extract Date and Time from -DateTimeOriginal
    if not has_date or not has_time:
        exif_date = get_exif_field(image, "-DateTimeOriginal")
        if exif_date and len(exif_date) >= 16:
            # Format pattern: "2018:10:13 06:32:54"
            raw_date = exif_date[:10].replace(":", "-", 2)
            raw_time = exif_date[11:16] # Extracts "06:32"
            
            if not has_date:
                photo["date"] = raw_date
                record_updated = True
                log_details.append(f"Date: {photo['date']}")
                
            if not has_time:
                photo["time"] = raw_time
                record_updated = True
                log_details.append(f"Time: {photo['time']}")

    # 2. Extract Camera Model
    if not has_camera:
        camera_model = get_exif_field(image, "-Model")
        if camera_model:
            photo["camera"] = camera_model
            record_updated = True
            log_details.append(f"Cam: {photo['camera']}")

    # 3. Extract GPS Coordinates with Local Privacy Box Checks
    if not has_gps:
        gps_lat = get_exif_field(image, "-GPSLatitude#")
        gps_lon = get_exif_field(image, "-GPSLongitude#")
        
        if gps_lat and gps_lon:
            try:
                lat_float = round(float(gps_lat), 6)
                lon_float = round(float(gps_lon), 6)
                
                # Check for hidden local privacy configuration boundaries
                is_blocked = False
                if os.path.exists(".env.local"):
                    with open(".env.local", "r", encoding="utf-8") as env_f:
                        env_data = env_f.read()
                        lat_min = float(re.search(r"BLOCK_LAT_MIN=(.+)", env_data).group(1))
                        lat_max = float(re.search(r"BLOCK_LAT_MAX=(.+)", env_data).group(1))
                        lon_min = float(re.search(r"BLOCK_LON_MIN=(.+)", env_data).group(1))
                        lon_max = float(re.search(r"BLOCK_LON_MAX=(.+)", env_data).group(1))
                        
                        if (lat_min <= lat_float <= lat_max) and (lon_min <= lon_float <= lon_max):
                            is_blocked = True

                if is_blocked:
                    # Silently bypass saving some locations
                    pass
                else:
                    photo["coordinates"] = [lat_float, lon_float]
                    record_updated = True
                    log_details.append(f"GPS: {photo['coordinates']}")
            except Exception:
                pass

    if record_updated:
        updated += 1
        print(f"{photo['id']} -> {' | '.join(log_details)}")

with open("_data/gallery.yml", "w", encoding="utf-8") as f:
    yaml.dump(photos, f)

print()
print(f"Updated {updated} records")