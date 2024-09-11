from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.payment_method_dropdown = (By.ID, 'paymentMethod')
        self.confirm_order_button = (By.ID, 'confirmOrder')

    def select_payment_method(self, method):
        self.driver.find_element(*self.payment_method_dropdown).send_keys(method)

    def click_confirm_order(self):
        self.driver.find_element(*self.confirm_order_button).click()
