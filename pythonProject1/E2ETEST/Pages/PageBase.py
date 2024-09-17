from selenium.webdriver.common.by import By
from E2ETEST.BrowserDriver.BrowserDriver import BrowserDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageBase:
    browser_driver = BrowserDriver().initialize_browser()
    wait = WebDriverWait(BrowserDriver.initialize_browser(), 10)
    button_locator = "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']"
    input_locator = "//textarea[@id='APjFqb']"


    @staticmethod
    def go_to_specified_page(page_name):
        BrowserDriver.go_to_page(page_name)

    @staticmethod
    def find_specified_element(self, element):
        self.wait.until(EC.visibility_of_element_located(element))
        return self.browser_driver.find_element(By.XPATH,element) == True

    @staticmethod
    def get_text(locator):
        return PageBase.wait.until(EC.visibility_of_element_located(locator)).text

    @staticmethod
    def input_name(locator, name):
        element = PageBase.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(name)

    @staticmethod
    def click(locator):
        PageBase.wait.until(EC.visibility_of_element_located((By.XPATH, locator))).click()