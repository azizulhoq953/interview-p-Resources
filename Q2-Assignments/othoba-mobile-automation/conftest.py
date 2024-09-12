import pytest
import os
import sys
from appium import webdriver

# Adding the root directory to sys.path so that the config module can be found
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the get_capabilities function from the config module
from config.capabilities import get_capabilities

@pytest.fixture(scope="session")
def appium_driver():
    """Fixture to initialize the Appium driver before tests and quit after tests."""
    # Get the desired capabilities for the Appium session
    desired_caps = get_capabilities()

    # Check if desired_caps is None or not a dictionary
    if not desired_caps:
        raise ValueError("Desired capabilities are not defined. Please check get_capabilities().")
    
    # Create a new Appium driver session
    driver = webdriver.Remote("http://127.0.0.1:4725/wd/hub", desired_caps)

    # Return the driver object to the test functions
    yield driver

    # Quit the driver after the tests
    driver.quit()

@pytest.fixture(scope="session", autouse=True)
def setup_environment():
    """Fixture to set up any environment variables or configurations globally."""
    # Export PYTHONPATH to ensure config module is found
    os.environ['PYTHONPATH'] = os.path.dirname(os.path.abspath(__file__))
