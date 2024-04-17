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
        # cookies_locator = (By.CLASS_NAME, 'cookies__btn')
        # cookies_element = wait.until(EC.element_to_be_clickable(cookies_locator))
        # cookies_element.click()

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

    def find_dropdown_menu(self, dropdown_locator):
        # find cookies & close
        wait = WebDriverWait(self.driver, 10)
        cookies_locator = (By.CLASS_NAME, 'cookies__btn')
        cookies_element = wait.until(EC.element_to_be_clickable(cookies_locator))
        cookies_element.click()
        self.driver.execute_script("window.scrollBy(0, 6500);")
        time.sleep(10)

        wait = WebDriverWait(self.driver, 10)
        dropdown_menus = wait.until(EC.presence_of_all_elements_located(dropdown_locator))
        return dropdown_menus

    def click_and_verify_dropdown_text(self, dropdown_menus, menu_text_locators):

        wait = WebDriverWait(self.driver, 10)
        for menu, (menu_text_locator, expected_text) in zip(dropdown_menus, menu_text_locators):
            menu.click()

            text_element = wait.until(EC.visibility_of_element_located(menu_text_locator))

            assert text_element.text == expected_text, f"Ожидаемый текст не совпадает: {expected_text} != {text_element.text}"

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
