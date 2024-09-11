from selenium.webdriver.common.by import By

class ProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.edit_profile_button = (By.ID, 'editProfile')
        self.logout_button = (By.ID, 'logout')

    def click_edit_profile(self):
        self.driver.find_element(*self.edit_profile_button).click()

    def click_logout(self):
        self.driver.find_element(*self.logout_button).click()
