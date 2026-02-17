import os
import json
from datetime import datetime

def normalize():
    data = []
    for file in os.listdir("raw"):
        if file.endswith(".info.json"):
            with open(os.path.join("raw", file)) as f:
                j = json.load(f)
            data.append({
                "video_id": j.get("id"),
                "upload_date": j.get("upload_date"),
                "views": j.get("view_count"),
                "likes": j.get("like_count"),
                "comments": j.get("comment_count"),
                "description": j.get("description"),
                "collected_at": datetime.utcnow().isoformat()
            })
    return data