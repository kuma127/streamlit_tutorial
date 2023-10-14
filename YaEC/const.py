from enum import Enum, auto


class PageId(Enum):
    PUBLIC_LOGIN = auto()
    PUBLIC_ITEM_LIST = auto()
    PAGE_ID = auto()


class SessionKey(Enum):
    AUTH_API_CLIENT = auto()
    USER_API_CLIENT = auto()
    ITEM_API_CLIENT = auto()
    USER = auto()
    SESSION_ID = auto()
    USERBOX = auto()
    PAGE_ID = auto()


class UserRole(Enum):
    ADMIN = auto()
    MEMBER = auto()
