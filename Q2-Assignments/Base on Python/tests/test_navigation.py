import pytest
# from selenium import webdriver
from selenium import webdriver
# from pages.home_page import HomePage
from pages.home_page import HomePage

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.othoba.com")
    yield driver
    driver.quit()

def test_navigation(setup):
    home_page = HomePage(setup)
    home_page.click_cart()
    # Add assertions to validate navigation
