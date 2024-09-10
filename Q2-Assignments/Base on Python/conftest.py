import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setup():
    options = Options()
    options.add_argument('--headless')  # Run headless Chrome
    options.binary_location = '/usr/bin/google-chrome'  # Update with correct path if needed

    # Use webdriver_manager to handle driver version and path
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.othoba.com")
    yield driver
    driver.quit()
