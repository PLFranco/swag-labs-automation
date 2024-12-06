from pages.login import SwagLabsLoginPage
from playwright.sync_api import expect, Page


def test_invalid_username(page: Page, login_page: SwagLabsLoginPage) -> None:
    login_page.load()
    login_page.fill_username()
    login_page.fill_password()
    login_page.click_login()

def test_invalid_password(page: Page, login_page: SwagLabsLoginPage) -> None:
    login_page.load()
    login_page.fill_username()
    login_page.fill_password()
    login_page.click_login()

def test_invalid_username_and_password(page: Page, login_page: SwagLabsLoginPage) -> None:
    login_page.load()
    login_page.fill_username()
    login_page.fill_password()
    login_page.click_login()

def test_blank_username_and_password(page: Page, login_page: SwagLabsLoginPage) -> None:
    login_page.load()
    login_page.fill_username()
    login_page.fill_password()
    login_page.click_login()




