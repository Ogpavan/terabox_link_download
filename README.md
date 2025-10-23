# terabox_link_download


This Python script automates downloading files from TeraBox links stored in a JSON file, using the TeraboxDL
 library.
It also includes an optional file size limit filter, so you can skip large files automatically (e.g., >50 MB).

🚀 Features

✅ Automatically downloads files from multiple TeraBox links.
✅ Skips files larger than a defined size (default: 50 MB).
✅ Displays progress, file size, and status logs.
✅ Handles errors and invalid links gracefully.
✅ Creates a target videos/ folder automatically.

📁 Project Structure
TeraboxDownloader/
├── terabox_downloader.py     # main script
├── links.json                # list of TeraBox links to download
├── videos/                   # output folder (auto-created)
└── requirements.txt          # dependencies (optional)

⚙️ Installation & Setup
1️⃣ Clone or Download the Repository
git clone https://github.com/<your-username>/TeraboxDownloader.git
cd TeraboxDownloader

2️⃣ Install Dependencies

Make sure you have Python 3.8+ and pip installed.

pip install TeraboxDL


(If you get permission issues, use pip install --user TeraboxDL.)

3️⃣ Create links.json

Create a links.json file in the same directory with your TeraBox share links:

[
    "https://1024terabox.com/s/1xrcmgwzTwjnK2kJFApUhcg",
    "https://terabox.com/s/1abcdefghijk12345"
]


Each link should be a valid TeraBox public share link.

🔑 Get Your Cookie

The script requires a valid TeraBox login cookie to access and download private or large files.

How to Get Cookie:

Open your browser (preferably Chrome).

Log in to https://terabox.com
.

Press F12 → Application → Cookies → https://terabox.com
.

Copy the value of these fields:

ndus

ndut_fmt

Combine them like this:

lang=en; ndus=YOUR_NDUS; ndut_fmt=YOUR_NDUT_FMT


Paste that into the script’s COOKIE variable.

Example:

COOKIE = "lang=en; ndus=Y235yeyteHuigO3_I6Maq4TWdFhDnP-fA8boAT-x; ndut_fmt=6165933440C52348F20F8D7E664BB765179D9AE16422BD454BE5EC13FB1ABA1F"

🧠 How It Works

The script loads all links from links.json.

For each link:

It retrieves the file info (name, size, etc.) using TeraboxDL.

It checks if the file size exceeds the defined limit (MAX_SIZE_MB).

If within the limit, it downloads and saves it inside the videos/ folder.

Any invalid or oversized files are skipped automatically.

⚙️ Configuration

You can adjust the following settings inside the script:

Variable	Description	Default
LINKS_JSON	Path to JSON file containing links	"links.json"
COOKIE	Your TeraBox cookie string	(must be filled manually)
SAVE_DIR	Directory where files will be saved	"videos"
MAX_SIZE_MB	Maximum allowed file size (in MB)	50

Example:
To allow larger files:

MAX_SIZE_MB = 500  # Allow files up to 500 MB

▶️ Usage

Once everything is configured:

python terabox_downloader.py


The script will:

Create the output folder (if not existing)

Check each link one by one

Print file info

Download eligible files

Skip or log any errors

🧾 Example Output
[1/3] Checking: https://1024terabox.com/s/1xrcmgwzTwjnK2kJFApUhcg
📁 File: example_video.mp4 | Size: 45.22 MB
✅ Downloaded: videos/example_video.mp4

[2/3] Checking: https://1024terabox.com/s/1anotherlink
📁 File: large_movie.mp4 | Size: 1050.00 MB
⏩ Skipped: File size 1050.00 MB > 50 MB

[3/3] Checking: https://invalidlink
❌ Error retrieving file info: invalid link or expired

🧩 Troubleshooting
Problem	Possible Fix
❌ Error retrieving file info	The link is invalid, private, or expired.
⚠️ Unexpected error: ...	Usually caused by a bad cookie or unstable network. Try refreshing the cookie.
File size shows 0 MB	The link might not point directly to a file (could be a folder).
Nothing downloads	Make sure the cookie is valid and not expired.
🌐 Deployment on Vercel or Web UI Integration

If you want to run this on a server and trigger downloads from a web page:

Use Flask or FastAPI to expose an API endpoint that runs this script.

You cannot directly deploy this Python script to Vercel because Vercel doesn’t support long-running Python processes or file writes.

Use Render, Replit, or Railway instead.

Example idea:

Create /api/download endpoint (Flask)

Accept JSON payload with links

Run the script logic in background

🧰 Example Enhancement Ideas

Add progress bar (e.g., with tqdm)

Add async/multithreaded downloads

Export logs to download_log.txt

Add Telegram bot to send results

Create simple HTML interface to upload links.json

🧑‍💻 Author

Developed by: Pawan Pal
Role: Full Stack Developer
GitHub: Ogpavan

🪪 License

This project uses the MIT License — free to use, modify, and distribute with attribution.
