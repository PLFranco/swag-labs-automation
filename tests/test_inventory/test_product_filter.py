from pages.products import SwagLabsProductListings
from playwright.sync_api import expect, Page

def test_alphabetical_sort_az(login_user, page: Page) -> None:
    product = SwagLabsProductListings(page)

    product.get_option('az')
    product.load_state()
    product_names_az = product.get_product_names()

    sorted_names_az = sorted(product_names_az)
    assert product_names_az == sorted_names_az

def test_alphabetical_sort_za(login_user, page: Page) -> None:
    product = SwagLabsProductListings(page)

    product.get_option('za')
    product.load_state()
    product_names_za = product.get_product_names()

    sorted_names_za = sorted(product_names_za, reverse=True)
    assert product_names_za == sorted_names_za





