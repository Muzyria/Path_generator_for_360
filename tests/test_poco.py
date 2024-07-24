import time
from contextlib import suppress
from selenium.common.exceptions import WebDriverException

class TestPOCO:
    IP = "dbe407da"
    app_package = "com.l1inc.yamatrack3d"

    def test_first(self, appium_driver):
        print("first test")
        appium_driver.activate_app(self.app_package)
        time.sleep(10)
        with suppress(WebDriverException):
            appium_driver.terminate_app(self.app_package)
        print("test complite")
