from pathlib import Path
import cvs
import json

def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")