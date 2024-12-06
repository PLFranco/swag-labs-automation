from pages.login import SwagLabsLoginPage
from pages.products import SwagLabsProductListings
from playwright.sync_api import expect, Page

def test_product_list_loads_correctly(login_user, page: Page) -> None:

    products = SwagLabsProductListings(page)
    products.verify_inventory_list()


def test_each_product_details(login_user, page: Page) -> None:

    products = SwagLabsProductListings(page)
    products.verify_inventory_list()
    products.verify_all_product_details()


def test_product_count_is_correct(login_user, page: Page) -> None:

    products = SwagLabsProductListings(page)
    products.verify_inventory_list()
    products.verify_product_count()


