from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.common.alert


class TestTUI(TestCase):
    """
    Things to test in this class:

    # The main shop page loads
    # A single product page loads
    # A customer can add a product to their cart
    # The cart page loads
    # A customer can reach the checkout page
    # Customer service page - chat
    """

    # Including explicit wait
    # WebDriverWait(self.driver, 10).until(expected_conditions.alert_is_present("element"))

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.tui.se/")
        self.driver.maximize_window()
        self.accept_next_alert = True

    def test_load_site(self):
        self.alert = self.driver.switch_to_alert()
        self.alert.accept()
        # Find "Spara och stäng"
        self.save = self.driver.find_element(
            By.XPATH, "/html/body/div[26]/div[2]/div[2]/button[1]/div")
        # Click "Spara och stäng"
        self.save.click()
        # Test that TUI is part of the URL
        # Måste man definiera current_url nånstans eller fattar Python det själv? (Kolla Eriks inspelningar igen!)
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

    def test_main_shop_page(self):
        # Find "Resor" dropdown
        self.resor = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/header/div/div/section/div/ul/li[1]/div/a/span[1]")
        # Create an instance of ActionChains and pass in the driver
        self.action_chains = ActionChains(self.driver)
        # Move the mouse to hover over the element
        self.action_chains.move_to_element(self.resor).perform()
        # Find "Hotell" in dropdown
        self.hotell = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/header/div/div/section/div/ul/li[1]/div[1]/section/div/div/div/div[2]/section/div/div/ul/li[3]/a")
        # Create an instance of ActionChains and pass in the driver
        self.action_chains = ActionChains(self.driver)
        # Move the mouse to hover over the element
        self.action_chains.move_to_element(self.hotell).perform()
        # Find "Swim up" link
        self.swim_up = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/header/div/div/section/div/ul/li[1]/div/section/div/div/div/div[3]/ul[1]/ul[2]/li[1]/a")
        # Click "Swim up"
        self.swim_up.click()
        # Test that URL now contains "swim-up"
        self.assertIn("swim-up", self.driver.current_url)

    def test_single_product_page(self):
        # Find "Resmål" dropdown
        self.resmål = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/header/div/div/section/div/ul/li[6]/div/a/span[1]")
        # Click "Resmål"
        self.resmål.click()
        # Find Tanzania
        self.Tanzania = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/section/div[4]/div/div[2]/div/ul/div/div[43]/li/a/div/div/div[2]")
        # Click Tanzania
        self.Tanzania.click()
        # Find "Visa alla hotell"
        self.show_all_hotels = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/section/div[2]/div/div/div/a/button")
        # Click "Visa alla hotell"
        self.show_all_hotels.click()
        # Find "Reef & Beach Resort" on product page
        self.hotel_Tanzania = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/section/div[2]/div/div/h1/span")
        product_element = self.hotel_Tanzania.find_element(
            By.XPATH, "/html/body/div[1]/div/section/div[5]/div/div/div/div[1]/section[4]/div/div[1]/div[2]/h3/a/span")
        print(product_element.text)
        self.assertTrue(product_element.is_displayed(), "Product not found under header.")

    # def test_adding_product_to_cart(self):
    #     """
    #     Only a mock test (not tested or only tested once) to test the cart page since I don't 
    #     want to be banned from the TUI homepage because I'm booking too many trips 
    #     without any intention of using them.
    #     """
    #     # Find "Avreseort"
    #     self.avreseort = self.driver.find_element(
    #         By.XPATH, "/html/body/div[1]/div/section/section[1]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div/div[2]/div/input")
    #     # Click "Avreseort"
    #     self.avreseort.click()
    #     # Find "Köpenhamns flygplats" checkbox
    #     self.CPH_checkbox = self.driver.find_element(
    #         By.XPATH, "/html/body/div[18]/section/div/div/div/section/div/div/div/div/div[2]/div[2]/ul/li[5]/label/span[1]/svg")
    #     #  Click "Köpenhamns flygplats"
    #     self.CPH_checkbox.click()
    #     # Find "Klar"
    #     self.klar_avreseort = self.driver.find_element(
    #         By.XPATH, "/html/body/div[18]/section/div/div/div/footer/div/div/span/button")
    #     # Click "Klar"
    #     self.klar_avreseort.click()
    #     # Find list of available countries
    #     self.countries = self.driver.find_element(
    #         By.XPATH, "/html/body/div[1]/div/section/section[1]/div/div/div/div/div[2]/div[1]/div/div/div[2]/div[1]/div/span[1]/span/span")
    #     # Click list
    #     self.countries.click()
    #     # Find clear button
    #     self.rensa_countries = self.driver.find_element(
    #         By.XPATH, "/html/body/div[19]/section/div/div/div/footer/div/div/a")
    #     # Click "Rensa"
    #     self.rensa_countries.click()
    #     # Find Jamaica
    #     self.Jamaica = self.driver.find_element(
    #         By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[1]/div/div/div/ul/li[18]/a")
    #     # Click Jamaica
    #     self.Jamaica.click()
    #     # Find the "Jamaica (Alla)" checkbox
    #     self.Jamaica_all_checkbox = self.driver.find_element(
    #         By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/div/div/div/div/div/div/span")
    #     # Find "Klar"
    #     self.klar_countries = self.driver.find_element(
    #         By.XPATH, "/html/body/div[3]/div/div/div[3]/div[2]/a")
    #     # Click "Klar"
    #     self.klar_countries.click()
    #     # Use the default values in "När"

    #     # Find "Sök"
    #     self.sök = self.driver.find_element(
    #         By.XPATH, "/html/body/div[1]/div/section/section[1]/div/div/div/div/div[2]/div[1]/div/div/div[6]/button")
    #     # Click "Sök"
    #     self.sök.click()

    #     # Verify that you are now in checkout page
    #     self.assertIn("payment", self.driver.current_url)

    def test_chat(self):
        """
        Hittat på ett nytt test eftersom man testar både adding to cart, cart page och checkout page samtidigt 
        = blir för få test
        """
        # Find "Kundservice" link
        self.customer_service = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/header/div/div/div/div/div/ul/li[2]/span/a")
        # Click the link
        self.customer_service.click()
        # Find chat
        self.chat = self.driver.find_element(
            By.XPATH, "/html/body/div[4]/button/span")
        # Click chat
        self.chat.click()
        # Find input field to answer chatbot
        self.input_field = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div/form/div/input")
        # Click input field
        self.input_field.click()
        # Clear text
        self.input_field.clear()
        # Input your name
        self.input_field.send_keys("Nina Persson" + Keys.RETURN)
        # Find "Jag har en fråga" button and make an assertion that it is there
        self.button = self.driver.find_element(By.NAME, "Jag har en fråga")
        self.assertEqual(self.button.text, "Jag har en fråga")

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.quit()

    if __name__ == "__main__":
        main()
