from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BrowserDriver:

    @staticmethod
    def initialize_browser():
        chrome_option = Options()
        chrome_option.add_argument("--disable-extensions")
        chrome_option.add_argument("--start-maximized")
        chrome_option.add_argument("--disable-infobars")
        chrome_option.add_argument("--incognito")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = chrome_option)
        driver.implicitly_wait(10)
        return driver

    @staticmethod
    def go_to_page(page):
        BrowserDriver.initialize_browser().get(page)

    @staticmethod
    def close_browser():
        BrowserDriver.initialize_browser().close()

