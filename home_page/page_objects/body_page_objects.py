import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class HomePageBody:
    url = 'https://freevpnplanet.com/'

    def __init__(self, browser):
        self.driver = browser

    def go_to(self):
        self.driver.get(HomePageBody.url)

    def find_os_and_browsers_links(self, expected_title):
        wait = WebDriverWait(self.driver, 10)

        cookies_locator = (By.CLASS_NAME, 'cookies__btn')
        cookies_element = wait.until(EC.element_to_be_clickable(cookies_locator))
        cookies_element.click()

        android_locator = (By.CSS_SELECTOR, '#__layout > div > div:nth-child(1) > main > header > div.page-section.light > div > div > div > a:nth-child(1)')
        android_element = wait.until(EC.element_to_be_clickable(android_locator))
        android_element.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def go_back(self):
        self.driver.get(HomePageBody.url)
