from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30, poll_frequency=1)

    def open(self):
        self.driver.get(self.PAGE_URL)

    def is_opened(self):
        self.wait.until(EC.url_to_be(self.PAGE_URL))


class AppiumBasePage:
    def __init__(self, appium_driver):
        self.appium_driver = appium_driver
