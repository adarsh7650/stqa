from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Edge()
driver.get("https://google.com")

wait = WebDriverWait(driver , 1000)
elements = wait.until(ec.presence_of_all_elements_located((By.XPATH , '//*')))

web_page_elements = set()

for e in elements:
    web_page_elements.add(e.tag_name)
print(web_page_elements
      )
print(len(web_page_elements))