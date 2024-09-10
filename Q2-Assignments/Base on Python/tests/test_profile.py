import pytest
# from selenium import webdriver
from selenium import webdriver
# from pages.profile_page import ProfilePage
from pages.profile_page import ProfilePage

@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run headless Chrome
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.othoba.com/profile")
    yield driver
    driver.quit()

def test_edit_profile(setup):
    profile_page = ProfilePage(setup)
    profile_page.click_edit_profile()
    # Add assertions to validate profile editing
