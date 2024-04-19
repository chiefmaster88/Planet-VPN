import os
import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FooterPageObjects:
    url = 'https://freevpnplanet.com/'

    def __init__(self, browser):
        self.driver = browser

    def go_to(self):
        pass

    def go_back(self):
        self.driver.get(FooterPageObjects.url)

    def find_footer_links(self, expected_title):
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        wait = WebDriverWait(self.driver, 10)
        cookies_locator = (By.CLASS_NAME, 'cookies__btn')
        cookies_element = wait.until(EC.element_to_be_clickable(cookies_locator))
        cookies_element.click()

        proxy_locator = (By.LINK_TEXT, 'What is Proxy')
        proxy_element = wait.until(EC.element_to_be_clickable(proxy_locator))
        proxy_element.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutException:
            return False

    # def find_footer_pop_support(self):
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #
    #     wait = WebDriverWait(self.driver, 10)
    #     cookies_locator = (By.CLASS_NAME, 'cookies__btn')
    #     cookies_element = wait.until(EC.element_to_be_clickable(cookies_locator))
    #     cookies_element.click()
    #
    #     support_locator = (By.LINK_TEXT, 'Support 24/7')
    #     support_element = wait.until(EC.element_to_be_clickable(support_locator))
    #     support_element.click()
    #
    # def find_footer_pop_up_chat(self):
    #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #
    #     wait = WebDriverWait(self.driver, 10)
    #     cookies_locator = (By.CLASS_NAME, 'cookies__btn')
    #     cookies_element = wait.until(EC.element_to_be_clickable(cookies_locator))
    #     cookies_element.click()
    #
    #     chat_locator = (By.XPATH, '//*[@id="Embed"]/div/div/button')
    #     chat_element = wait.until(EC.element_to_be_clickable(chat_locator))
    #     chat_element.click()
    #


class FooterPageDownloads:

    def __init__(self, browser_and_download, download_directory):
        self.driver = browser_and_download
        self.download_directory = download_directory

    def go_to(self, url):
        self.driver.get(url)

    def find_element_download_windows(self, expected_filename):
        wait = WebDriverWait(self.driver, 10)
        cookies_locator = (By.CLASS_NAME, 'cookies__btn')
        cookies_element = wait.until(EC.element_to_be_clickable(cookies_locator))
        cookies_element.click()

        download_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/footer/div/div/div/div[2]/div/a[2]')
        download_element = wait.until(EC.element_to_be_clickable(download_locator))
        download_element.click()

        file_path = os.path.join(self.download_directory, expected_filename)

        wait = WebDriverWait(self.driver, 500)
        wait.until(lambda driver: os.path.exists(file_path))

        return file_path

    def find_element_download_macOS(self, expected_filename):
        wait = WebDriverWait(self.driver, 10)
        cookies_locator = (By.CLASS_NAME, 'cookies__btn')
        cookies_element = wait.until(EC.element_to_be_clickable(cookies_locator))
        cookies_element.click()

        download_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/footer/div/div/div/div[2]/div/a[5]')
        download_element = wait.until(EC.element_to_be_clickable(download_locator))
        download_element.click()

        file_path = os.path.join(self.download_directory, expected_filename)

        wait = WebDriverWait(self.driver, 500)
        wait.until(lambda driver: os.path.exists(file_path))

        return file_path
