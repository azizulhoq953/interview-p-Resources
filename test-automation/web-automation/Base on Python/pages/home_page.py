from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, 'search')
        self.cart_link = (By.ID, 'cart')
        self.profile_link = (By.ID, 'profile')

    def enter_search_query(self, query):
        self.driver.find_element(*self.search_box).send_keys(query)

    def click_cart(self):
        self.driver.find_element(*self.cart_link).click()

    def click_profile(self):
        self.driver.find_element(*self.profile_link).click()
