import pytest
from pages.login import SwagLabsLoginPage
from playwright.sync_api import Page

@pytest.fixture
def login_user(page: Page) -> None:
    login_page = SwagLabsLoginPage(page)
    login_page.load()
    login_page.fill_username('standard_user')
    login_page.fill_password('secret_sauce')
    login_page.click_login()