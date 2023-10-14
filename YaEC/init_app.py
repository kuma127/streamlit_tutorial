from pathlib import Path
from tempfile import TemporaryDirectory

from YaEC.session import StreamlitSessionManager
from .mock import MockDB, MockSessionDB
from YaEC.application import BasePage, MultiPageApp
from YaEC.pages.login import LoginPage
from YaEC.pages.itemlist import ItemListPage
from YaEC.const import PageId
from YaEC.services.auth import MockAuthAPIClientService
from YaEC.services.user import MockUserAPIClientService
from YaEC.services.item import MockItemAPIClientService


def init_session() -> StreamlitSessionManager:
    mockdir = Path(TemporaryDirectory().name)
    mockdir.mkdir(exist_ok=True)
    mockdb = MockDB(mockdir.joinpath("mock.db"))
    session_db = MockSessionDB(mockdir.joinpath("session.json"))
    ssm = StreamlitSessionManager(
        auth_api_client=MockAuthAPIClientService(mockdb, session_db),
        user_api_client=MockUserAPIClientService(mockdb, session_db),
        item_api_client=MockItemAPIClientService(mockdb)
    )
    return ssm


def init_pages(ssm: StreamlitSessionManager) -> list[BasePage]:
    pages = [
        LoginPage(page_id=PageId.PUBLIC_LOGIN, title="ログイン", ssm=ssm),
        ItemListPage(page_id=PageId.PUBLIC_ITEM_LIST, title="商品一覧", ssm=ssm)
    ]
    return pages


# アプリケーションの初期化
def init_app(ssm: StreamlitSessionManager, pages: list[BasePage]) -> MultiPageApp:
    app = MultiPageApp(ssm, pages)
    return app
