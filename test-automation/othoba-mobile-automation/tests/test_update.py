import pytest
# from config.capabilities import get_capabilities
from config.capabilities import get_capabilities

class TestUpdateProduct:
    def setup_method(self):
        self.driver = get_capabilities()

    def teardown_method(self):
        self.driver.quit()

    def test_update_product(self):
        # Log into the application
        login_button = self.driver.find_element_by_id("com.othoba.android:id/login_button")
        login_button.click()

        username_field = self.driver.find_element_by_id("com.othoba.android:id/username")
        password_field = self.driver.find_element_by_id("com.othoba.android:id/password")
        username_field.send_keys("01706257588")
        password_field.send_keys("Othoba4Beats@")

        submit_button = self.driver.find_element_by_id("com.othoba.android:id/login_submit")
        submit_button.click()

        # Navigate to products section
        products_button = self.driver.find_element_by_id("com.othoba.android:id/products")
        products_button.click()

        # Select the product to update
        product_item = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Test Product']")
        product_item.click()

        # Edit product details
        edit_button = self.driver.find_element_by_id("com.othoba.android:id/edit_product")
        edit_button.click()

        # Update product price
        product_price = self.driver.find_element_by_id("com.othoba.android:id/product_price")
        product_price.clear()
        product_price.send_keys("150")

        # Save the updated product
        save_button = self.driver.find_element_by_id("com.othoba.android:id/save_product")
        save_button.click()

        # Assert the product update success
        success_message = self.driver.find_element_by_id("com.othoba.android:id/success_message")
        assert success_message.text == "Product updated successfully"
