import pytest
# from config.capabilities import get_capabilities
from config.capabilities import get_capabilities

class TestDeleteProduct:
    def setup_method(self):
        self.driver = get_capabilities()

    def teardown_method(self):
        self.driver.quit()

    def test_delete_product(self):
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

        # Select the product to delete
        product_item = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Test Product']")
        product_item.click()

        # Delete the product
        delete_button = self.driver.find_element_by_id("com.othoba.android:id/delete_product")
        delete_button.click()

        # Confirm the deletion
        confirm_button = self.driver.find_element_by_id("com.othoba.android:id/confirm_delete")
        confirm_button.click()

        # Assert the product deletion success
        success_message = self.driver.find_element_by_id("com.othoba.android:id/success_message")
        assert success_message.text == "Product deleted successfully"
