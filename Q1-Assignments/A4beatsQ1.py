from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
from datetime import datetime
import time
service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://www.google.com")
    search_bar = driver.find_element(By.NAME, "q")
    
    time.sleep(15) 
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul[role='listbox']")))
    suggestions_container = driver.find_element(By.CSS_SELECTOR, "ul[role='listbox']")
    suggestions = suggestions_container.find_elements(By.CSS_SELECTOR, "li[role='option']")
    keywords = [driver.execute_script("return arguments[0].innerText;", suggestion).strip() for suggestion in suggestions]
    if not keywords:
        raise ValueError("No suggestions found")
    
    largest_keyword = max(keywords, key=len)
    smallest_keyword = min(keywords, key=len)

    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Keywords"
    sheet.append(["Largest Keyword", largest_keyword])
    sheet.append(["Smallest Keyword", smallest_keyword])
    current_day = datetime.now().strftime("%A")
    workbook.save(f"{current_day}.xlsx")

finally:
    driver.quit()
