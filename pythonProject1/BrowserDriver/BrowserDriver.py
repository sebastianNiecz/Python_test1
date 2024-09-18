from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BrowserDriver:

    def __init__(self):
        self.driver = None
        self.chrome_option = None

    def initialize_browser(self):
        self.chrome_option = Options()
        self.chrome_option.add_argument("--disable-extensions")
        self.chrome_option.add_argument("--start-maximized")
        self.chrome_option.add_argument("--disable-infobars")
        self.chrome_option.add_argument("--incognito")
        self.chrome_option.add_argument("--disable-search-engine-choice-screen")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = self.chrome_option)
        self.driver.implicitly_wait(10)


    def go_to_page(self, page):
        self.driver.get(page)


    def close_browser(self):
        self.driver.close()

