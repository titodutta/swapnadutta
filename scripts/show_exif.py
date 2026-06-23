#!/usr/bin/env python3

import subprocess
import os
import re
from ruamel.yaml import YAML
from ruamel.yaml.scalarstring import PlainScalarString

# Initialize the YAML round-trip parser
yaml = YAML()
yaml.preserve_quotes = False  
yaml.width = 4096             

# Force all strings and dates to be completely plain (drops single quotes)
def represent_none(self, data):
    return self.represent_scalar('tag:yaml.org,2002:null', 'null')

def string_representer(mapping, data):
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
    if not photo.get("exif"):
        reordered_photos.append(photo)
        continue

    # FORCE BACKFILL GATE: If it has EXIF but no coordinates key, parse it!
    if photo.get("exif") and not photo.get("coordinates"):
        has_date = bool(photo.get("date"))
        has_time = bool(photo.get("time"))
        has_camera = bool(photo.get("camera"))
        has_gps = False
    else:
        # Standard safety gate for everything else
        has_date = bool(photo.get("date"))
        has_time = bool(photo.get("time"))
        has_camera = bool(photo.get("camera"))
        has_gps = bool(photo.get("coordinates"))
        if has_date and has_time and has_camera and has_gps:
            reordered_photos.append(photo)
            continue

    image = f"assets/images/gallery/{photo['file']}"
    record_updated = False
    log_details = []

    # 1. Extract Date and Time cleanly as strict string representations
    if not has_date or not has_time:
        exif_date = get_exif_field(image, "-DateTimeOriginal")
        if exif_date and len(exif_date) >= 16:
            raw_date = exif_date[:10].replace(":", "-", 2)
            raw_time = exif_date[11:16]  # e.g., "16:24"
            
            if not has_date:
                photo["date"] = PlainScalarString(raw_date)
                record_updated = True
                log_details.append(f"Date: {photo['date']}")
                
            if not has_time:
                photo["time"] = PlainScalarString(raw_time)
                record_updated = True
                log_details.append(f"Time: {photo['time']}")

    # 2. Extract Camera Model
    if not has_camera:
        camera_model = get_exif_field(image, "-Model")
        if camera_model:
            photo["camera"] = PlainScalarString(camera_model)
            record_updated = True
            log_details.append(f"Cam: {photo['camera']}")

    # 3. Extract GPS Coordinates with Privacy Firewall Checked
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

    if record_updated:
        updated += 1
        print(f"{photo['id']} -> {' | '.join(log_details)}")

    # STABLE FIELD REORDERING: Construct a clean mapping order explicitly
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
    
    # Force string evaluation on existing dates/times to wrap them safely into strict text
    if photo.get("date"): ordered_entry["date"] = PlainScalarString(str(photo["date"]))
    if photo.get("time"): ordered_entry["time"] = PlainScalarString(str(photo["time"]))
    if photo.get("camera"): ordered_entry["camera"] = PlainScalarString(str(photo["camera"]))
    if photo.get("coordinates"): ordered_entry["coordinates"] = photo["coordinates"]

    reordered_photos.append(ordered_entry)

# Write the file and inject clean formatting breaks between elements
with open("_data/gallery.yml", "w", encoding="utf-8") as f:
    yaml.dump(reordered_photos, f)

# POST-PROCESSING: Read back the raw text file and place a newline break before each list item
with open("_data/gallery.yml", "r", encoding="utf-8") as f:
    content = f.read()

# Re-adds structural breaks right before every clean list dashboard indicator
formatted_content = re.sub(r"\n- id:", r"\n\n- id:", content)

with open("_data/gallery.yml", "w", encoding="utf-8") as f:
    f.write(formatted_content)

print()
print(f"Updated records. Pristine layout with clean entry spacing restored.")