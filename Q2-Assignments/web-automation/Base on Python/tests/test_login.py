import pytest
# from selenium import webdriver
from selenium import webdriver
# from pages.login_page import LoginPage
from pages.login_page import LoginPage
# from pages.home_page import HomePage
from pages.home_page import HomePage

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.othoba.com/login")
    yield driver
    driver.quit()

def test_login_success(setup):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)

    login_page.enter_username('01706257588')
    login_page.enter_password('Othoba4Beats@')
    login_page.click_login()

    assert "Home" in setup.title
