import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, browser):
        self.driver = browser

    def go_to(self):
        pass

    def find_elements_why_vpn_wats_is_vpn(self, expected_title):
        # find why_vpn_locator & click
        wait = WebDriverWait(self.driver, 10)
        why_vpn_locator = (By.CSS_SELECTOR,
                           '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(1) > div > div')
        why_vpn_element = wait.until(EC.presence_of_element_located(why_vpn_locator))
        why_vpn_element.click()

        # find what_is_vpn locator & click
        what_is_vpn_locator = (By.LINK_TEXT, 'What is a VPN?')
        what_is_vpn_element = wait.until(EC.visibility_of_element_located(what_is_vpn_locator))
        what_is_vpn_element.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False


    def find_elements_why_vpn_no_logs(self, expected_title):
        # find why_vpn_locator & click
        wait = WebDriverWait(self.driver, 10)
        why_vpn_locator = (By.CSS_SELECTOR,
                           '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(1) > div > div')
        why_vpn_element = wait.until(EC.presence_of_element_located(why_vpn_locator))
        why_vpn_element.click()

        # find no_logs_locator & click
        no_logs_locator = (By.LINK_TEXT, 'No logs')
        no_logs_element = wait.until(EC.visibility_of_element_located(no_logs_locator))
        no_logs_element.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_why_vpn_what_is_proxy(self, expected_title):
        # find why_vpn_locator & click
        wait = WebDriverWait(self.driver, 10)
        why_vpn_locator = (By.CSS_SELECTOR,
                           '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(1) > div > div')
        why_vpn_element = wait.until(EC.visibility_of_element_located(why_vpn_locator))
        why_vpn_element.click()

        # find what_is_proxy locator & click
        what_is_proxy_locator = (By.LINK_TEXT, 'What is Proxy')
        what_is_proxy_element = wait.until(EC.visibility_of_element_located(what_is_proxy_locator))
        what_is_proxy_element.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_why_vpn_our_vpn_network(self, expected_title):
        # find why_vpn_locator & click
        wait = WebDriverWait(self.driver, 10)
        why_vpn_locator = (By.CSS_SELECTOR,
                           '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(1) > div > div')
        why_vpn_element = wait.until(EC.presence_of_element_located(why_vpn_locator))
        why_vpn_element.click()

        # find our_vpn_network locator & click
        our_vpn_network_locator = (By.LINK_TEXT, 'Our VPN network')
        our_vpn_network_element = wait.until(EC.visibility_of_element_located(our_vpn_network_locator))
        our_vpn_network_element.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elemets_why_vpn_about_vpn_protocols(self, expected_title):
        # find why_vpn_locator & click
        wait = WebDriverWait(self.driver, 10)
        why_vpn_locator = (By.CSS_SELECTOR,
                           '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(1) > div > div')
        why_vpn_element = wait.until(EC.presence_of_element_located(why_vpn_locator))
        why_vpn_element.click()

        # find about_vpn_protocols locator & click
        about_vpn_locator = (By.LINK_TEXT, 'About VPN protocols')
        about_vpn_element = wait.until(EC.presence_of_element_located(about_vpn_locator))
        about_vpn_element.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_why_vpn_free_vpn(self, expected_title):
        # find why_vpn_locator & click
        wait = WebDriverWait(self.driver, 10)
        why_vpn_locator = (By.CSS_SELECTOR,
                           '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(1) > div > div')
        why_vpn_element = wait.until(EC.presence_of_element_located(why_vpn_locator))
        why_vpn_element.click()

        # find free_vpn locator & click
        free_vpn_locator = (By.LINK_TEXT, 'Free VPN')
        free_vpn_element = wait.until(EC.visibility_of_element_located(free_vpn_locator))
        free_vpn_element.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_why_vpn_close_pop_up(self):
        # find why_vpn_locator & click
        wait = WebDriverWait(self.driver, 10)
        why_vpn_locator = (By.CSS_SELECTOR,
                           '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(1) > div > div')
        why_vpn_element = wait.until(EC.presence_of_element_located(why_vpn_locator))
        why_vpn_element.click()

        # find close image locator & click
        close_pop_up_locator = (By.CLASS_NAME, 'nav-submenu__close')
        close_pop_up_element = wait.until(EC.visibility_of_element_located(close_pop_up_locator))
        close_pop_up_element.click()

        is_pop_up_closed = wait.until(EC.invisibility_of_element_located(close_pop_up_locator))

        return is_pop_up_closed

    def find_elements_advantages_access_pop_up(self, expected_title):
        # find advantages locator & click
        wait = WebDriverWait(self.driver, 10)
        advantages_locator = (
            By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[1]/div[2]/nav/div[2]/div[2]/div/div')
        advantages_element = wait.until(EC.visibility_of_element_located(advantages_locator))
        advantages_element.click()

        # find access_to_games locator & click
        access_locator = (By.LINK_TEXT, 'Access to games and movies')
        access_element = wait.until(EC.visibility_of_element_located(access_locator))
        access_element.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_advantages_steam(self, expected_title):
        # find advantages locator & click
        wait = WebDriverWait(self.driver, 10)
        advantages_locator = (
            By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[1]/div[2]/nav/div[2]/div[2]/div/div')
        advantages_element = wait.until(EC.visibility_of_element_located(advantages_locator))
        advantages_element.click()

        # find steam locator & click
        steam_locator = (By.LINK_TEXT, 'Steam')
        steam_element = wait.until(EC.visibility_of_element_located(steam_locator))
        steam_element.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_advantages_preventing_surveillance(self, expected_title):
        # find advantages locator & click
        wait = WebDriverWait(self.driver, 10)
        advantages_locator = (
            By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[1]/div[2]/nav/div[2]/div[2]/div/div')
        advantages_element = wait.until(EC.visibility_of_element_located(advantages_locator))
        advantages_element.click()

        # find preventing locator & click
        preventing_locator = (By.LINK_TEXT, 'Preventing surveillance')
        preventing_element = wait.until(EC.visibility_of_element_located(preventing_locator))
        preventing_element.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_advantages_secure_wi_fi(self, expected_title):
        # find advantages locator & click
        wait = WebDriverWait(self.driver, 10)
        advantages_locator = (
            By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[1]/div[2]/nav/div[2]/div[2]/div/div')
        advantages_element = wait.until(EC.visibility_of_element_located(advantages_locator))
        advantages_element.click()

        # find secure_wi_fi locator & click
        wi_fi_locator = (By.LINK_TEXT, 'Secure Wi Fi')
        wi_fi_element = wait.until(EC.visibility_of_element_located(wi_fi_locator))
        wi_fi_element.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_advantages_streaming(self, expected_title):
        # find advantages locator & click
        wait = WebDriverWait(self.driver, 10)
        advantages_locator = (
            By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[1]/div[2]/nav/div[2]/div[2]/div/div')
        advantages_element = wait.until(EC.visibility_of_element_located(advantages_locator))
        advantages_element.click()

        # find streaming locator & click
        streaming_locator = (By.LINK_TEXT, 'Streaming')
        streaming_element = wait.until(EC.visibility_of_element_located(streaming_locator))
        streaming_element.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_advantages_airline_tickets(self, expected_title):
        # find advantages locator & click
        wait = WebDriverWait(self.driver, 10)
        advantages_locator = (
            By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[1]/div[2]/nav/div[2]/div[2]/div/div')
        advantages_element = wait.until(EC.visibility_of_element_located(advantages_locator))
        advantages_element.click()

        # find airline locator & click
        air_line_locator = (By.LINK_TEXT, 'Airline Tickets')
        air_line_element = wait.until(EC.visibility_of_element_located(air_line_locator))
        air_line_element.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_advantages_online_anonymity(self, expected_title):
        # find advantages locator & click
        wait = WebDriverWait(self.driver, 10)
        advantages_locator = (
            By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[1]/div[2]/nav/div[2]/div[2]/div/div')
        advantages_element = wait.until(EC.visibility_of_element_located(advantages_locator))
        advantages_element.click()

        # find anonymity locator & click
        anonymity_locator = (By.LINK_TEXT, 'Online Anonymity')
        anonymity_element = wait.until(EC.visibility_of_element_located(anonymity_locator))
        anonymity_element.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_advantages_data_encryption(self, expected_title):
        # find advantages locator & click
        wait = WebDriverWait(self.driver, 10)
        advantages_locator = (
            By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[1]/div[2]/nav/div[2]/div[2]/div/div')
        advantages_element = wait.until(EC.visibility_of_element_located(advantages_locator))
        advantages_element.click()

        # find data locator & click
        data_locator = (By.LINK_TEXT, 'Data encryption')
        data_element = wait.until(EC.visibility_of_element_located(data_locator))
        data_element.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_advantages_music(self, expected_title):
        # find advantages locator & click
        wait = WebDriverWait(self.driver, 10)
        advantages_locator = (
            By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[1]/div[2]/nav/div[2]/div[2]/div/div')
        advantages_element = wait.until(EC.visibility_of_element_located(advantages_locator))
        advantages_element.click()

        # find music locator & click
        music_locator = (By.LINK_TEXT, 'Music')
        music_element = wait.until(EC.visibility_of_element_located(music_locator))
        music_element.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_advantages_booking_hotels(self, expected_title):
        # find advantages locator & click
        wait = WebDriverWait(self.driver, 10)
        advantages_locator = (
            By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[1]/div[2]/nav/div[2]/div[2]/div/div')
        advantages_element = wait.until(EC.visibility_of_element_located(advantages_locator))
        advantages_element.click()

        # find booking locator
        booking_hotels_locator = (By.LINK_TEXT, 'Booking Hotels')
        booking_hotels_element = wait.until(EC.visibility_of_element_located(booking_hotels_locator))
        booking_hotels_element.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_advantages_change_or_hid_ip(self, expected_title):
        # find advantages locator & click
        wait = WebDriverWait(self.driver, 10)
        advantages_locator = (
            By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[1]/div[2]/nav/div[2]/div[2]/div/div')
        advantages_element = wait.until(EC.visibility_of_element_located(advantages_locator))
        advantages_element.click()

        # find hide_ip locator & click
        hide_ip_locator = (By.LINK_TEXT, 'Change or Hide your IP')
        hide_ip_element = wait.until(EC.visibility_of_element_located(hide_ip_locator))
        hide_ip_element.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False
    def find_elements_advantages_car_rentals(self, expected_title):
        # find advantages locator & click
        wait = WebDriverWait(self.driver, 10)
        advantages_locator = (
            By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[1]/div[2]/nav/div[2]/div[2]/div/div')
        advantages_element = wait.until(EC.visibility_of_element_located(advantages_locator))
        advantages_element.click()

        # find car_rentals locator & click
        car_rentals_locator = (By.LINK_TEXT, 'Car Rentals')
        car_rentals_element = wait.until(EC.visibility_of_element_located(car_rentals_locator))
        car_rentals_element.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_advantages_torrents(self, expected_title):
        # find advantages locator & click
        wait = WebDriverWait(self.driver, 10)
        advantages_locator = (
            By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[1]/div[2]/nav/div[2]/div[2]/div/div')
        advantages_element = wait.until(EC.visibility_of_element_located(advantages_locator))
        advantages_element.click()

        # find torrents locator & click
        torrents_locator = (By.LINK_TEXT, 'Torrents')
        torrents_element = wait.until(EC.visibility_of_element_located(torrents_locator))
        torrents_element.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_advantages_close_pop_up(self):
        # find advantages locator & click
        wait = WebDriverWait(self.driver, 10)
        advantages_locator = (
            By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[1]/div[2]/nav/div[2]/div[2]/div/div')
        advantages_element = wait.until(EC.visibility_of_element_located(advantages_locator))
        advantages_element.click()

        # find close pop_up img & click
        close_pop_up_locator = (By.CLASS_NAME, 'nav-submenu__close')
        close_pop_up_element = wait.until(EC.visibility_of_element_located(close_pop_up_locator))
        close_pop_up_element.click()
        is_pop_up_closed = wait.until(EC.invisibility_of_element_located(close_pop_up_locator))

        return is_pop_up_closed

    def find_elements_products_android_pop_up(self, expected_title):
        # find product locator and click
        wait = WebDriverWait(self.driver, 10)
        products_locator = (By.CSS_SELECTOR,
                            '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(3) > div > div')
        products_elements = wait.until(EC.presence_of_element_located(products_locator))
        products_elements.click()
        # find product locator and click
        android_locator = (By.LINK_TEXT, 'Android')
        android_element = wait.until(EC.visibility_of_element_located(android_locator))
        android_element.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_products_chrome_pop_up(self, expected_title):
        # find product locator and click
        wait = WebDriverWait(self.driver, 10)
        products_locator = (By.CSS_SELECTOR,
                            '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(3) > div > div')
        products_elements = wait.until(EC.presence_of_element_located(products_locator))
        products_elements.click()

        # find chrome locator and click
        chrome_locator = (By.LINK_TEXT, 'Chrome')
        chrome_elements = wait.until(EC.presence_of_element_located(chrome_locator))
        chrome_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_products_windows_pop_up(self, expected_title):
        # find product locator and click
        wait = WebDriverWait(self.driver, 10)
        products_locator = (By.CSS_SELECTOR,
                            '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(3) > div > div')
        products_elements = wait.until(EC.presence_of_element_located(products_locator))
        products_elements.click()

        # find windows locator & click
        windows_locator = (By.LINK_TEXT, 'Windows')
        windows_elements = wait.until(EC.visibility_of_element_located(windows_locator))
        windows_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_products_router_pop_up(self, expected_title):
        # find product locator and click
        wait = WebDriverWait(self.driver, 10)
        products_locator = (By.CSS_SELECTOR,
                            '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(3) > div > div')
        products_elements = wait.until(EC.presence_of_element_located(products_locator))
        products_elements.click()

        # find router locator & click
        router_locator = (By.LINK_TEXT, 'Router')
        router_elements = wait.until(EC.visibility_of_element_located(router_locator))
        router_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_dns_leak_pop_up(self, expected_title):
        # find product locator and click
        wait = WebDriverWait(self.driver, 10)
        products_locator = (By.CSS_SELECTOR,
                            '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(3) > div > div')
        products_elements = wait.until(EC.presence_of_element_located(products_locator))
        products_elements.click()

        # find DNS_Leak_Test locator & click
        dns_locator = (By.LINK_TEXT, 'DNS Leak Test')
        dns_elements = wait.until(EC.visibility_of_element_located(dns_locator))
        dns_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_products_ios_pop_up(self, expected_title):
        # find product locator and click
        wait = WebDriverWait(self.driver, 10)
        products_locator = (By.CSS_SELECTOR,
                            '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(3) > div > div')
        products_elements = wait.until(EC.presence_of_element_located(products_locator))
        products_elements.click()

        # find ios locator and click
        ios_locator = (By.LINK_TEXT, 'iOS')
        ios_elements = wait.until(EC.visibility_of_element_located(ios_locator))
        ios_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_products_firefox_po_up(self, expected_title):
        # find product locator and click
        wait = WebDriverWait(self.driver, 10)
        products_locator = (By.CSS_SELECTOR,
                            '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(3) > div > div')
        products_elements = wait.until(EC.presence_of_element_located(products_locator))
        products_elements.click()

        # find firefox locator & click
        firefox_locator = (By.LINK_TEXT, 'Firefox')
        firefox_elements = wait.until(EC.visibility_of_element_located(firefox_locator))
        firefox_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_products_macos_pop_up(self, expected_title):
        # find product locator and click
        wait = WebDriverWait(self.driver, 10)
        products_locator = (By.CSS_SELECTOR,
                            '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(3) > div > div')
        products_elements = wait.until(EC.presence_of_element_located(products_locator))
        products_elements.click()

        # find macOS locator & click
        macos_locator = (By.LINK_TEXT, 'macOS')
        macos_elements = wait.until(EC.visibility_of_element_located(macos_locator))
        macos_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_products_open_vpn_pop_up(self, expected_title):
        # find product locator and click
        wait = WebDriverWait(self.driver, 10)
        products_locator = (By.CSS_SELECTOR,
                            '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(3) > div > div')
        products_elements = wait.until(EC.presence_of_element_located(products_locator))
        products_elements.click()

        # find open_vpn locator & click
        open_vpn_locator = (By.LINK_TEXT, 'OpenVPN')
        open_vpn_elements = wait.until(EC.visibility_of_element_located(open_vpn_locator))
        open_vpn_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_products_web_rtc_pop_up(self, expected_title):
        # find product locator and click
        wait = WebDriverWait(self.driver, 10)
        products_locator = (By.CSS_SELECTOR,
                            '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(3) > div > div')
        products_elements = wait.until(EC.presence_of_element_located(products_locator))
        products_elements.click()

        # find webRTC locator & click
        web_rtc_locator = (By.LINK_TEXT, 'WebRTC Leak Test')
        web_rtc_elements = wait.until(EC.visibility_of_element_located(web_rtc_locator))
        web_rtc_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_products_edge(self, expected_title):
        # find product locator and click
        wait = WebDriverWait(self.driver, 10)
        products_locator = (By.CSS_SELECTOR,
                            '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(3) > div > div')
        products_elements = wait.until(EC.presence_of_element_located(products_locator))
        products_elements.click()

        # find edge locator & click
        edges_locator = (By.LINK_TEXT, 'Edge')
        edges_elements = wait.until(EC.visibility_of_element_located(edges_locator))
        edges_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_products_linux(self, expected_title):
        # find product locator and click
        wait = WebDriverWait(self.driver, 10)
        products_locator = (By.CSS_SELECTOR,
                            '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(3) > div > div')
        products_elements = wait.until(EC.presence_of_element_located(products_locator))
        products_elements.click()

        # find linux locator & click

        linux_locator = (By.LINK_TEXT, 'Linux')
        linux_elements = wait.until(EC.visibility_of_element_located(linux_locator))
        linux_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_products_virus_scan_pop_up(self, expected_title):
        # find product locator and click
        wait = WebDriverWait(self.driver, 10)
        products_locator = (By.CSS_SELECTOR,
                            '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(3) > div > div')
        products_elements = wait.until(EC.presence_of_element_located(products_locator))
        products_elements.click()

        # find virus_scan locator & click
        virus_scan_locator = (By.LINK_TEXT, 'Virus scan')
        virus_scan_elements = wait.until(EC.visibility_of_element_located(virus_scan_locator))
        virus_scan_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_products_opera_pop_up(self, expected_title):
        # find product locator and click
        wait = WebDriverWait(self.driver, 10)
        products_locator = (By.CSS_SELECTOR,
                            '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(3) > div > div')
        products_elements = wait.until(EC.presence_of_element_located(products_locator))
        products_elements.click()

        # find opera_locator & click
        opera_locator = (By.LINK_TEXT, 'Opera')
        opera_elements = wait.until(EC.visibility_of_element_located(opera_locator))
        opera_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_products_what_is_my_ip_pop_up(self, expected_title):
        # find product locator and click
        wait = WebDriverWait(self.driver, 10)
        products_locator = (By.CSS_SELECTOR,
                            '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(3) > div > div')
        products_elements = wait.until(EC.presence_of_element_located(products_locator))
        products_elements.click()

        # find what_is_my_ip locator & click
        what_is_my_locator = (By.LINK_TEXT, 'What is my IP?')
        what_is_my_elements = wait.until(EC.visibility_of_element_located(what_is_my_locator))
        what_is_my_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_product_yandex_pop_up(self, expected_title):
        # find product locator and click
        wait = WebDriverWait(self.driver, 10)
        products_locator = (By.CSS_SELECTOR,
                            '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(3) > div > div')
        products_elements = wait.until(EC.presence_of_element_located(products_locator))
        products_elements.click()

        # find yandex locator & click
        yandex_locator = (By.LINK_TEXT, 'Yandex')
        yandex_elements = wait.until(EC.visibility_of_element_located(yandex_locator))
        yandex_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

    def find_elements_products_password_generator_pop_up(self, expected_title):
        # find product locator and click
        wait = WebDriverWait(self.driver, 10)
        products_locator = (By.CSS_SELECTOR,
                            '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(3) > div > div')
        products_elements = wait.until(EC.presence_of_element_located(products_locator))
        products_elements.click()

        # find password_generator locator & click
        password_generator_locator = (By.LINK_TEXT, 'Password generator')
        password_generator_elements = wait.until(EC.visibility_of_element_located(password_generator_locator))
        password_generator_elements.click()

        try:
            wait.until(EC.title_is(expected_title))
            return True
        except TimeoutError:
            return False

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

    def find_elements_premium_button(self):
        # find premium button locator & click
        wait = WebDriverWait(self.driver, 10)
        premium_buttons_locator = (By.LINK_TEXT, 'Premium')
        premium_buttons_elements = wait.until(EC.visibility_of_element_located(premium_buttons_locator))
        premium_buttons_elements.click()

        time.sleep(2)
        return self.driver

    def find_elements_planet_vpn_logo(self):
        # find premium button locator & click
        wait = WebDriverWait(self.driver, 10)
        premium_buttons_locator = (By.LINK_TEXT, 'Premium')
        premium_buttons_elements = wait.until(EC.visibility_of_element_located(premium_buttons_locator))
        premium_buttons_elements.click()
        time.sleep(2)

        # find planet_vpn_logo locator & click
        planet_vpn_logo_locator = (By.CLASS_NAME, 'header-logo__logo')
        planet_vpn_logo_elements = wait.until(EC.visibility_of_element_located(planet_vpn_logo_locator))
        planet_vpn_logo_elements.click()

        time.sleep(2)
        return self.driver

    def find_elements_download_vpn(self):
        # find download locator & click
        wait = WebDriverWait(self.driver, 10)
        download_locator = (By.LINK_TEXT, 'Download VPN')
        download_elements = wait.until(EC.visibility_of_element_located(download_locator))
        download_elements.click()

        time.sleep(2)
        return self.driver

    def find_elements_login(self):
        # find login locator & click
        wait = WebDriverWait(self.driver, 10)
        login_locator = (By.LINK_TEXT, 'Login')
        login_elements = wait.until(EC.visibility_of_element_located(login_locator))
        login_elements.click()

        time.sleep(2)
        return self.driver

    def find_elements_localizations_pt(self):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find pt locator & click
        pt_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[10]')
        pt_elements = wait.until(EC.visibility_of_element_located(pt_locator))
        pt_elements.click()

        time.sleep(2)
        return self.driver

    def find_elements_localizations_ro(self):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find ro locator & click
        ro_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[11]')
        ro_elements = wait.until(EC.visibility_of_element_located(ro_locator))
        ro_elements.click()

        time.sleep(2)
        return self.driver

    def find_elements_localizations_ru(self):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find ru locator & click
        ru_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[12]')
        ru_elements = wait.until(EC.visibility_of_element_located(ru_locator))
        ru_elements.click()

        time.sleep(2)
        return self.driver

    def find_elements_localizations_sv(self):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find sv locator & click
        sv_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[13]')
        sv_elements = wait.until(EC.visibility_of_element_located(sv_locator))
        sv_elements.click()

        time.sleep(2)
        return self.driver

    def find_elements_localizations_th(self):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find th locator & click
        th_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[14]')
        th_elements = wait.until(EC.visibility_of_element_located(th_locator))
        th_elements.click()

        time.sleep(2)
        return self.driver

    def find_elements_localizations_tl(self):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find tl locator & click
        tl_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[15]')
        tl_elements = wait.until(EC.visibility_of_element_located(tl_locator))
        tl_elements.click()

        time.sleep(2)
        return self.driver

    def find_elements_localizations_tr(self):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find tr_ locator & click
        tr_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[16]')
        tr_elements = wait.until(EC.visibility_of_element_located(tr_locator))
        tr_elements.click()

        time.sleep(2)
        return self.driver

    def find_elements_localizations_ua(self):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find ua locator & click
        ua_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[17]')
        ua_elements = wait.until(EC.visibility_of_element_located(ua_locator))
        ua_elements.click()

        time.sleep(2)
        return self.driver

    def find_elements_localizations_ar(self):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find ar locator & click
        ar_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[1]')
        ar_elements = wait.until(EC.visibility_of_element_located(ar_locator))
        ar_elements.click()

        time.sleep(2)
        return self.driver

    def find_elements_localizations_cs(self):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find cs locator & click
        cs_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[2]')
        cs_elements = wait.until(EC.visibility_of_element_located(cs_locator))
        cs_elements.click()

        time.sleep(2)
        return self.driver

    def find_elements_localizations_de(self):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find de locator & click
        de_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[3]')
        de_elements = wait.until(EC.visibility_of_element_located(de_locator))
        de_elements.click()

        time.sleep(2)
        return self.driver

    def find_elements_localizations_en(self):
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

        time.sleep(2)
        return self.driver

    def find_elements_localizations_es(self):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find es locator & click
        es_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[5]')
        es_elements = wait.until(EC.visibility_of_element_located(es_locator))
        es_elements.click()

        time.sleep(2)
        return self.driver

    def find_elements_localizations_fr(self):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find fr_ locator & click
        fr_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[6]')
        fr_elements = wait.until(EC.visibility_of_element_located(fr_locator))
        fr_elements.click()

        time.sleep(2)
        return self.driver

    def find_elements_localizations_id(self):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find id locator & click
        id_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[7]')
        id_elements = wait.until(EC.visibility_of_element_located(id_locator))
        id_elements.click()

        time.sleep(2)
        return self.driver

    def find_elements_localizations_it(self):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find it locator & click
        it_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[8]')
        it_elements = wait.until(EC.visibility_of_element_located(it_locator))
        it_elements.click()

        time.sleep(2)
        return self.driver

    def find_elements_localizations_pl(self):
        # find localizations locator & click
        wait = WebDriverWait(self.driver, 10)
        localisation_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[1]')
        localisation_elements = wait.until(EC.visibility_of_element_located(localisation_locator))
        localisation_elements.click()

        # find pl locator & click
        pl_locator = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[9]')
        pl_elements = wait.until(EC.visibility_of_element_located(pl_locator))
        pl_elements.click()

        time.sleep(2)
        return self.driver
