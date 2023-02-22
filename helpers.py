class Helpers():

    # Helper for waiting explicitly
    def document_initialised(driver):
        return driver.execute_script("return initialised")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.tui.se/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.quit()
        
    