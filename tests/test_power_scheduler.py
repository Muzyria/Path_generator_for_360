
import subprocess
import time
import pytest
from base.adb_commands import AdbCommands


class TestPowerScheduler:

    @pytest.fixture(autouse=True)
    def adb_commands(self):
        self.adb_command = AdbCommands("192.168.0.105")
        self.adb_command.device_connect()

    def test_first(self):
        """
        2)Set Power Scheduler at a 9:55 PM, Confirme randomizer's time on Power Scheduler - note it
        4) Wait randomizer's time and confirm device restart.
        """

