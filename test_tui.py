from unittest import TestCase
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

    # Helper for waiting explicitly
    def document_initialised(self.driver):
        return self.driver.execute_script("return initialised")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.tui.se/")
        self.driver.maximize_window()    

    def test_load_site(self):
        # Test that TUI is part of the URL
        self.assertIn("tui", self.driver.current_url) # Måste man definiera current_url nånstans eller fattar Python det själv? (Kolla Eriks inspelningar igen!)

    def test_main_shop_page(self):
        # Load Selenium Webdriver # Måste man ladda Selenium Webdriver i vartenda test eller räcker det att anropa en metod som gör det?
        self.driver = webdriver.Chrome()
        self.driver.get(pageURL)

        # Find Products page link
        products_link = self.driver.find_element_by_XPATH, "Products")

        # Click on products page link
        products_link.click()

        # Including explicit wait
        scar_original = WebDriverWait(self.driver, timeout = 10).until(lambda d: d.find_element_by_XPATH, "/html/body/div/main/section/div/main/a[1]/div/div[2]/h2"))

        # Test that the text contains "Scar Original"
        self.assertIn(a, b)

            # Test that URL now contains .......
        

    def test_single_product_page(self):

        # Load Selenium Webdriver

        # Enter "Avreseort"

        #  Enter "Resmål", datum

        # Test that the product text contains "XXXX"
        
        # Test that URL now contains .......



    def test_adding_product_to_cart(self):
         
        # Load Selenium Webdriver
         
        # Enter "Avreseort"
        avreseort = driver.find_element(By.XPATH, /html/body/div[1]/div/section/section[1]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div/div[2]/div/input)
        # Enter "Resmål"
            
        # Enter date

        # Enter length

        # Enter quantity



    
    def test_cart_page(self):


    def test_checkout_page(self):
    

    def tearDown(self):
        self.driver.delete_all_cookies()     
        self.driver.quit()  

if __name__ == '__main__':
    unittest.main()