import pytest
# from selenium import webdriver
from selenium import webdriver
# from pages.product_page import ProductPage
from pages.product_page import ProductPage
# from pages.cart_page import CartPage
from pages.cart_page import CartPage

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.othoba.com")
    yield driver
    driver.quit()

def test_add_to_cart(setup):
    product_page = ProductPage(setup)
    cart_page = CartPage(setup)

    product_page.click_add_to_cart()
    cart_page.click_checkout()
    # Add assertions to validate the checkout process
