# Filename: test_products.py

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy # type: ignore
from appium.webdriver.common.touch_action import TouchAction # type: ignore
import unittest

class TestProductModule(unittest.TestCase):
    
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'appPackage': 'com.othoba',
            'appActivity': '.MainActivity',
            'automationName': 'UiAutomator2',
            'noReset': True,  # Prevent resetting app state between tests
            'fullContextList': True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    
    def test_create_product(self):
        driver = self.driver
        # Navigate to Products and add product
        driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Add Product').click()
        driver.find_element(MobileBy.ID, 'com.othoba:id/product_name').send_keys('Test Product')
        driver.find_element(MobileBy.ID, 'com.othoba:id/product_price').send_keys('100')
        driver.find_element(MobileBy.ID, 'com.othoba:id/save_button').click()
        
        # Verify product is added
        # Adjust selector or method to correctly locate and validate the added product
        product_list_elements = driver.find_elements(MobileBy.ID, 'com.othoba:id/product_list')
        product_names = [element.text for element in product_list_elements]
        self.assertIn('Test Product', product_names)
    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
