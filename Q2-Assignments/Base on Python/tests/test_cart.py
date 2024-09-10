import pytest
from selenium import webdriver
# from pages.cart_page import CartPage
from pages.cart_page import CartPage

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.othoba.com/cart")
    yield driver
    driver.quit()

def test_view_cart(setup):
    cart_page = CartPage(setup)
    # Add assertions to validate cart content
