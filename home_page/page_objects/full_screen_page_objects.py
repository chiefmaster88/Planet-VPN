import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class PageObject:
    def __init__(self, driver):
        self.driver = driver

    def go_to(self, url):
        self.driver.get(url)

    def take_full_page_screenshot(self, filename, directory):
        wait = WebDriverWait(self.driver, 10)

        filepath = os.path.join(directory, filename)

        width = self.driver.execute_script("return document.body.scrollWidth")
        height = self.driver.execute_script("return document.body.scrollHeight")

        self.driver.set_window_size(width, height)

        self.driver.save_screenshot(filepath)
        return filepath
