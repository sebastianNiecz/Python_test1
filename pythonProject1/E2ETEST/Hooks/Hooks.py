from E2ETEST.BrowserDriver.BrowserDriver import BrowserDriver


class Hooks:

    @staticmethod
    def before_scenario():
        BrowserDriver.initialize_browser()

    @staticmethod
    def before_feature():
        BrowserDriver.initialize_browser()

    @staticmethod
    def after_feature():
        BrowserDriver.close_browser()

    @staticmethod
    def after_scenario():
        BrowserDriver.close_browser()