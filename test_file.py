from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

class TestFile(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.tui.se/")
        self.driver.maximize_window()
        self.cookies = self.driver.find_element(
            By.NAME, "Close consent Widget").click()

    def test_load_site(self):
        # Test that TUI is part of the URL
        self.assertIn("tui", self.driver.current_url)

    def test_dropdown(self):
        # Find "Resor" dropdown
        self.resor = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/header/div/div/section/div/ul/li[1]/div/a/span[1]")
        # Loops through all the options in the dropdown
        options = self.resor.find_elements(By.XPATH, ".//option")

        item_to_check = "Charterresor"
        item_found = False
        for option in options:
            if option.text == item_to_check:
                item_found = True
                break

        self.assertTrue(
            item_found, f"{item_to_check} is not present in the dropdown menu.")
        
# chrome_options = Options()
#         chrome_options.add_argument("--incognito")
#self.driver = webdriver.Chrome(options = chrome_options)