from __future__ import annotations

from dataclasses import dataclass

from YaEC.model.base import BaseDataModel


@dataclass
class Cart(BaseDataModel):
    def to_dict(self) -> dict[str, str]:
        return super().to_dict()

    @classmethod
    def from_dict(cls, data: dict[str, str]) -> Cart:
        pass
