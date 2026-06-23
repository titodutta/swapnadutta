#!/usr/bin/env python3

import subprocess
import os
import re
from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import PlainScalarString, SingleQuotedScalarString

# ==============================================================================
# PHASE 0: RAW TEXT LINE FILTER (Fixes pre-existing unquoted times before loading)
# ==============================================================================
if os.path.exists("_data/gallery.yml"):
    with open("_data/gallery.yml", "r", encoding="utf-8") as f:
        raw_lines = f.readlines()

    cleaned_lines = []
    for line in raw_lines:
        if line.startswith("  time: ") and not ("'" in line or '"' in line):
            val = line.replace("  time: ", "").strip()
            # If it's a corrupted numerical value, we strip it out completely 
            # so the EXIF logic below can clean it up and pull fresh text
            if "." in val or val.isdigit():
                continue
            cleaned_lines.append(f"  time: '{val}'\n")
        else:
            cleaned_lines.append(line)

    with open("_data/gallery.yml", "w", encoding="utf-8") as f:
        f.writelines(cleaned_lines)

# Initialize the YAML round-trip parser
yaml = YAML()
yaml.preserve_quotes = True  # Changed to True to respect explicit quote forcing
yaml.width = 4096             

def represent_none(self, data):
    return self.represent_scalar('tag:yaml.org,2002:null', 'null')

def string_representer(mapping, data):
    # FIX: If the data already has an explicit scalar string style (like single quotes), 
    # preserve its style instead of overriding it with style=''
    if hasattr(data, 'style'):
        return mapping.represent_scalar('tag:yaml.org,2002:str', str(data), style=data.style)
    return mapping.represent_scalar('tag:yaml.org,2002:str', str(data), style='')

yaml.representer.add_representer(type(None), represent_none)
yaml.representer.add_representer(str, string_representer)

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

reordered_photos = []

for photo in photos:
    photo_id = photo.get("id", "UNKNOWN_ID")
    file_name = photo.get("file", "UNKNOWN_FILE")

    if not photo.get("exif"):
        reordered_photos.append(photo)
        continue

    # Clean check to identify corrupted numerical times
    raw_time_val = str(photo.get("time", ""))
    is_time_corrupted = ("." in raw_time_val) or (raw_time_val.isdigit())

    # FORCE BACKFILL GATE: If time is corrupted, force backfill execution
    has_date = bool(photo.get("date"))
    has_time = bool(photo.get("time")) and not is_time_corrupted
    has_camera = bool(photo.get("camera"))
    has_gps = bool(photo.get("coordinates"))

    if has_date and has_time and has_camera and has_gps:
        reordered_photos.append(photo)
        continue

    image = f"assets/images/gallery/{file_name}"
    
    if not os.path.exists(image):
        print(f"⚠️ Warning: Missing target asset path for {photo_id} ({file_name}). Skipping EXIF loop.")
        reordered_photos.append(photo)
        continue

    record_updated = False
    log_details = []

    try:
        # 1. Extract Date and Time cleanly
        if not has_date or not has_time:
            exif_date = get_exif_field(image, "-DateTimeOriginal")
            if exif_date and len(exif_date) >= 16:
                raw_date = exif_date[:10].replace(":", "-", 2)
                raw_time = exif_date[11:16]  # e.g., "16:24"
                
                if not has_date:
                    photo["date"] = PlainScalarString(raw_date)
                    record_updated = True
                    log_details.append(f"Date: {photo['date']}")
                    
                # Overwrites the corrupted numerical time with a fresh, quoted string literal
                if not has_time:
                    photo["time"] = SingleQuotedScalarString(raw_time)
                    record_updated = True
                    log_details.append(f"Time: {photo['time']}")

        # 2. Extract Camera Model
        if not has_camera:
            camera_model = get_exif_field(image, "-Model")
            if camera_model:
                photo["camera"] = PlainScalarString(camera_model)
                record_updated = True
                log_details.append(f"Cam: {photo['camera']}")

        # 3. Extract GPS Coordinates
        if not has_gps:
            gps_lat = get_exif_field(image, "-GPSLatitude#")
            gps_lon = get_exif_field(image, "-GPSLongitude#")
            
            if gps_lat and gps_lon:
                try:
                    lat_float = round(float(gps_lat), 6)
                    lon_float = round(float(gps_lon), 6)
                    
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

                    if not is_blocked:
                        photo["coordinates"] = [lat_float, lon_float]
                        record_updated = True
                        log_details.append(f"GPS: {photo['coordinates']}")
                except Exception:
                    pass

    except Exception as error_msg:
        print(f"❌ PIPELINE EXCEPTION on ID {photo_id} ({file_name}): {error_msg}")
        reordered_photos.append(photo)
        continue

    if record_updated:
        updated += 1
        print(f"{photo['id']} -> {' | '.join(log_details)}")

    # STABLE FIELD REORDERING
    ordered_entry = yaml.map()
    ordered_entry["id"] = photo.get("id")
    ordered_entry["file"] = photo.get("file")
    ordered_entry["exif"] = photo.get("exif")
    
    ordered_entry["location_en"] = photo.get("location_en")
    ordered_entry["location_bn"] = photo.get("location_bn")
    ordered_entry["people_en"] = photo.get("people_en", [])
    ordered_entry["people_bn"] = photo.get("people_bn", [])
    ordered_entry["tags_en"] = photo.get("tags_en", [])
    ordered_entry["tags_bn"] = photo.get("tags_bn", [])
    ordered_entry["alt_en"] = photo.get("alt_en")
    ordered_entry["alt_bn"] = photo.get("alt_bn")
    ordered_entry["caption_en"] = photo.get("caption_en")
    ordered_entry["caption_bn"] = photo.get("caption_bn")
    
    if photo.get("date"): ordered_entry["date"] = PlainScalarString(str(photo["date"]))
    if photo.get("time"): ordered_entry["time"] = SingleQuotedScalarString(str(photo["time"]))
    if photo.get("camera"): ordered_entry["camera"] = PlainScalarString(str(photo["camera"]))
    if photo.get("coordinates"): ordered_entry["coordinates"] = photo["coordinates"]

    reordered_photos.append(ordered_entry)

with open("_data/gallery.yml", "w", encoding="utf-8") as f:
    yaml.dump(reordered_photos, f)

with open("_data/gallery.yml", "r", encoding="utf-8") as f:
    content = f.read()

formatted_content = re.sub(r"\n- id:", r"\n\n- id:", content)

with open("_data/gallery.yml", "w", encoding="utf-8") as f:
    f.write(formatted_content)

print()
print(f"Done. Processed metadata cleanly with single-quoted timestamps fixed. Total files updated: {updated}")