from datetime import datetime

from base.base_page import BasePage
from config.links import Links_syncwise360
from selenium.webdriver.support import expected_conditions as EC


def my_decorator(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        duration = (end - start).total_seconds()
        print(f"Время выполнения функции {func.__name__}: {duration} секунд")
    return wrapper


class LoginPageSyncwise360(BasePage):

    PAGE_URL = Links_syncwise360.LOGIN_PAGE

    USERNAME_FIELD = ("xpath", "//input[@id='username']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")
    BUTTON_LOGIN = ("xpath", "//button[@aria-label='submit']")

    SPINNER = ("xpath", "//div[@class='loader']")

    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)

    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_LOGIN)).click()


    @my_decorator
    def spinner(self):
        self.wait.until(EC.visibility_of_element_located(self.SPINNER))

        self.wait.until(EC.invisibility_of_element_located(self.SPINNER))



