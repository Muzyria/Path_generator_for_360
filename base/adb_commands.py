import os
import subprocess
import time
from datetime import datetime, timedelta
import re


class AdbCommands:
    def __init__(self, ip_device=None):
        self.ip_device = ip_device

    @staticmethod
    def device_read_ip_address():
        """Получение IP адрес девайса при подключении по USB"""
        os.system(fr'adb shell ip addr show wlan0')  # читаем IP девайса
        result = subprocess.run(["adb", "shell", "ip", "addr", "show", "wlan0"], capture_output=True, text=True)
        output_lines = result.stdout.splitlines()

        # Регулярное выражение для извлечения IP-адреса
        pattern = r'inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        ip_address = re.search(pattern, [item for item in output_lines if 'inet ' in item][0]).group(0).split()[1]
        print(ip_address)
        return ip_address

    def adb_get_state(self):
        output = os.system('adb get-state')
        # print(f'{output}')
        return output

    def device_disconnect(self):
        os.system(f'adb disconnect {self.ip_device}')

    def device_connect(self):
        print(f"\n CONNECT DEVICE {self.ip_device}")
        os.system(f'adb connect {self.ip_device}')

    def device_reboot(self):
        os.system(f'adb -s {self.ip_device} reboot')

    def check_devices_active(self):
        """Проверяем, есть ли подключенные устройства в выводе в консоль"""
        output = subprocess.check_output(['adb', 'devices'])
        if self.ip_device in str(output) and "offline" not in str(output):
            print('Устройство Android подключено и активно.')

        else:
            print(f'Устройство Android {self.ip_device} будет подключено By TCP/IP')
            self.device_disconnect()
            time.sleep(2)
            self.device_connect()


    def device_send_key(self, key=26):
        os.system(f'adb -s {self.ip_device} shell input keyevent {key}')

    def touch_screen(self, x=700, y=500):
        os.system(f'adb -s {self.ip_device} shell input tap {x} {y}')

    def device_send_coordinate(self, location):
        os.system(rf'adb -s {self.ip_device}:5555 shell am broadcast -a ua.org.jeff.mockgps.ACTION_LOCATION --es location \"{location}\"')  # "50.012356,36.243361"

    def device_in_cart_barn(self):
        os.system(f'adb -s {self.ip_device} shell am broadcast -a com.l1inc.yamatrack3d.action.powermanagement.cart_barn_sleep')

    def device_in_off_hole(self):
        os.system(f'adb -s {self.ip_device} shell am broadcast -a com.l1inc.yamatrack3d.action.powermanagement.not_on_hole_sleep')

    def device_close_yamatack(self):
        os.system(f'adb -s {self.ip_device} shell am force-stop com.l1inc.yamatrack3d')

    def device_close_all(self):
        os.system(f'adb -s {self.ip_device} shell input keyevent KEYCODE_HOME')

    def device_kill_app(self):
        os.system(f'adb -s {self.ip_device} shell input keyevent KEYCODE_APP_SWITCH')
        os.system(f'adb -s {self.ip_device} shell input keyevent DEL')

    def device_get_system_volume_speaker(self):
        """Get value system volume speaker"""
        os.system(f'adb -s {self.ip_device} shell settings get system volume_alarm_speaker')

    """SETTINGS PAGES"""
    def device_open_settings_main_page(self):
        os.system(f'adb -s {self.ip_device} shell am start -a android.settings.SETTINGS')

    def device_open_wifi_settings(self):
        """Open pages Settings WI-FI"""
        os.system(f'adb -s {self.ip_device} shell am start -a android.settings.WIFI_SETTINGS')

    def device_open_wireless_settings(self):
        """Open pages Settings WireLess"""
        os.system(f'adb -s {self.ip_device} shell am start -a android.settings.WIRELESS_SETTINGS')

    def device_open_sounds_settings(self):
        """Open pages Settings Sounds"""
        os.system(f'adb -s {self.ip_device} shell am start -a android.settings.SOUND_SETTINGS')

    def device_open_location_settings(self):
        """Open pages Settings Location"""
        os.system(f'adb -s {self.ip_device} shell am start -a android.settings.LOCATION_SOURCE_SETTINGS')

    def open_date_settings(self):
        """Open pages Settings Date"""
        os.system(f'adb -s {self.ip_device} shell am start -a android.settings.DATE_SETTINGS')

    def open_device_info_settings(self):
        """Open pages Settings Device Info"""
        os.system(f'adb -s {self.ip_device} shell am start -a android.settings.DEVICE_INFO_SETTINGS')

    def open_device_developer_options_settings(self):
        """Open pages Settings Developer Options"""
        os.system(f'adb -s {self.ip_device} shell am start -a android.settings.APPLICATION_DEVELOPMENT_SETTINGS')