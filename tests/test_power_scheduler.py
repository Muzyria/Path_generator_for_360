
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

        new_time = self.settings_date_time.get_current_time_tuple()
        print(new_time)

        self.settings_date_time.switch_am_pm_time(new_time[2])

        self.settings_date_time.set_hours(new_time[0])
        self.settings_date_time.set_minutes(new_time[1])
        self.settings_date_time.button_ok_click()

        self.adb_command.get_time_off()
        self.adb_command.get_random_power_off_time()


        print("TEST ____ FINISH")
