from typing import Any, Dict, List

def filter_equals(
        records: List[Dict[str, Any]],
        field: str,
        value: Any
) -> List[Dict[str, Any]]:
    result = []

    for record in records:
        if field not in record:
            continue
        
        if record[field] == value:
            result.append(record)

    return result


def filter_range(
        records: List[Dict[str, Any]], 
        field: str,
        min_value: float,
        max_value: float
) -> List[Dict[str, Any]]:
    