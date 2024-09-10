from selenium.webdriver.common.by import By

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_results = (By.CSS_SELECTOR, '.search-results')

    def get_search_results(self):
        return self.driver.find_elements(*self.search_results)
