import streamlit as st

from YaEC.const import SessionKey
from YaEC.services.auth import IAuthAPIClientService
from YaEC.services.user import IUserAPIClientService
from YaEC.services.item import IItemAPIClientService


class StreamlitSessionManager:
    def __init__(
        self,
        auth_api_client,
        user_api_client,
        item_api_client
    ) -> None:
        self._session_state = st.session_state
        self._session_state[SessionKey.AUTH_API_CLIENT.name] = auth_api_client
        self._session_state[SessionKey.USER_API_CLIENT.name] = user_api_client
        self._session_state[SessionKey.ITEM_API_CLIENT.name] = item_api_client

    def get_auth_api_client(self) -> IAuthAPIClientService:
        return self._session_state[SessionKey.AUTH_API_CLIENT.name]

    def get_user_api_client(self) -> IUserAPIClientService:
        return self._session_state[SessionKey.USER_API_CLIENT.name]

    def get_item_api_client(self) -> IItemAPIClientService:
        return self._session_state[SessionKey.ITEM_API_CLIENT.name]
