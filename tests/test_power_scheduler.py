
import subprocess
import time
import pytest
from base.adb_commands import AdbCommands

from appium.webdriver.common.appiumby import AppiumBy


class TestPowerScheduler:

    @pytest.fixture(autouse=True)
    def adb_commands(self):
        print("ADB CONNECT START")
        self.adb_command = AdbCommands("192.168.0.104")
        self.adb_command.device_connect()

    def test_first(self,  appium_driver):
        """
        2)Set Power Scheduler at a 9:55 PM, Confirme randomizer's time on Power Scheduler - note it
        4) Wait randomizer's time and confirm device restart.
        """
        el = appium_driver.find_element(AppiumBy.ID, value='com.l1inc.yamatrack3d:id/buttonMenu')
        el.click()

