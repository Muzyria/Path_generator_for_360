
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


    def run_adb_logcat(self):
        # Запуск команды adb logcat
        process = subprocess.Popen('adb logcat -d', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, _ = process.communicate()
        return output.decode('utf-8', errors='ignore')

    def check_for_message(self, message_to_find, timeout=3900, interval=60):
        start_time = time.time()
        start_time_readable = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))
        print(f"Начало ожидания сообщения в {start_time_readable}")
        # log_file = open("log.txt", "a", encoding="utf-8")  # Открываем файл логов для добавления сообщений
        # log_file.write(f"Start waiting for messages at {start_time_readable}\n")

        last_adb_execution_time = start_time - interval  # Изначально устанавливаем время последнего выполнения adb

        while time.time() - start_time < timeout:
            current_time = time.time()
            if current_time - last_adb_execution_time >= interval:
                # Выполняем команду adb
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
                    # log_file.write(f"The message found at {end_time_readable}\n")
                    # log_file.write(f"Waiting time: {duration} seconds\n\n")
                    # log_file.close()  # Закрываем файл после записи

                    return True
            # ---------------------------------------------------------------------------------------------------
            except Exception as e:
                print(f"Произошла ошибка: {e}")
                print(output)  # Добавляем вывод результата работы метода run_adb_logcat()
            # ---------------------------------------------------------------------------------------------------
            time.sleep(1)  # Проверяем каждую секунду

        # log_file.write(f"Message not found for {timeout} seconds.\n")
        # log_file.close()  # Закрываем файл после записи
        return False

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

        self.adb_command.device_send_key(4)

        # Ожидаем получение сообщения
        message_to_find = "START u0 {act=android.intent.action.REBOOT"
        if self.check_for_message(message_to_find):
            print("ОЖИДАНИЕ REBOOT 120 СУКУНД")
            time.sleep(120)
        else:
            pytest.fail("Сообщение не найдено в течение заданного времени.")

        print("TEST ____ FINISH")
