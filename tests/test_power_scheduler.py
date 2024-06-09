
import subprocess
import time
import pytest
from base.adb_commands import AdbCommands

from pages.device_pages.settings_date_time_page import SettingsDateTime


def log_message(message):
    with open("test_logs/log_scheduler.txt", "a", encoding="utf-8") as log_file:
        log_file.write(message + "\n")


def calculate_timeout(reboot_time_str):
    current_time = time.localtime()
    current_time_in_minutes = current_time.tm_hour * 60 + current_time.tm_min

    reboot_hour = int(reboot_time_str[:2])
    reboot_minute = int(reboot_time_str[2:])
    reboot_time_in_minutes = reboot_hour * 60 + reboot_minute

    if reboot_time_in_minutes < current_time_in_minutes:
        reboot_time_in_minutes += 24 * 60  # добавляем 24 часа, если время перезагрузки на следующий день

    timeout_in_minutes = reboot_time_in_minutes - current_time_in_minutes
    timeout_in_seconds = timeout_in_minutes * 60
    return timeout_in_seconds


class TestPowerScheduler:
    IP = "192.168.0.101"
    MESSAGE_REBOOT = "START u0 {act=android.intent.action.REBOOT"
    MESSAGE_SHUTDOWN = "START u0 {act=android.intent.action.ACTION_REQUEST_SHUTDOWN"

    settings_date_time: SettingsDateTime

    @pytest.fixture(autouse=True)
    def adb_commands(self, request):
        print()
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

    def check_for_message(self, message_to_find, reboot_time_str, interval=60):
        timeout = calculate_timeout(reboot_time_str)

        start_time = time.time()
        start_time_readable = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))
        print(f"Начало ожидания сообщения в {start_time_readable} с тайм-аутом {timeout} секунд")
        print(f"Планируемое время перезагрузки в {reboot_time_str[:2]}:{reboot_time_str[2:]}")

        last_adb_execution_time = start_time - interval  # Изначально устанавливаем время последнего выполнения adb

        while time.time() - start_time < timeout:
            current_time = time.time()
            if current_time - last_adb_execution_time >= interval:
                # Выполняем команду adb
                self.adb_command.swipe_screen(100, 500, 200, 500, 250)
                self.adb_command.swipe_screen(200, 500, 100, 500, 250)
                last_adb_execution_time = current_time  # Обновляем время последнего выполнения adb

            try:
                output = self.run_adb_logcat()
                if message_to_find in output:
                    end_time = time.time()
                    end_time_readable = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))
                    duration = int(end_time - start_time)  # Преобразуем продолжительность ожидания в целое число
                    print(f"Сообщение найдено в {end_time_readable}")
                    print(f"Время ожидания: {duration} секунд")
                    return True
            except Exception as e:
                print(f"Произошла ошибка: {e}")
                print(output)  # Добавляем вывод результата работы метода run_adb_logcat()

            time.sleep(1)  # Проверяем каждую секунду

        return False

    def test_first(self):
        """
        2)Set Power Scheduler at a 9:55 PM, Confirm randomizer's time on Power Scheduler - note it
        4) Wait randomizer's time and confirm device restart.
        """

        print("TEST __ START")
        # self.adb_command.open_date_settings()
        #
        # self.settings_date_time.click_set_power_time()
        #
        # new_time = self.settings_date_time.get_new_time_tuple()
        # print(new_time)

        # self.settings_date_time.switch_am_pm_time(new_time[2])
        #
        # self.settings_date_time.set_hours(new_time[0])
        # self.settings_date_time.set_minutes(new_time[1])
        # self.settings_date_time.button_ok_click()


        self.adb_command.put_time_off("0230")
        self.adb_command.put_random_time_off("0246")


        time_off = self.adb_command.get_time_off()
        random_time_off = self.adb_command.get_random_power_off_time()

        # self.adb_command.device_send_key(4)

        # Ожидаем получение сообщения
        message_to_find = self.MESSAGE_REBOOT

        if self.check_for_message(message_to_find, random_time_off):
            print("__OK__")
            print("ОЖИДАНИЕ REBOOT 120 СУКУНД")
            # time.sleep(120)
        else:
            pytest.fail("Сообщение не найдено в течение заданного времени.")

        print("TEST ____ FINISH")
