from dataclasses import dataclass
from typing import Any, Tuple, Type, Dict

@dataclass(frozen=True)
class FieldSchema:
    name: str
    types: Tuple[Type, ...]
    required: bool = True


@dataclass(frozen=True)
class RecordSchema:
    fields: Dict[str, FieldSchema]
    allow_extra_fields: bool = True


def validate_record(
        record: Dict[str, Any],
        schema: RecordSchema
) -> bool: