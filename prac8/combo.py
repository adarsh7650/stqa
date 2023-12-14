from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("http://127.0.0.1:5501/prac8/one.html")

select = driver.find_element(By.ID , "mycombobox")

combobox = select.find_elements(By.TAG_NAME , "option")

for c in combobox:
    print(c.get_attribute("value"))