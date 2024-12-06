from playwright.sync_api import Page

class SwagLabsLoginPage:
    URL = 'https://www.saucedemo.com/v1/index.html'

    def __init__(self, page: Page) -> None:
        self.page = page
        self.username = page.locator('[data-test=\"username\"]')
        self.password = page.locator('[data-test=\"password\"]')
        self.login_button = page.locator("#login-button")
    
    def load(self) -> None:
        self.page.goto(self.URL)

    def fill_username(self, username: str) -> None:
        self.username.fill(username)
    
    def fill_password(self, password: str) -> None:
        self.password.fill(password)
    
    def click_login(self) -> None:
        self.login_button.click()