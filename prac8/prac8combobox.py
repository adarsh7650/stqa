from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("http://127.0.0.1:5501/prac8/one.html")

select = driver.find_element(By.ID , "mycombobox")
options  = select.find_elements(By.TAG_NAME , "option")

for o in options:
    print(o.get_attribute("value"))
