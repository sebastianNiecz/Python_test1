from BrowserDriver.BrowserDriver import BrowserDriver


class Hooks:
    browser_driver = BrowserDriver()
    @staticmethod

    def before_scenario():
        Hooks.browser_driver.initialize_browser()

    @staticmethod
    def before_feature():
        Hooks.browser_driver.initialize_browser()

    @staticmethod
    def after_feature():
        Hooks.browser_driver.close_browser()

    @staticmethod
    def after_scenario(self=None):
        Hooks.browser_driver.close_browser()
