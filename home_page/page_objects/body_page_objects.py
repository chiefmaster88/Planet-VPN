import os
import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePageBody:
    url = 'https://freevpnplanet.com/'

    def __init__(self, browser):
        self.driver = browser

    def go_to(self):
        self.driver.get(HomePageBody.url)

    def find_body_links_and_buttons(self, expected_title):
        # find cookies & close
        wait = WebDriverWait(self.driver, 10)
        cookies_locator = (By.CLASS_NAME, 'cookies__btn')
        cookies_element = wait.until(EC.element_to_be_clickable(cookies_locator))
        cookies_element.click()

        # find android locator & click
        android_locator = (By.CSS_SELECTOR,
                           '#__layout > div > div:nth-child(1) > main > header > div.page-section.light > div > div > div > a:nth-child(1)')
        android_element = wait.until(EC.element_to_be_clickable(android_locator))
        android_element.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutException:
            return False

    def find_drop_down(self):
        self.driver.execute_script("window.scrollBy(0, 6500);")
        wait = WebDriverWait(self.driver, 10)
        dropdown_locators = [
            (By.CSS_SELECTOR,
             '#__layout > div > div:nth-child(1) > main > div:nth-child(9) > div > div > article:nth-child(2) > div.faq-item__question'),
            (By.CSS_SELECTOR,
             '#__layout > div > div:nth-child(1) > main > div:nth-child(9) > div > div > article:nth-child(3) > div.faq-item__question'),

            (By.CSS_SELECTOR,
             '#__layout > div > div:nth-child(1) > main > div:nth-child(9) > div > div > article:nth-child(4) > div.faq-item__question'),

            (By.CSS_SELECTOR,
             '#__layout > div > div:nth-child(1) > main > div:nth-child(9) > div > div > article:nth-child(5) > div.faq-item__question'),

            (By.CSS_SELECTOR,
             '#__layout > div > div:nth-child(1) > main > div:nth-child(9) > div > div > article:nth-child(6) > div.faq-item__question'),

            (By.CSS_SELECTOR,
             '#__layout > div > div:nth-child(1) > main > div:nth-child(9) > div > div > article:nth-child(7) > div.faq-item__question'),

            (By.CSS_SELECTOR,
             '#__layout > div > div:nth-child(1) > main > div:nth-child(9) > div > div > article:nth-child(8) > div.faq-item__question'),

        ]

        for locator in dropdown_locators:
            dropdown_element = wait.until(EC.element_to_be_clickable(locator))
            dropdown_element.click()
            time.sleep(1)
            self.driver.execute_script("window.scrollBy(0, 150);")

    def go_back(self):
        self.driver.get(HomePageBody.url)


class DownloadPage:

    def __init__(self, driver, download_directory):
        self.driver = driver
        self.download_directory = download_directory

    def go_to_download(self, url):
        self.driver.get(url)

    def download_file(self, expected_filename):
        wait = WebDriverWait(self.driver, 10)
        download_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/main/header/div[1]/div/div/div[2]/a')
        download_element = wait.until(EC.element_to_be_clickable(download_locator))
        download_element.click()

        file_path = os.path.join(self.download_directory, expected_filename)

        wait = WebDriverWait(self.driver, 500)
        wait.until(lambda driver: os.path.exists(file_path))

        return file_path

    def download_file_get_for_free(self, expected_filename):
        wait = WebDriverWait(self.driver, 10)
        download_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/main/div[5]/div/section/div[2]/div[1]/div[2]/a')
        download_element = wait.until(EC.element_to_be_clickable(download_locator))
        download_element.click()

        file_path = os.path.join(self.download_directory, expected_filename)

        wait = WebDriverWait(self.driver, 500)
        wait.until(lambda driver: os.path.exists(file_path))

        return file_path
