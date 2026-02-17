import subprocess
import os
from config import USERNAME

def collect():
    os.makedirs("raw", exist_ok=True)
    cmd = [
        "python3", "-m", "yt_dlp",
        f"https://www.tiktok.com/@{USERNAME}",
        "--write-info-json",
        "--skip-download",
        "-o", "raw/%(id)s"
    ]
    subprocess.run(cmd)