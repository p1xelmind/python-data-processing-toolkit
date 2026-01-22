from dataclasses import dataclass
from typing import Any, Dict, Tuple, Type, Iterable, List

@dataclass(frozen=True)
class FieldSchema:
    name: str
    types: Tuple[Type, ...]
    required: bool = True


@dataclass(frozen=True)
class RecordSchema:
    fields: Dict[str, FieldSchema]
    allow_extra_fields: bool = True


def validate_record(record: Dict[str, Any], schema: RecordSchema) -> bool:
    for field_name, field_schema in schema.fields.items():
        if field_schema.required and field_name not in record:
            return False

    for field_name, value in record.items():
        if field_name not in schema.fields:
            if schema.allow_extra_fields:
                continue
            else:
                return False

        field_schema = schema.fields[field_name]

        if not isinstance(value, field_schema.types):
            return False

    return True


def validate_records(
    records: Iterable[Dict[str, Any]],
    schema: RecordSchema
) -> List[Dict[str, Any]]:
    valid_records = []

    for record in records:
        if validate_record(record, schema):
            valid_records.append(record)

    return valid_records