import pytest
# from selenium import webdriver
from selenium import webdriver
# from pages.product_page import ProductPage
from pages.product_page import ProductPage

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.othoba.com/product")
    yield driver
    driver.quit()

def test_view_product_details(setup):
    product_page = ProductPage(setup)
    # Add assertions to validate product details
