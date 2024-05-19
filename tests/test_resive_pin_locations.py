import os
import subprocess
import time

import pytest
from base.adb_commands import AdbCommands


class TestPinLocations:

    @pytest.fixture(autouse=True)
    def adb_commands(self):
        self.adb_command = AdbCommands("192.168.0.105")
        self.adb_command.device_connect()

    def read_device_logs(self):
        # command = 'adb logcat | Select-String -Pattern "Received custom message:"'
        pass


    def check_logcat(self, timeout=10):
        command = 'adb logcat | Select-String -Pattern "Received custom message:"'
        # subprocess.run(["powershell", "-Command", command])

        subprocess.run(["start", "powershell", "-Command", command], shell=True)
        time.sleep(15)

    @pytest.mark.parametrize("i", range(1, 3))
    def test_pin_locations(self, signature_api_360, i):
        print(signature_api_360.SECRET_KEY)
        signature_api_360.pin_position_update()

        # Ожидаем, пока данные придут на устройство
        data_received = self.check_logcat(timeout=60)

        # Проверяем, были ли данные получены на устройстве
        # assert data_received, "Data was not received on the device."
