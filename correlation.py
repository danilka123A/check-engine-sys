import hashlib
import re

def generate_username_variations(username):
    base = username.replace("_", "").replace("-", "").replace(".", "")
    variations = set()

    variations.add(username)
    variations.add(base)

    separators = ["_", "-", "."]
    for sep in separators:
        parts = re.split(r"[_\-.]", username)
        if len(parts) > 1:
            variations.add(sep.join(parts))

    if username[-2:].isdigit():
        variations.add(username[:-2])

    return list(variations)


def hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()


def extract_hashtags(description):
    if not description:
        return []
    return re.findall(r"#\w+", description)


def extract_mentions(description):
    if not description:
        return []
    return re.findall(r"@\w+", description)