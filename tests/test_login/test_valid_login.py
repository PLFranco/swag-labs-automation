from pages.login import SwagLabsLoginPage
from playwright.sync_api import expect, Page

def test_valid_login(page: Page, login_page: SwagLabsLoginPage) -> None:
   
    #Given the Swaglabs homepage is displayed
    login_page.load()

    #User enters a valid username
    login_page.fill_username('standard_user')

    #User enters a valid password
    login_page.fill_password('secret_sauce')

    #The user clicks the Login button
    login_page.click_login()

    #Then the user is navigated to the Products Page
    expect(page.locator('div.product_label')).to_have_text('Products')



 