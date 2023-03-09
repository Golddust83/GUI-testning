from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
import time

class TestFile(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.tui.se/")
        self.driver.maximize_window()
        # Including explicit wait
        WebDriverWait(self.driver, 10).until(lambda d: d.find_element(By.ID, "cmCloseBanner"))
        self.cookies = self.driver.find_element(
            By.ID, "cmCloseBanner").click()

    def test_load_site(self):
        # Test that TUI is part of the URL
        self.assertIn("tui", self.driver.current_url)

    # def test_dropdown(self):
    #     # Find "Resor" dropdown
    #     self.resor = self.driver.find_element(
    #         By.XPATH, "/html/body/div[1]/div/header/div/div/section/div/ul/li[1]/div/a/span[1]")
    #     # Loops through all the options in the dropdown
    #     options = self.resor.find_elements(By.XPATH, ".//option")

    #     item_to_check = "Charterresor"
    #     item_found = False
    #     for option in options:
    #         print(option)
    #         if option.text == item_to_check:
    #             item_found = True
    #             break

    #     self.assertTrue(
    #         item_found, f"{item_to_check} is not present in the dropdown menu.")

    def test_single_product_page(self):
        # Find "Resmål" dropdown
        self.resmål = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/header/div/div/section/div/ul/li[6]/div/a/span[1]").click()
        # Find Tanzania
        self.Tanzania = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/section/div[4]/div/div[2]/div/ul/div/div[43]/li/a/div/div/div[2]").click()
        # Find "Visa alla hotell"
        self.show_all_hotels = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/section/div[2]/div/div/div/a/button").click()
        # Find "Reef & Beach Resort" on product page
        self.hotel_Tanzania = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/section/div[2]/div/div/h1/span")
        self.assertTrue(self.hotel_Tanzania.is_displayed(), "Product not found under header.")

    def test_chat(self):
        """
        Hittat på ett nytt test eftersom man testar både adding to cart, cart page och checkout page samtidigt 
        = blir för få test
        """
        # Find "Kundservice" link
        self.customer_service = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/header/div/div/div/div/div/ul/li[2]/span/a").click()
        # Find chat
        # self.chat = WebDriverWait(self.driver, 20).until(lambda d: d.find_element(By.XPATH, "/html/body/div[5]/button"))
        self.chat = WebDriverWait(self.driver, 20).until(element_to_be_clickable((By.XPATH, "/html/body/div[5]/button"))) # Utforska mer!!
        self.chat.click()
        # = self.driver.find_element(
        #By.XPATH, "/html/body/div[5]/button").click()
        # Find input field to answer chatbot
        print("hej")
        self.input_field = WebDriverWait(self.driver, 20).until(lambda d: d.find_element(By.XPATH, "/html/body/div[1]/div/div/form/div/input"))
        print("hej2")
        
        #self.input_field.click()
        # self.input_field = self.driver.find_element(
        #     By.XPATH, "/html/body/div[1]/div/div/form/div/input")
        # # Click input field
        # self.input_field.click()
        # Clear text
        time.sleep()
        self.input_field.clear()
        # Input your name
        
        self.input_field.send_keys("Nina Persson" + Keys.RETURN)
        print("hej3")
        # Find "Jag har en fråga" button and make an assertion that it is there
        self.button = self.driver.find_element(By.NAME, "Jag har en fråga")
        self.assertEqual("Jag har en fråga", self.button.text)
        
# chrome_options = Options()
#         chrome_options.add_argument("--incognito")
#self.driver = webdriver.Chrome(options = chrome_options)

#<button id="cmCloseBanner" class="button raised blue" aria-label="Close consent Widget" data-di-id="#cmCloseBanner">Godkänn</button>