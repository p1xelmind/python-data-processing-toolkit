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


def group_mean(
        records: List[Dict[str, Any]],
        group_field: str,
        value_field: str
) -> Dict[Any, float]:
    result = {}
    groups = {}

    for record in records:
        if group_field not in record or value_field not in record:
            continue

        group_value = record[group_field]

        if group_value in groups:
            try:
                groups[group_value]["sum"] += float(record[value_field])
                groups[group_value]["count"] += 1
            except(TypeError, ValueError):
                continue
        else:
            try:
                groups[group_value] = {"sum": float(record[value_field]), "count": 1}
            except(TypeError, ValueError):
                continue

    for group_value, data in groups.items():
        result[group_value] = data["sum"] / data["count"]

    return result