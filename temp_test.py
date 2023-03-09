
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time


driver = webdriver.Chrome()
driver.get("https://www.tui.se/")
driver.maximize_window()
# Including explicit wait
WebDriverWait(driver, 10).until(lambda d: d.find_element(By.ID, "cmCloseBanner"))
cookies = driver.find_element(
    By.ID, "cmCloseBanner").click()

# Find "Resor" dropdown
resor = driver.find_element(
    By.XPATH, "/html/body/div[1]/div/header/div/div/section/div/ul/li[1]/div/a/span[1]")

# Loops through all the options in the dropdown
options = resor.find_elements(By.XPATH, ".//option")


item_to_check = "Charterresor"
item_found = False
print("hej")
for option in options:
    print("hej2")
    print(option.text)
    if option.text == item_to_check:
        item_found = True
        break