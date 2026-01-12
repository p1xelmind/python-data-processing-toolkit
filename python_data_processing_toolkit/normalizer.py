from typing import Any, Dict, List, Union

def normalize(data: Union[str, Dict[str, Any], List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
    if isinstance(data, list):
        return data
    
    if isinstance(data, dict):
        return [data]
    
    raise TypeError("Only structured data (dict or list of dicts) can be normalized")