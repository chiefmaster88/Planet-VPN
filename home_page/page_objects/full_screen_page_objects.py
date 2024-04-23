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
        # s = lambda x: self.driver.execute_script('return document.body.parentNode.scroll' + x)
        # self.driver.set_window_size(s('Width'), s('Height'))
        # self.driver.find_element(By.TAG_NAME, 'body')

        self.driver.set_window_size(width, height)

        self.driver.save_screenshot(filepath)
        return filepath
