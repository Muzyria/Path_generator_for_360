import subprocess
import time
import pytest
from base.adb_commands import AdbCommands


class TestPinLocations:

    @pytest.fixture(autouse=True)
    def adb_commands(self):
        self.adb_command = AdbCommands("192.168.0.106")
        self.adb_command.device_connect()

    def run_adb_logcat(self):
        # Запуск команды adb logcat
        process = subprocess.Popen('adb logcat -d', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                                   shell=True)
        output, _ = process.communicate()
        return output

    def check_for_message(self, message_to_find, timeout=300):
        start_time = time.time()
        start_time_readable = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))
        print(f"Начало ожидания сообщения в {start_time_readable}")

        while time.time() - start_time < timeout:
            output = self.run_adb_logcat()
            if message_to_find in output:
                end_time = time.time()
                end_time_readable = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))
                duration = end_time - start_time
                print(f"Сообщение найдено в {end_time_readable}")
                print(f"Полное сообщение: {output}")
                print(f"Время ожидания: {duration} секунд")
                return True
            time.sleep(1)  # Проверяем каждую секунду

        print(f"Сообщение не найдено в течение {timeout} секунд.")
        return False

    @pytest.mark.parametrize("i", range(1, 2))
    def test_pin_locations(self, signature_api_360, i):
        print(signature_api_360.SECRET_KEY)
        signature_api_360.pin_position_update()

        # Ожидаем получение сообщения
        message_to_find = "Received custom message"
        if self.check_for_message(message_to_find):
            print("Сообщение найдено.")
        else:
            pytest.fail("Сообщение не найдено в течение заданного времени.")
