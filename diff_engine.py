import sqlite3
from datetime import datetime
from config import DATABASE

def update_database(videos):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    for v in videos:
        c.execute("SELECT video_id FROM videos WHERE video_id = ?", (v["video_id"],))
        exists = c.fetchone()

        if not exists:
            c.execute("""
            INSERT INTO videos VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                v["video_id"],
                v["upload_date"],
                datetime.utcnow().isoformat(),
                datetime.utcnow().isoformat(),
                v["views"],
                v["likes"],
                v["comments"]
            ))
        else:
            c.execute("""
            UPDATE videos SET
            last_seen = ?,
            views = ?,
            likes = ?,
            comments = ?
            WHERE video_id = ?
            """, (
                datetime.utcnow().isoformat(),
                v["views"],
                v["likes"],
                v["comments"],
                v["video_id"]
            ))

    conn.commit()
    conn.close()

def detect_deleted(current_videos):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    current_ids = {v["video_id"] for v in current_videos}
    c.execute("SELECT video_id FROM videos")
    db_ids = {row[0] for row in c.fetchall()}

    conn.close()

    return list(db_ids - current_ids)