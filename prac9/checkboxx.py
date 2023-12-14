from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("http://127.0.0.1:5501/prac9/one.html")

checkbox = driver.find_elements(By.XPATH ,"/html/body/input[@type='checkbox']")

checked = 0
unchecked = 0
for c in checkbox:
    if c.is_selected():
        checked += 1
    else:
        unchecked +=1
print(len(checkbox))
print(checked)
print(unchecked)