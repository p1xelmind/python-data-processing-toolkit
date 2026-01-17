from typing import Any, List, Dict

def count(records: List[Dict[str, Any]]) -> int:
    return len(records)


def mean(
        records: List[Dict[str, Any]],
        field: str
) -> float | None:
    total = 0.0
    count = 0

    for record in records:
        if field not in record:
            continue

        value = record[field]

        try:
            numeric_value = float(value)
            total += numeric_value
            count += 1
        except (TypeError, ValueError):
            continue

    if count == 0:
        return None

    return total / count


def median(
        records: List[Dict[str, Any]],
        field: str
) -> float | None:
    values = []

    for record in records:
        if field not in record:
            continue

        value = record[field]

        try:
            numeric_value = float(value)
            values.append(numeric_value)
        except (TypeError, ValueError):
            continue

    if len(values) == 0:
        return None

    values.sort()
    countity_nums = len(values)

    if countity_nums % 2 != 0:
        return values[countity_nums//2]
    elif countity_nums % 2 == 0:
        return values[(countity_nums//2-1) + (countity_nums//2)] / 2 
    

def histogram(
        records: List[Dict[str, Any]],
        field: str
) -> Dict[Any, int]:
    result = {}

    for record in records:
        if field not in record:
            continue
        
        value = record[field]
        
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    
    return result


def group_by(
        records: List[Dict[str, Any]],
        field: str
) -> Dict[Any, List[Dict[str, Any]]]:
    result = {}
    
    for record in records:
        if field not in record:
            continue

        value = record[field]

        if value in result:
            result[value].append(record)
        else:
            result[value] = [record] 
    
    return result