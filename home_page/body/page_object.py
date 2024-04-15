from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageObject:
    def __init__(self, browser):
        self.driver = browser

    def go_to(self):
       pass




    def fid_element_download_vpn(self, expected_title, timeout=10):
        # Создаем ожидание с указанным таймаутом
        wait = WebDriverWait(self.driver, timeout)
        download_locator = (By.LINK_TEXT, 'Download VPN')
        download_element = wait.until(EC.presence_of_element_located(download_locator))
        download_element.click()


        # Ожидаем, что заголовок страницы будет равен ожидаемому
        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False
