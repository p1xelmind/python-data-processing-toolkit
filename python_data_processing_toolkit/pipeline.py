from typing import Any, Iterable, Dict, List, Callable, Optional
from pathlib import Path
from loader import load_text
from normalizer import normalize
from schema import validate_records, RecordSchema

def run_pipeline(
        source: Any,
        *,
        schema: Optional[Any] = None,
        filters: Optional[List[Callable[[Dict[str,Any]], bool]]] = None,
        aggregation: Optional[Callable[[List[Dict[str, Any]]], Any]] = None
) -> Any:
    path = Path(source)
    raw_data = load_text(path)
    records = normalize(raw_data)
    
    if filters is not None:
        filtered_records = []
    
        for record in records:
            keep = True

            for filter_fn in filters:
                if not filter_fn(record):
                    keep = False
                    break

            if keep:
                filtered_records.append(record)