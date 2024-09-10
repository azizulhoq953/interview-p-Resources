import pytest
# from selenium import webdriver
from selenium import webdriver
# from pages.cart_page import CartPage
from pages.cart_page import CartPage
# from pages.checkout_page import CheckoutPage
from pages.checkout_page import CheckoutPage

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.othoba.com/cart")
    yield driver
    driver.quit()

def test_checkout(setup):
    checkout_page = CheckoutPage(setup)

    checkout_page.select_payment_method('Credit Card')
    checkout_page.click_confirm_order()
    # Add assertions to validate the checkout process
