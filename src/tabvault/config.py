from pathlib import Path

NOTEPADPP_BACKUP = Path.home() / "AppData/Roaming/Notepad++/backup"

OUTPUT_DIR = Path.cwd() / "output"
RAW_DIR = OUTPUT_DIR / "_raw"

CLASSIFIERS = {
    "kubernetes": ["kubectl", "helm"],
    "docker": ["docker"],
    "git": ["git "],
    "sql": ["SELECT ", "INSERT ", "UPDATE ", "DELETE "],
    "powershell": ["Get-", "Set-", "New-"],
    "bash": ["sudo ", "chmod ", "grep "],
    "azure": ["az "],
    "aws": ["aws "],
}

DEFAULT_CATEGORY = "misc"
