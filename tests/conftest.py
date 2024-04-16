import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Chrome()
    base_url = 'https://freevpnplanet.com'
    driver.get(base_url)
    yield driver

    driver.quit()






