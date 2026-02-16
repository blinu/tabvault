from pathlib import Path
from tabvault.config import NOTEPADPP_BACKUP, OUTPUT_DIR, RAW_DIR
from tabvault.classifier import classify
from tabvault.utils import hash_content, make_header
from tabvault.extractor import extract_file

def ensure_dirs():
    OUTPUT_DIR.mkdir(exist_ok=True)
    RAW_DIR.mkdir(exist_ok=True)

def process_file(file_path: Path):
    content = file_path.read_text(errors="ignore")
    if not content.strip():
        return

    file_hash = hash_content(content)
    category = classify(content)

    category_dir = OUTPUT_DIR / category
    category_dir.mkdir(exist_ok=True)

    filename = f"{category}_{file_hash}.txt"

    raw_target = RAW_DIR / filename
    if not raw_target.exists():
        extract_file(file_path, raw_target)

    target = category_dir / filename
    if not target.exists():
        header = make_header(file_path.name)
        target.write_text(header + content)

    print(f"Processed {file_path.name}")

def run():
    print("tabvault starting...")
    ensure_dirs()

    if not NOTEPADPP_BACKUP.exists():
        print("Backup folder not found")
        return

    files = list(NOTEPADPP_BACKUP.glob("*"))

    for file in files:
        if file.is_file():
            process_file(file)

    print("done")
