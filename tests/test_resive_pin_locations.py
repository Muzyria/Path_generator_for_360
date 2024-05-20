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

    def check_for_message(self, message_to_find, timeout=1200):
        start_time = time.time()
        start_time_readable = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))
        print(f"Начало ожидания сообщения в {start_time_readable}")
        log_file = open("log.txt", "a", encoding="utf-8")  # Открываем файл логов для добавления сообщений
        log_file.write(f"Start waiting for messages at {start_time_readable}\n")

        while time.time() - start_time < timeout:
            output = self.run_adb_logcat()
            if message_to_find in output:
                end_time = time.time()
                end_time_readable = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))
                duration = int(end_time - start_time)  # Преобразуем продолжительность ожидания в целое число
                print(f"Сообщение найдено в {end_time_readable}")
                print(f"Время ожидания: {duration} секунд")
                log_file.write(f"The message found at {end_time_readable}\n")
                log_file.write(f"Waiting time: {duration} seconds\n\n")
                # log_file.write(f"Полное сообщение: {output}\n")
                log_file.close()  # Закрываем файл после записи
                return True
            time.sleep(1)  # Проверяем каждую секунду

        log_file.write(f"Сообщение не найдено в течение {timeout} секунд.\n")
        log_file.close()  # Закрываем файл после записи
        return False

    @pytest.mark.parametrize("location", [(50.08200445682767, 36.230381742010366), (50.08197390756561, 36.23083627639708)])
    @pytest.mark.parametrize("i", range(1, 3))
    def test_pin_locations(self, signature_api_360, i, location):
        print(signature_api_360.SECRET_KEY)
        print(location, i)
        signature_api_360.pin_position_update(location)

        # Ожидаем получение сообщения
        message_to_find = "Received custom message"
        # message_to_find = "Received custom message: 06[KoyhA-zWt6os;240521;01"

        if self.check_for_message(message_to_find):
            print("Сообщение найдено.")
            time.sleep(90)
        else:
            pytest.fail("Сообщение не найдено в течение заданного времени.")


