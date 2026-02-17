import sqlite3
from config import DATABASE

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS videos (
        video_id TEXT PRIMARY KEY,
        upload_date TEXT,
        first_seen TEXT,
        last_seen TEXT,
        views INTEGER,
        likes INTEGER,
        comments INTEGER
    )
    """)
    conn.commit()
    conn.close()