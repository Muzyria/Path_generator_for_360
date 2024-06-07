from base.base_page import AppiumBasePage
from appium.webdriver.common.appiumby import AppiumBy

from datetime import datetime, timedelta
from selenium.webdriver.support import expected_conditions as EC


class SettingsDateTime(AppiumBasePage):

    SET_POWER_TIME = ("xpath", "(//android.widget.LinearLayout)[17]")

    CLOCK_HOURS = ("id", "android:id/hours")
    CLOCK_MINUTES = ("id", "android:id/minutes")

    AM_LABEL = ("id", "android:id/am_label")
    PM_LABEL = ("id", "android:id/pm_label")

    @staticmethod
    def get_hours_locator(hours_value):
        return ("xpath", f'//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc="{hours_value}"]')  # from 1 to 12

    @staticmethod
    def get_minutes_locator(minutes_value):
        return ("xpath", f'//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc="{minutes_value}"]')  # from 0 to 55 by step 5

    BUTTON_OK = ("id", "android:id/button1")

    def click_set_power_time(self):
        self.wait.until(EC.element_to_be_clickable(self.SET_POWER_TIME)).click()

    def click_pm_label(self):
        self.wait.until(EC.element_to_be_clickable(self.PM_LABEL)).click()

    def click_am_label(self):
        self.wait.until(EC.element_to_be_clickable(self.AM_LABEL)).click()

    def switch_am_pm_time(self, value):
        if value == "AM":
            self.click_am_label()
        else:
            self.click_pm_label()

    def set_hours(self, hours_value=10):
        self.wait.until(EC.element_to_be_clickable(self.get_hours_locator(hours_value))).click()

    def set_minutes(self, minutes_value=0):
        self.wait.until(EC.element_to_be_clickable(self.get_minutes_locator(minutes_value))).click()

    def button_ok_click(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_OK)).click()

    @staticmethod
    def get_current_time_tuple(extra_minute=5):
        # Получаем текущее время
        now = datetime.now()
        # Извлекаем часы и минуты
        hour = now.strftime("%I")
        minute = int(now.strftime("%M"))
        # Определяем часть дня (AM/PM)
        period = now.strftime("%p")
        # Округляем минуты вверх с шагом 5
        if minute % 5 != 0:
            minute = (minute // 5 + 1) * 5
            if minute == 60:
                minute = 0
                now += timedelta(hours=1)
                hour = now.strftime("%I")
                period = now.strftime("%p")
        return int(hour), minute + extra_minute, period

