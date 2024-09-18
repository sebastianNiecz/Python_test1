from selenium.webdriver.common.by import By
from BrowserDriver.BrowserDriver import BrowserDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class PageBase:
    browser_driver = BrowserDriver()
    wait = WebDriverWait(browser_driver.driver, 10)

    def go_to_specified_page(self, page):
        accept_all_button = "//button[@id='L2AGLb']"
        self.browser_driver.initialize_browser()
        self.browser_driver.go_to_page(page)
        time.sleep(2)
        self.click(accept_all_button)

    @staticmethod
    def find_specified_element(element):
        PageBase.wait.until(EC.visibility_of_element_located(element))
        PageBase.browser_driver.driver.find_element(By.XPATH,element)

    @staticmethod
    def get_text(locator):
        return PageBase.wait.until(EC.visibility_of_element_located(locator)).text

    @staticmethod
    def input_name(locator, name):
        element = PageBase.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(name)

 #   @staticmethod
    def click(self, locator):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, locator))).click()
