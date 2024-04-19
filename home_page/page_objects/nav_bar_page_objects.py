from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    url = 'https://freevpnplanet.com/'

    def __init__(self, browser):
        self.driver = browser

    def go_to(self):
        pass

    def find_elements_why_vpn_wats_is_vpn(self, expected_title):
        # find why_vpn_locator & click
        wait = WebDriverWait(self.driver, 10)
        cookies_locator = (By.CLASS_NAME, 'cookies__btn')
        cookies_element = wait.until(EC.element_to_be_clickable(cookies_locator))
        cookies_element.click()
        why_vpn_locator = (By.CSS_SELECTOR,
                           '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(1) > div')
        why_vpn_element = wait.until(EC.element_to_be_clickable(why_vpn_locator))
        why_vpn_element.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutException:
            return False

    def find_button_why_and_click(self):
        # find why_vpn_locator & click
        wait = WebDriverWait(self.driver, 10)
        why_vpn_locator = (By.CSS_SELECTOR,
                           '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(1) > div')
        why_vpn_element = wait.until(EC.element_to_be_clickable(why_vpn_locator))
        why_vpn_element.click()
        return self.driver

    def go_back(self):
        self.driver.get(HomePage.url)

    def find_element_close_pop_up(self):
        # find advantages locator & click
        wait = WebDriverWait(self.driver, 10)
        advantages_locator = (
            By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[1]/div[2]/nav/div[2]/div[2]/div/div')
        advantages_element = wait.until(EC.element_to_be_clickable(advantages_locator))
        advantages_element.click()

        # find close pop_up img & click
        close_pop_up_locator = (By.CLASS_NAME, 'nav-submenu__close')
        close_pop_up_element = wait.until(EC.element_to_be_clickable(close_pop_up_locator))
        close_pop_up_element.click()
        is_pop_up_closed = wait.until(EC.invisibility_of_element_located(close_pop_up_locator))

        return is_pop_up_closed

    def find_elements_advantages_access_pop_up(self, expected_title):
        # find advantages locator & click

        wait = WebDriverWait(self.driver, 10)
        cookies_locator = (By.CLASS_NAME, 'cookies__btn')
        cookies_element = wait.until(EC.element_to_be_clickable(cookies_locator))
        cookies_element.click()
        advantages_locator = (
            By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[1]/div[2]/nav/div[2]/div[2]/div/div')
        advantages_element = wait.until(EC.element_to_be_clickable(advantages_locator))
        advantages_element.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_advantages_button_and_click(self):
        wait = WebDriverWait(self.driver, 10)

        advantages_locator = (
            By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[1]/div[2]/nav/div[2]/div[2]/div/div')
        advantages_element = wait.until(EC.element_to_be_clickable(advantages_locator))
        advantages_element.click()
        return self.driver

    def find_elements_products_android_pop_up(self, expected_title):
        # find product locator and click
        wait = WebDriverWait(self.driver, 10)
        cookies_locator = (By.CLASS_NAME, 'cookies__btn')
        cookies_element = wait.until(EC.element_to_be_clickable(cookies_locator))
        cookies_element.click()
        products_locator = (By.CSS_SELECTOR,
                            '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(3) > div > div')
        products_elements = wait.until(EC.presence_of_element_located(products_locator))
        products_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_products_button_and_click(self):
        wait = WebDriverWait(self.driver, 10)
        products_locator = (By.CSS_SELECTOR,
                            '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(3) > div > div')
        products_elements = wait.until(EC.presence_of_element_located(products_locator))
        products_elements.click()
        return self.driver

    def find_elements_premium_and_login_and_logo_buttons(self, expected_title):
        # find premium button locator & click
        wait = WebDriverWait(self.driver, 10)
        premium_buttons_locator = (By.LINK_TEXT, 'Premium')
        premium_buttons_elements = wait.until(EC.visibility_of_element_located(premium_buttons_locator))
        premium_buttons_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_download_vpn(self, expected_title):
        # find download locator & click
        wait = WebDriverWait(self.driver, 10)
        download_locator = (By.LINK_TEXT, 'Download VPN')
        download_elements = wait.until(EC.visibility_of_element_located(download_locator))
        download_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_localizations_pt(self, expected_title):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_english_element_and_click(self):
        wait = WebDriverWait(self.driver, 10)
        english_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        english_elements = wait.until(EC.visibility_of_element_located(english_locator))
        english_elements.click()
