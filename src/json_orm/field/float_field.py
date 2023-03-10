from typing import Any

from json_orm.field.field_base import FieldBase


class FloatField(FieldBase[float]):
    def type_factory(self, value: Any) -> float:
        return float(value)
