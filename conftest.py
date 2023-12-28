import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options as OptionsFirefox

drivers = {'chrome': 'chromedriver.exe', 'firefox': 'geckodriver.exe', 'yandex': 'yandexdriver.exe'}


def get_driver_file_path(os_type, browser_name):
    # os.chdir("..")
    if os_type == "windows":
        if browser_name in drivers.keys():
            return os.path.join(os.getcwd(), 'drivers', 'windows', drivers[browser_name])
        else:
            raise pytest.UsageError("browser_name should be chrome, yandex or firefox")
    elif os_type == "linux":
        pass
    else:
        raise pytest.UsageError("os_type should be windows or linux")


def set_browser_options(browser_name, language):
    if browser_name == 'chrome':
        options = OptionsChrome()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        return options
    elif browser_name == 'yandex':
        options = OptionsChrome()
        options.add_argument(f'--lang={language}')
        return options
    elif browser_name == 'firefox':
        options = OptionsFirefox()
        options.set_preference("intl.accept_languages", language)
        return options
    else:
        raise pytest.UsageError("browser_name should be chrome, yandex or firefox")


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome, yandex or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose browser language")
    parser.addoption('--os_type', action='store', default="windows",
                     help="Choose operation system: windows or linux")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    os_type = request.config.getoption("os_type")

    binary_driver_file = get_driver_file_path(os_type=os_type, browser_name=browser_name)
    service = Service(executable_path=binary_driver_file)
    options = set_browser_options(browser_name=browser_name, language=language)

    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(service=service, options=options)
    elif browser_name == "yandex":
        print("\nstart yandex browser for test..")
        browser = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(service=service, options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
