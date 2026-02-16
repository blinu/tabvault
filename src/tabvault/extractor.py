import shutil
from pathlib import Path

def extract_file(source: Path, target: Path):
    shutil.copy2(source, target)
