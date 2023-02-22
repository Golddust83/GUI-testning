from unittest import TestCase
from unittest.mock import patch
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from helpers import Helpers
from page_objects import PageObjects

class TestTUI(TestCase):
    """
    Things to test in this class:
    
    # The main shop page loads
    # A single product page loads
    # A customer can add a product to their cart
    # The cart page loads
    # A customer can reach the checkout page
    """

    @unittest.fixture(scope = class)

    # def setUp(self):
    #     self.driver = webdriver.Chrome()
    #     driver.maximize_window()

    # def tearDown(self):
    #     self.addCleanup(self.browser.quit)
    #     driver.delete_all_cookies()

    # Setup and Teardown for every class
    def load_driver(self):

            # Selenium 4.6 and above use a BETA version of Selenium Manager which automatically handles the browser drivers
            # If we have an older version, or if Selenium Managers somehow does not work on your system, follow this guide for installing the correct driver:
            # https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/

            driver = webdriver.Chrome()
            yield driver
            print("RUN CLASS TEARDOWN")
            driver.quit()

    # Setup and Teardown for every single test
    @unittest.fixture
    def get_TUI_site(self, load_driver):
        driver = load_driver
        # Load TUI website
        driver.get(pageURL)
        yield driver
        print("RUN TEST TEARDOWN")
        driver.delete_all_cookies()


    def test_load_site(self, pageURL):
        driver.get(pageURL)
        # Test that TUI is part of the URL
        self.assert("tui" in driver.current_url)

    def test_main_shop_page(self, get_iceberry_site):
        # Load Selenium Webdriver
        driver.get(pageURL)

        # Find Products page link
        products_link = driver.find_element(By.LINK_TEXT, "Products")

        # Click on products page link
        products_link.click()

        # Including explicit wait
        scar_original = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, "/html/body/div/main/section/div/main/a[1]/div/div[2]/h2"))

        # Test that the text contains "Scar Original"
        self.assertIn("Scar Original" in scar_original.text)

        # Test that URL now contains .......
        boolean_assert("products" in driver.current_url, f"Expected products in url, got: {driver.current_url}")

    def test_single_product_page():

        # Load Selenium Webdriver

        # Enter "Avreseort"

        #  Enter "Resmål", datum

        # Test that the product text contains "XXXX"
        
        # Test that URL now contains .......



    def test_adding_product_to_cart():
         
        # Load Selenium Webdriver
         
        # Enter "Avreseort"
        avreseort = driver.find_element(By.XPATH, /html/body/div[1]/div/section/section[1]/div/div/div/div/div[2]/div[1]/div/div/div[1]/div/div[2]/div/input)
        # Enter "Resmål"
            
        # Enter date

        # Enter length

        # Enter quantity



    
    def test_cart_page():


    def test_checkout_page():
    






# Eriks advanced



    def test_advanced_1(self, get_iceberry_site):
        # Load Selenium webdriver
        driver = get_iceberry_site

        # Test that iceberry is part of the url
        boolean_assert("iceberry" in driver.current_url, f"Expected iceberry in url, got: {driver.current_url}")


    def test_advanced_2(self, get_iceberry_site):
        # Load Selenium webdriver
        driver = get_iceberry_site

        # Find products page link
        products_link = driver.find_element(By.LINK_TEXT, "Products")

        # Click on products page link
        products_link.click()

        # Including explicit wait
        # WARNING: This does not work together with implicit wait
        scar_original = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH, "/html/body/div/main/section/div/main/a[1]/div/div[2]/h2"))

        print('Scar Original'== scar_original.text)
        # Test that the text contains "Scar Original"
        boolean_assert("Scar Original" in scar_original.text, f"Expected Scar Original in text for first product, got: {scar_original.text}")

        # Test that url now contains products
        boolean_assert("products" in driver.current_url, f"Expected products in url, got: {driver.current_url}")


    



# För att aktivera venv: Sökväg: venv\Scripts\activate

if __name__ == '__main__':
    unittest.main()