from dataclasses import dataclass
from typing import Any, Tuple, Type

@dataclass
class FieldSchema:
    name: str
    types: Tuple[Type, ...]
    required: bool = True