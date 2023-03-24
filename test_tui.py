from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestTUI(TestCase):
    """
    Things to test in this class:

    # Product can be found in dropdown
    # The main shop page loads
    # A single product page loads
    # Customer service page - chat
    """

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.tui.se/")
        self.driver.maximize_window()
        # Including explicit wait to be able to close cookie alert
        WebDriverWait(self.driver, 10).until(lambda d: d.find_element(By.ID, "cmCloseBanner"))
        self.cookies = self.driver.find_element(
            By.ID, "cmCloseBanner").click()
        
    def test_load_site(self):
        """
        Testing that TUI is part of the URL
        """
        self.assertIn("tui", self.driver.current_url)

    def test_dropdown(self):
        """
        Testing that "Charterresor" is present in the "Resor" dropdown 
        """
        # Find "Resor" dropdown
        self.resor = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((
            By.XPATH, "/html/body/div[1]/div/header/div/div/section/div/ul/li[1]/div[1]/a"))).click()
        # Create an instance of ActionChains and pass in the driver
        self.action_chains = ActionChains(self.driver)
        # Move the mouse to hover over the element
        self.action_chains.move_to_element(self.resor).perform()
        # Find "Charterresor" in dropdown
        self.charterresor = self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/header/div/div/section/div/ul/li[1]/div[1]/section/div/div/div/div[2]/section/div/div/ul/li[2]/a").click()
        # Test that URL now contains "charter"
        self.assertTrue(
            "charter" in self.driver.current_url, f"{self.charterresor} is not present in the dropdown menu.")

    def test_main_shop_page(self):
        """
        Testing that "Swim up" hotel product exist 
        """
        # Find "Resor" dropdown
        self.resor = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((
            By.XPATH, "/html/body/div[1]/div/header/div/div/section/div/ul/li[1]/div/a/span[1]")))
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
            By.XPATH, "/html/body/div[1]/div/header/div/div/section/div/ul/li[1]/div/section/div/div/div/div[3]/ul[1]/ul[2]/li[1]/a").click()
        # Test that URL now contains "swim-up"
        self.assertIn("swim-up", self.driver.current_url)

    def test_single_product_page(self):
        """
        Testing that explicit product exist on product page
        """
        # Find "Resmål" dropdown
        self.resmål = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((
            By.XPATH, "/html/body/div[1]/div/header/div/div/section/div/ul/li[6]/div/a/span[1]")))
        self.resmål.click()
        # Find Tanzania
        self.Tanzania = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((
            By.XPATH, "/html/body/div[1]/div/section/div[4]/div/div[2]/div/ul/div/div[43]/li/a/div/div/div[2]"))).click()
        # Find "Visa alla hotell"
        self.show_all_hotels = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((
            By.XPATH, "/html/body/div[1]/div/section/div[2]/div/div/div/a/button"))).click()
        # Find "Reef & Beach Resort" on product page
        self.hotel_Tanzania = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((
            By.XPATH, "/html/body/div[1]/div/section/div[2]/div/div/h1/span"))).click()
        self.assertTrue(self.hotel_Tanzania.is_displayed(), "Product not found under header.")

    def test_kundservice(self):
        """
        Testing the "Kundservice" link and get some info
        """
        # Find "Kundservice" link
        self.customer_service = WebDriverWait(self.driver, 10).until(lambda d: d.find_element(
            By.XPATH, "/html/body/div[1]/div/header/div/div/div/div/div/ul/li[2]/span/a")).click()
        # Find a question
        self.question = WebDriverWait(self.driver, 10).until(lambda d: d.find_element(
            By.XPATH, "/html/body/div[1]/div/div/div[2]/div[3]/div")).click()
        self.assertTrue("covid-19-test-pa-min-resa" in self.driver.current_url, "Covid 19 answer is not present in the tui URL.")
        self.text = WebDriverWait(self.driver, 10).until(lambda d: d.find_element(
            By.XPATH, "/html/body/div[1]/div/div/div[2]/div[3]/div/div/div[2]/div[2]/div/div/div[1]/p")).text
        self.assertIn("erbjuder TUI test till rabatterat pris", self.text)
        
    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.quit()

    if __name__ == "__main__":
        main()
