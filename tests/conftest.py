import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def browser():
    options = Options()

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    base_url = 'https://freevpnplanet.com'
    driver.get(base_url)
    # driver.maximize_window()
    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def browser_and_download():
    download_directory = '/Users/ivanhrytsyna/PycharmProjects/vpn_planet/downloads'

    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")

    prefs = {
        "download.default_directory": download_directory,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    yield driver, download_directory

    driver.quit()


@pytest.fixture(scope='function')
def full_screen():
    options = Options()
    # options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)

    # driver.maximize_window()
    yield driver
    driver.quit()
