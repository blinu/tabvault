import hashlib
from datetime import datetime

def hash_content(content: str) -> str:
    return hashlib.sha256(content.encode()).hexdigest()[:8]

def make_header(original_name: str) -> str:
    now = datetime.now().isoformat()
    return f"""# tabvault extracted file
# original: {original_name}
# extracted: {now}
# description: TODO

"""
