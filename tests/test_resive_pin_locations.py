
import allure
import subprocess
import time
import pytest
from base.adb_commands import AdbCommands


# @allure.feature("Check Functionality")
class TestPinLocations:
    EXPECTED_TIME = 120
    ACTUAL_TIME = None

    @pytest.fixture(autouse=True)
    def adb_commands(self, request):
        if 'usb' in request.keywords:
            device = self.get_connected_device()
            self.adb_command = AdbCommands(device)
            print(f"Устройство для подключения по USB: {device}")
        else:
            self.adb_command = AdbCommands("192.168.0.105")
            self.adb_command.device_connect()

    def get_connected_device(self):
        # Получаем список подключенных устройств
        process = subprocess.Popen('adb devices', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        output, _ = process.communicate()
        lines = output.strip().split('\n')

        if len(lines) > 1:
            # Второй элемент будет первым устройством в списке
            device = lines[1].split('\t')[0]
            print(f"Подключенное устройство: {device}")
            return device
        else:
            raise Exception("Нет подключенных устройств.")

    def run_adb_logcat(self):
        # Запуск команды adb logcat
        # process = subprocess.Popen('adb logcat -d', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
        #                            shell=True)
        # output, _ = process.communicate()
        # return output

        # --------------
        # Запуск команды adb logcat
        process = subprocess.Popen('adb logcat -d', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, _ = process.communicate()
        return output.decode('utf-8', errors='ignore')

    def check_for_message(self, message_to_find, timeout=3600, interval=60):
        start_time = time.time()
        start_time_readable = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))
        print(f"Начало ожидания сообщения в {start_time_readable}")
        log_file = open("log.txt", "a", encoding="utf-8")  # Открываем файл логов для добавления сообщений
        log_file.write(f"Start waiting for messages at {start_time_readable}\n")

        last_adb_execution_time = start_time - interval  # Изначально устанавливаем время последнего выполнения adb

        while time.time() - start_time < timeout:
            current_time = time.time()
            if current_time - last_adb_execution_time >= interval:
                # Выполняем команду adb
                # subprocess.run(['adb', 'shell input tap 700 500'])
                # self.adb_command.touch_screen(800, 700)
                self.adb_command.swipe_screen(100, 500, 200, 500, 250)
                self.adb_command.swipe_screen(200, 500, 100, 500, 250)
                last_adb_execution_time = current_time  # Обновляем время последнего выполнения adb
            # ---------------------------------------------------------------------------------------------------
            try:
                output = self.run_adb_logcat()
            # ---------------------------------------------------------------------------------------------------
                if message_to_find in output:
                    end_time = time.time()
                    end_time_readable = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))
                    duration = int(end_time - start_time)  # Преобразуем продолжительность ожидания в целое число
                    print(f"Сообщение найдено в {end_time_readable}")
                    print(f"Время ожидания: {duration} секунд")
                    log_file.write(f"The message found at {end_time_readable}\n")
                    log_file.write(f"Waiting time: {duration} seconds\n\n")
                    log_file.close()  # Закрываем файл после записи

                    self.ACTUAL_TIME = duration

                    print("ДОПОЛНИТЕЛЬНОЕ ОЖИДАНИЕ 120 СУКУНД")
                    time.sleep(60)
                    self.adb_command.touch_screen(800, 700)
                    time.sleep(60)
                    return True
            # ---------------------------------------------------------------------------------------------------
            except Exception as e:
                print(f"Произошла ошибка: {e}")
                print(output)  # Добавляем вывод результата работы метода run_adb_logcat()
            # ---------------------------------------------------------------------------------------------------
            time.sleep(1)  # Проверяем каждую секунду

        log_file.write(f"Message not found for {timeout} seconds.\n")
        log_file.close()  # Закрываем файл после записи
        return False

    # @allure.step("Check duration time")
    def check_duration_time(self):
        assert self.EXPECTED_TIME >= self.ACTUAL_TIME, f"Время доставки сообщения {self.ACTUAL_TIME} превысило {self.EXPECTED_TIME}"

    @pytest.mark.usb
    @pytest.mark.parametrize("location", [(50.08200445682767, 36.230381742010366), (50.08197390756561, 36.23083627639708)])
    @pytest.mark.parametrize("i", range(1, 20))
    def test_pin_locations_usb(self, signature_api_360, i, location):
        print("  CONNECT BY USB")
        print(signature_api_360.SECRET_KEY)
        print(location, i)
        signature_api_360.pin_position_update(location)

        # Ожидаем получение сообщения
        message_to_find = "Received custom message"

        if self.check_for_message(message_to_find):
            # self.check_duration_time()
            print("Подготовка следующего теста.")
            print("Ожидание внутри теста 60 секунд")
            self.adb_command.touch_screen(800, 700)
            time.sleep(60)
            self.adb_command.touch_screen(800, 700)

        else:
            pytest.fail("Сообщение не найдено в течение заданного времени.")

    # @allure.title("Receiving update messages")
    # @allure.severity("Critical")
    @pytest.mark.wifi
    @pytest.mark.parametrize("location", [(50.08200445682767, 36.230381742010366), (50.08197390756561, 36.23083627639708)])
    @pytest.mark.parametrize("i", range(1, 20))
    def test_pin_locations_wifi(self, signature_api_360, i, location):
        print('  CONNECT BY WIFI')
        print(signature_api_360.SECRET_KEY)
        print(location, i)
        signature_api_360.pin_position_update(location)

        # Ожидаем получение сообщения
        # message_to_find = "Received custom message"

        text_message = str(location[0])[:8]
        message_to_find = f"Received custom message: 06[KoyhA-zWt6os;240526;01,{text_message}"
        print(message_to_find)

        if self.check_for_message(message_to_find):
            # self.check_duration_time()
            print("Подготовка следующего теста.")
            print("Ожидание внутри теста 60 секунд")
            time.sleep(60)
        else:
            pytest.fail("Сообщение не найдено в течение заданного времени.")
