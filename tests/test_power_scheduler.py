
import subprocess
import time
import pytest
from base.adb_commands import AdbCommands

from appium.webdriver.common.appiumby import AppiumBy

from pages.device_pages.settings_date_time_page import SettingsDateTime


class TestPowerScheduler:
    IP = "192.168.0.101"

    @pytest.fixture(autouse=True)
    def adb_commands(self, request):
        print("ADB CONNECT START")
        request.cls.IP = self.IP
        self.adb_command = AdbCommands(self.IP)
        self.adb_command.device_connect()

    def test_first(self, appium_driver):
        """
        2)Set Power Scheduler at a 9:55 PM, Confirme randomizer's time on Power Scheduler - note it
        4) Wait randomizer's time and confirm device restart.
        """
        # el = appium_driver.find_element(AppiumBy.ID, value='com.l1inc.yamatrack3d:id/buttonMenu')
        # el.click()
        print("TEST__")
        test = SettingsDateTime(appium_driver)
        test.qwerety()
        print("TEST ____ FINISH")
