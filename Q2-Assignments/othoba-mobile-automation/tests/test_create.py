import pytest

class TestCreateProduct:
    @pytest.fixture(autouse=True)
    def setup_method(self, appium_driver):
        """Initialize driver before each test method and quit after each test method."""
        self.driver = appium_driver

    def teardown_method(self):
        self.driver.quit()

    def test_create_product(self):
        # Find and click the login button
        login_button = self.driver.find_element_by_id("com.othoba.android:id/login_button")
        login_button.click()

        # Enter username and password
        username_field = self.driver.find_element_by_id("com.othoba.android:id/username")
        password_field = self.driver.find_element_by_id("com.othoba.android:id/password")
        username_field.send_keys("01706257588")
        password_field.send_keys("Othoba4Beats@")

        # Submit login
        submit_button = self.driver.find_element_by_id("com.othoba.android:id/login_submit")
        submit_button.click()

        # Navigate to products section and click on Add Product
        add_product_button = self.driver.find_element_by_id("com.othoba.android:id/add_product")
        add_product_button.click()

        # Fill product details
        product_name = self.driver.find_element_by_id("com.othoba.android:id/product_name")
        product_price = self.driver.find_element_by_id("com.othoba.android:id/product_price")
        product_name.send_keys("Test Product")
        product_price.send_keys("100")

        # Submit the product creation form
        save_button = self.driver.find_element_by_id("com.othoba.android:id/save_product")
        save_button.click()

        # Assert that product creation is successful
        success_message = self.driver.find_element_by_id("com.othoba.android:id/success_message")
        assert success_message.text == "Product added successfully"
