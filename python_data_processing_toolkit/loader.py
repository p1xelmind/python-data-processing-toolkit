from pathlib import Path
import csv
import json
from typing import Any, Union, List, Dict

def load_text(path: Path) -> Union[str, Dict[str, Any], List[Dict[str, Any]]]:
    suffix = path.suffix.lower()

    if suffix == ".txt":
        return path.read_text(encoding="utf-8")

    if suffix == ".json":
        with path.open(encoding="utf-8") as file:
            return json.load(file)
    
    if suffix == ".csv":
        with path.open(encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)

    raise ValueError(f"Unsupported file type: {suffix}")