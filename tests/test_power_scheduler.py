
import subprocess
import time
import pytest
from base.adb_commands import AdbCommands

from pages.device_pages.settings_date_time_page import SettingsDateTime


class TestPowerScheduler:
    IP = "192.168.0.101"

    settings_date_time: SettingsDateTime

    @pytest.fixture(autouse=True)
    def adb_commands(self, request):
        print("ADB CONNECT START")
        request.cls.IP = self.IP
        self.adb_command = AdbCommands(self.IP)
        self.adb_command.device_connect()

    @pytest.fixture(autouse=True)
    def setup(self, request, appium_driver):
        request.cls.settings_date_time = SettingsDateTime(appium_driver)

    def test_first(self):
        """
        2)Set Power Scheduler at a 9:55 PM, Confirm randomizer's time on Power Scheduler - note it
        4) Wait randomizer's time and confirm device restart.
        """

        print("TEST __ START")
        self.adb_command.open_date_settings()

        self.settings_date_time.click_set_power_time()

        self.settings_date_time.click_pm_label()
        self.settings_date_time.set_hours(6)
        self.settings_date_time.set_minutes(20)
        self.settings_date_time.button_ok_click()
        print("TEST ____ FINISH")
