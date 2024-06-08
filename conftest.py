
import pytest
import subprocess

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService

from selenium.common.exceptions import WebDriverException

from base.sincwise_clients_method import SyncwiseClient


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


@pytest.fixture(scope="function")
def appium_service():
    """appium service fixture"""
    print("\nstart appium_service")
    service = AppiumService()
    service.start(
        args=['--address', '127.0.0.1', '-p', '4723'],
        timeout_ms=20000,
    )
    yield service
    service.stop()


@pytest.fixture(scope="function")
def appium_driver(appium_service, request):
    """appium fixture"""
    print()
    print('__USE_APPIUM_FIXTURE__')
    print("\nstart appium_driver for test..")

    device_name = request.cls.IP

    capabilities = dict(
        platformName='android',
        automationName='uiautomator2',
        deviceName=device_name,
        newCommandTimeout=600
    )

    appium_server_url = 'http://localhost:4723'
    appium_driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    yield appium_driver
    print("\nquit appium_driver..")
    try:
        appium_driver.quit()
    except WebDriverException as e:
        print("Session terminated unexpectedly:", e)
