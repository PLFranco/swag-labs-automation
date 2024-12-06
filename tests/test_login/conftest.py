import pytest
from pages.login import SwagLabsLoginPage
from playwright.sync_api import Page

@pytest.fixture
def login_page(page: Page) -> SwagLabsLoginPage:
    return SwagLabsLoginPage(page)

