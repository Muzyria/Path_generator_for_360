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
        # Команда для чтения логов с устройства через adb
        adb_command = "adb logcat"

        # Запускаем процесс adb logcat и читаем его вывод
        try:
            output = os.popen(adb_command).read()
            return output
        except Exception as e:
            return f"Error reading device logs: {e}"

    def check_logcat(self, timeout=10):
        start_time = time.time()
        while time.time() - start_time < timeout:
            # Читаем логи с устройства
            logs = self.read_device_logs()
            # Проверяем, содержится ли в логах ожидаемое сообщение
            if "Received custom message:" in logs:
                return True
            time.sleep(1)
        return False

    @pytest.mark.parametrize("i", range(1, 2))
    def test_pin_locations(self, signature_api_360, i):
        print(signature_api_360.SECRET_KEY)
        signature_api_360.pin_position_update()

        # Ожидаем, пока данные придут на устройство
        data_received = self.check_logcat(timeout=30)

        # Проверяем, были ли данные получены на устройстве
        assert data_received, "Data was not received on the device."
