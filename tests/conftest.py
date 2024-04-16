import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.fixture(scope='function')
def browser():
    driver = webdriver.Chrome()
    base_url = 'https://freevpnplanet.com'
    driver.get(base_url)
    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def browser_and_download():

    download_directory = '/Users/ivanhrytsyna/PycharmProjects/vpn_planet/downloads'

    chrome_options = Options()
    prefs = {
        "download.default_directory": download_directory,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chrome_options)
    yield driver, download_directory

    driver.quit()







