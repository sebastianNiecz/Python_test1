from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BrowserDriver:

    @staticmethod
    def initialize_browser():
        chrome_option = Options()
        chrome_option.add_argument("--disable-extensions")
        driver = webdriver.Chrome(options = chrome_option)
        driver.implicitly_wait(10)
        return driver

    @staticmethod
    def go_to_page(page):
        BrowserDriver.initialize_browser().get(page)

    @staticmethod
    def close_browser():
        BrowserDriver.initialize_browser().close()

