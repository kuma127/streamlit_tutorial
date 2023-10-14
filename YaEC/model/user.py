from __future__ import annotations

from datetime import datetime, date
from dataclasses import dataclass

from YaEC.model.base import BaseDataModel
from YaEC.const import UserRole


@dataclass(frozen=True)
class User(BaseDataModel):
    user_id: str
    name: str
    birthday: date
    email: str
    role: UserRole

    def to_dict(self) -> dict[str, str]:
        return dict(
            user_id=self.user_id,
            name=self.name,
            birthday=self.birthday.isoformat(),
            email=self.email,
            role=self.role.name,
        )

    @classmethod
    def from_dict(cls, data: dict[str, str]) -> User:
        birthday = datetime.fromisoformat(data["birthday"])
        return User(
            user_id=data["user_id"],
            name=data["name"],
            birthday=birthday.date(),
            email=data["email"],
            role=UserRole[data["role"]],
        )
