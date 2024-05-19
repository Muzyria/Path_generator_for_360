
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from base.adb_commands import AdbCommands
from base.sincwise_clients_method import SyncwiseClient


# device_name = "192.168.2.31"
# device_name = "dbe407da"


def pytest_addoption(parser):
    """Опции командной строки.
    В командную строку передается параметр вида '--language="es"'
    По умолчанию передается параметр, включающий английский интерфейс в браузере
    """
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ---")


@pytest.fixture(scope="function")
def driver(request):
    """selenium fixture"""
    print()
    print("__USE_SELENIUM_FIXTURE__")
    print("\nstart driver for test..")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Убираем лишние ошибки из консоли

    user_language = request.config.getoption("language")
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    request.cls.driver = driver
    yield driver
    print("\nquit driver..")
    driver.quit()


@pytest.fixture(scope="function")
def signature_api_360():
    data = SyncwiseClient("https://api2.syncwise360.com")
    data.user_account_login()
    print("__SIGNATURE_SUCCESSFUL__")
    return data



