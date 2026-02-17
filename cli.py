import argparse
from core.collector import collect
from core.normalizer import normalize
from core.storage import init_db
from core.diff_engine import update_database, detect_deleted
from core.correlation import generate_username_variations

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command")
    args = parser.parse_args()

    if args.command == "init":
        init_db()
        print("Database initialized.")

    elif args.command == "collect":
        collect()
        print("Collection complete.")

    elif args.command == "analyze":
        videos = normalize()
        update_database(videos)
        deleted = detect_deleted(videos)
        print("Database updated.")
        if deleted:
            print("Deleted videos detected:", deleted)

    elif args.command == "correlate":
        from config import USERNAME
        variations = generate_username_variations(USERNAME)
        print("Username variations:")
        for v in variations:
            print("-", v)

    else:
        print("Unknown command.")

if __name__ == "__main__":
    main()