import time

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

    def find_elements_product_close_pop_up(self):
        # find product locator and click
        wait = WebDriverWait(self.driver, 10)
        products_locator = (By.CSS_SELECTOR,
                            '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(3) > div > div')
        products_elements = wait.until(EC.presence_of_element_located(products_locator))
        products_elements.click()

        # find close pop_up button & click
        close_pop_up_locator = (By.CLASS_NAME, 'nav-submenu__close')
        close_pop_up_elements = wait.until(EC.visibility_of_element_located(close_pop_up_locator))
        close_pop_up_elements.click()

        close_pop_up = wait.until(EC.invisibility_of_element_located(close_pop_up_elements))

        return close_pop_up

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

    def find_elements_login(self, expected_title):
        # find login locator & click
        wait = WebDriverWait(self.driver, 10)
        login_locator = (By.LINK_TEXT, 'Login')
        login_elements = wait.until(EC.visibility_of_element_located(login_locator))
        login_elements.click()

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

        # find pt locator & click
        pt_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[10]')
        pt_elements = wait.until(EC.visibility_of_element_located(pt_locator))
        pt_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_localizations_ro(self, expected_title):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find ro locator & click
        ro_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[11]')
        ro_elements = wait.until(EC.visibility_of_element_located(ro_locator))
        ro_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_localizations_ru(self, expected_title):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find ru locator & click
        ru_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[12]')
        ru_elements = wait.until(EC.visibility_of_element_located(ru_locator))
        ru_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_localizations_sv(self, expected_title):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find sv locator & click
        sv_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[13]')
        sv_elements = wait.until(EC.visibility_of_element_located(sv_locator))
        sv_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_localizations_th(self, expected_title):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find th locator & click
        th_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[14]')
        th_elements = wait.until(EC.visibility_of_element_located(th_locator))
        th_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_localizations_tl(self, expected_title):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find tl locator & click
        tl_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[15]')
        tl_elements = wait.until(EC.visibility_of_element_located(tl_locator))
        tl_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_localizations_tr(self, expected_title):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find tr_ locator & click
        tr_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[16]')
        tr_elements = wait.until(EC.visibility_of_element_located(tr_locator))
        tr_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_localizations_ua(self, expected_title):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find ua locator & click
        ua_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[17]')
        ua_elements = wait.until(EC.visibility_of_element_located(ua_locator))
        ua_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_localizations_ar(self, expected_title):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find ar locator & click
        ar_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[1]')
        ar_elements = wait.until(EC.visibility_of_element_located(ar_locator))
        ar_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_localizations_cs(self, expected_title):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find cs locator & click
        cs_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[2]')
        cs_elements = wait.until(EC.visibility_of_element_located(cs_locator))
        cs_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_localizations_de(self, expected_title):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find de locator & click
        de_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[3]')
        de_elements = wait.until(EC.visibility_of_element_located(de_locator))
        de_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_localizations_en(self, expected_title):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find de locator & click
        de_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[3]')
        de_elements = wait.until(EC.visibility_of_element_located(de_locator))
        de_elements.click()

        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find en locator & click
        en_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[4]')
        en_elements = wait.until(EC.visibility_of_element_located(en_locator))
        en_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_localizations_es(self, expected_title):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find es locator & click
        es_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[5]')
        es_elements = wait.until(EC.visibility_of_element_located(es_locator))
        es_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_localizations_fr(self, expected_title):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find fr_ locator & click
        fr_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[6]')
        fr_elements = wait.until(EC.visibility_of_element_located(fr_locator))
        fr_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_localizations_id(self, expected_title):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find id locator & click
        id_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[7]')
        id_elements = wait.until(EC.visibility_of_element_located(id_locator))
        id_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_localizations_it(self, expected_title):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find it locator & click
        it_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[8]')
        it_elements = wait.until(EC.visibility_of_element_located(it_locator))
        it_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_localizations_pl(self, expected_title):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find pl locator & click
        pl_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[9]')
        pl_elements = wait.until(EC.visibility_of_element_located(pl_locator))
        pl_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False
