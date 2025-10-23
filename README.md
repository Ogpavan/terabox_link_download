# 📦 Terabox Auto Downloader (with Size Limit Filter)

This Python script automates downloading files from **TeraBox** links stored in a JSON file, using the [`TeraboxDL`](https://github.com/Damantha126/TeraboxDL) library.  
It includes a **file size filter**, skipping any file larger than your defined limit (default: 50 MB).

---

## 🚀 Features

- ✅ Automatically downloads multiple TeraBox links.
- ✅ Skips files larger than a set limit.
- ✅ Displays detailed logs and progress.
- ✅ Creates the output folder automatically.
- ✅ Gracefully handles broken or invalid links.

---

## 📁 Project Structure

```bash
TeraboxDownloader/
├── terabox_downloader.py     # main script
├── links.json                # contains all terabox links
├── videos/                   # output directory (auto-created)
└── requirements.txt           # dependencies (optional)
⚙️ Installation & Setup
1️⃣ Clone or Download the Repository
bash
Copy code
git clone https://github.com/<your-username>/TeraboxDownloader.git
cd TeraboxDownloader
2️⃣ Install Required Packages
Make sure Python 3.8+ and pip are installed, then run:

bash
Copy code
pip install TeraboxDL
If permission issues occur:

bash
Copy code
pip install --user TeraboxDL
3️⃣ Create links.json
Create a file named links.json in the same directory:

json
Copy code
[
    "https://1024terabox.com/s/1xrcmgwzTwjnK2kJFApUhcg",
    "https://terabox.com/s/1abcdefghijk12345"
]
Each entry must be a valid TeraBox public share link.

🔑 Setting Your Cookie
The script needs your TeraBox cookie to authenticate downloads.

Steps to Get Cookie:
Open https://terabox.com and log in.

Press F12 → open Application → Cookies → https://terabox.com.

Copy the values of:

ndus

ndut_fmt

Combine them like this:

text
Copy code
lang=en; ndus=YOUR_NDUS; ndut_fmt=YOUR_NDUT_FMT
Example:

python
Copy code
COOKIE = "lang=en; ndus=Y235yeyteHuigO3_I6Maq4TWdFhDnP-fA8boAT-x; ndut_fmt=6165933440C52348F20F8D7E664BB765179D9AE16422BD454BE5EC13FB1ABA1F"
⚙️ Configuration Options
Modify these variables at the top of the script:

Variable	Description	Default
LINKS_JSON	JSON file containing links	"links.json"
COOKIE	Your TeraBox cookie	(required)
SAVE_DIR	Directory to save files	"videos"
MAX_SIZE_MB	Maximum allowed file size in MB	50

Example to allow larger files:

python
Copy code
MAX_SIZE_MB = 500  # Allow up to 500 MB per file
▶️ Running the Script
Once configured, simply run:

bash
Copy code
python terabox_downloader.py
🧾 Example Terminal Output
bash
Copy code
[1/3] Checking: https://1024terabox.com/s/1xrcmgwzTwjnK2kJFApUhcg
📁 File: example_video.mp4 | Size: 45.22 MB
✅ Downloaded: videos/example_video.mp4

[2/3] Checking: https://1024terabox.com/s/1anotherlink
📁 File: large_movie.mp4 | Size: 1050.00 MB
⏩ Skipped: File size 1050.00 MB > 50 MB

[3/3] Checking: https://invalidlink
❌ Error retrieving file info: invalid link or expired
🧠 How It Works
Reads all links from links.json.

Retrieves each file’s metadata via TeraboxDL.

Compares its size with the MAX_SIZE_MB threshold.

Downloads the file only if it passes the check.

Saves the file in the videos/ folder.
