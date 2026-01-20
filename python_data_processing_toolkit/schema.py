from dataclasses import dataclass
from typing import Any, Tuple, Type

@dataclass(frozen=True)
class FieldSchema:
    name: str
    types: Tuple[Type, ...]
    required: bool = True

@dataclass(frozen=True)
class RecordSchema:
    fields: Tuple[FieldSchema, ...]