import pytest
# from selenium import webdriver
from selenium import webdriver
# from pages.home_page import HomePage
from pages.home_page import HomePage
# from pages.search_page import SearchPage
from pages.search_page import SearchPage

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.othoba.com")
    yield driver
    driver.quit()

def test_search(setup):
    home_page = HomePage(setup)
    search_page = SearchPage(setup)

    home_page.enter_search_query('product')
    results = search_page.get_search_results()

    assert len(results) > 0
