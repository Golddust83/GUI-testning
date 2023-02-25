from unittest import TestCase, main
from unittest.mock import patch
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

class TestTUI(TestCase):
    """
    Things to test in this class:
    
    # The main shop page loads
    # A single product page loads
    # A customer can add a product to their cart
    # The cart page loads
    # A customer can reach the checkout page
    """

    # Helper for waiting explicitly     Kolla vad som krävs för explicit waits i Unittest!!
    def document_initialised(self):
        return self.driver.execute_script("return initialised")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.tui.se/")
        self.driver.maximize_window()    

    def test_load_site(self):
        # Test that TUI is part of the URL
        self.assertIn("tui", self.driver.current_url) # Måste man definiera current_url nånstans eller fattar Python det själv? (Kolla Eriks inspelningar igen!)

    def test_main_shop_page(self):
        # Find Products page link
        products_link = self.driver.find_element_by_XPATH, "Products")

        # Click on products page link
        products_link.click()

        # Including explicit wait
        scar_original = WebDriverWait(self.driver, timeout = 10).until(lambda d: d.find_element_by_XPATH, "/html/body/div/main/section/div/main/a[1]/div/div[2]/h2")

        # Test the dropdown "Resor" and verify that it contains a title "Charterresor"
        self.assertIn(a, b)

        # Test that URL now contains "charter"
        self.assertIn("charter", self.driver.current_url)
        

    def test_single_product_page(self):

       

        # Enter "Avreseort"

        #  Enter "Resmål", datum

        #  Test the Resmål/Kroatien/Makarska-rivieran/Visa mer/TUI Blue Jadran



    def test_adding_product_to_cart(self):
         
                 
        # Enter "Avreseort"
        self.avreseort = self.driver.find_element_by_XPATH("/html/body/div[1]/div/section/section[1]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div/div[2]/div/input")
        # Enter "Resmål"
            
        # Enter date
        # Lördag 6 maj, +/- 14 dagar -> Klar

        # Enter length

        # Enter quantity, 1 person

        # Klicka sök

        # Klicka på grönt datum

        # Klicka på Fortsätt

        # Klicka på Boka
    
        # Verify that you are now in checkout page
        self.assertIn("payment", self.driver.current_url)

    def test_chat(self): # Hittat på ett annat test eftersom man testar både adding to cart, cart page och checkout page samtidigt
        # Find Kundservice link
        self.customer_service = self.driver.find_element_by_XPATH("/html/body/div[1]/div/header/div/div/div/div/div/ul/li[2]/span/a")
        # Click the link
        self.customer_service.click()
        # Find chat
        self.chat = self.driver.find_element_by_XPATH("/html/body/div[4]/button/span")
        # Click chat
        self.chat.click()
        # Find input field to answer chatbot
        self.input_field = self.driver.find_element_by_XPATH("/html/body/div[1]/div/div/form/div/input")
        # Clear text
        self.input_field.clear()
        # Input your name
        self.input_field.send_keys("Nina Persson")
        # Find Skicka-button
        self.send = self.driver.find_element_by_XPATH("/html/body/div[1]/div/div/form/button")
        # Click button
        self.send.click()
        # Find "Jag har en fråga" button and make an assertion that it is there
        self.button = self.driver.find_element_by_NAME("Jag har en fråga") 
        self.assertIsNotNone(self.button)

    def tearDown(self):
        self.driver.delete_all_cookies()     
        self.driver.quit()  

    if __name__ == '__main__':
        main()