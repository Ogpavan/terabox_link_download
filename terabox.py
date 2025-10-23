import json
import os
from TeraboxDL import TeraboxDL

LINKS_JSON = "links.json"
COOKIE = "lang=en; ndus=Y235yeyteHuigO3_I6Maq4TWdFhDnP-fA8boAT-x; ndut_fmt=6165933440C52348F20F8D7E664BB765179D9AE16422BD454BE5EC13FB1ABA1F"
SAVE_DIR = "videos"
MAX_SIZE_MB = 50

def main():
    # Ensure save directory exists
    os.makedirs(SAVE_DIR, exist_ok=True)

    # Load links
    with open(LINKS_JSON, "r", encoding="utf-8") as f:
        links = json.load(f)

    tb = TeraboxDL(COOKIE)

    for idx, link in enumerate(links, 1):
        print(f"\n[{idx}/{len(links)}] Checking: {link}")
        try:
            info = tb.get_file_info(link)
            if "error" in info:
                print("❌ Error retrieving file info:", info["error"])
                continue

            file_size_str = info.get("file_size", "0 MB")
            try:
                size_val, size_unit = file_size_str.split()
                size_val = float(size_val)
                if size_unit.upper() == "GB":
                    file_size_mb = size_val * 1024
                else:
                    file_size_mb = size_val
            except Exception:
                file_size_mb = 0
            file_name = info.get("file_name", "unknown")

            print(f"📁 File: {file_name} | Size: {file_size_mb:.2f} MB")

            if file_size_mb > MAX_SIZE_MB:
                print(f"⏩ Skipped: File size {file_size_mb:.2f} MB > {MAX_SIZE_MB} MB")
                continue

            result = tb.download(info, save_path=SAVE_DIR, callback=None)
            if "error" in result:
                print("❌ Download error:", result["error"])
            else:
                print(f"✅ Downloaded: {result['file_path']}")

        except Exception as e:
            print(f"⚠️ Unexpected error: {e}")

if __name__ == "__main__":
    main()