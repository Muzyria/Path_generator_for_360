from base.base_page import AppiumBasePage
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support import expected_conditions as EC

class SettingsDateTime(AppiumBasePage):

    def qwerety(self):
        print("QQQQQQQ")
        # el = self.appium_driver.find_element(AppiumBy.ID, value='com.l1inc.yamatrack3d:id/buttonMenu')
        el = self.wait.until(EC.element_to_be_clickable(('id', 'com.l1inc.yamatrack3d:id/buttonMenu')))
        el.click()


