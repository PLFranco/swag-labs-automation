from pages.login import SwagLabsLoginPage
from playwright.sync_api import expect, Page


def test_invalid_username(page: Page, login_page: SwagLabsLoginPage) -> None:
    login_page.load()
    login_page.fill_username('locked_out_user')
    login_page.fill_password('secret_sauce')
    login_page.click_login()

    