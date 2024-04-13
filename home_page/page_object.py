import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    url = 'https://freevpnplanet.com/'

    def __init__(self, browser):
        self.driver = browser

    def go_to(self):
        self.driver.get(HomePage.url)

    def find_elements_why_vpn_wats_is_vpn(self):
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
        time.sleep(2)

        # find h1 what_is_vpn
        h1_locator = (By.CSS_SELECTOR, 'h1')
        h1_element = wait.until(EC.visibility_of_element_located(h1_locator))

        return h1_element

    def find_elements_why_vpn_no_logs(self):
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
        time.sleep(2)

        # find h1 no_logs
        h1_locator = (By.CSS_SELECTOR, 'h1')
        h1_nologs_element = wait.until(EC.visibility_of_element_located(h1_locator))

        return h1_nologs_element

    def find_elements_why_vpn_what_is_proxy(self):
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
        time.sleep(2)

        # find h1 what_is_proxy
        h1_locator = (By.TAG_NAME, 'h1')
        h1_element = wait.until(EC.visibility_of_element_located(h1_locator))
        return h1_element

    def find_elements_why_vpn_our_vpn_network(self):
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
        time.sleep(2)

        # find h1 our_vpn_network

        h1_locator = (By.TAG_NAME, 'h1')
        h1_element = wait.until(EC.visibility_of_element_located(h1_locator))

        return h1_element

    def find_elemets_why_vpn_about_vpn_protocols(self):
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
        time.sleep(2)


        # find h1 about_vpn_protocols
        h1_locator = (By.TAG_NAME, 'h1')
        h1_element = wait.until(EC.visibility_of_element_located(h1_locator))

        return h1_element

    def find_elements_why_vpn_free_vpn(self):
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
        time.sleep(2)

        # find h1 free_vpn
        h1_locator = (By.TAG_NAME, 'h1')
        h1_element = wait.until(EC.visibility_of_element_located(h1_locator))

        return h1_element

    def find_elements_why_vpn_close_pop_up(self):
        # find why_vpn_locator & click
        wait = WebDriverWait(self.driver, 10)
        why_vpn_locator = (By.CSS_SELECTOR,
                           '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(1) > div > div')
        why_vpn_element = wait.until(EC.presence_of_element_located(why_vpn_locator))
        why_vpn_element.click()

        # find close image locator & click
        close_pop_up_locator = (By.CSS_SELECTOR,
                                '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div.nav-menu-item.expanded > div.nav-menu-item__submenu.about > div > button > img')
        close_pop_up_element = wait.until(EC.visibility_of_element_located(close_pop_up_locator))
        close_pop_up_element.click()

        is_pop_up_closed = wait.until(EC.invisibility_of_element_located(close_pop_up_locator))

        return is_pop_up_closed

    def find_elements_advantages_access(self):
        advantages = self.driver.find_element(By.CSS_SELECTOR,
                                              '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(2) > div > div')
        advantages.click()
        time.sleep(2)
        # find access_to_games button
        access_to_games = self.driver.find_element(By.LINK_TEXT, 'Access to games and movies')
        access_to_games.click()
        time.sleep(2)
        # find h1
        h1_element = self.driver.find_element(By.TAG_NAME, 'h1')

        return h1_element

    def find_elements_advantages_steam(self):
        advantages = self.driver.find_element(By.CSS_SELECTOR,
                                              '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(2) > div > div')
        advantages.click()
        time.sleep(2)
        steam_element = self.driver.find_element(By.LINK_TEXT, 'Steam')
        steam_element.click()
        time.sleep(2)

        # find h1_steam
        h1_steam = self.driver.find_element(By.TAG_NAME, 'h1')

        return h1_steam

    def find_elements_advantages_preventing_surveillance(self):
        advantages = self.driver.find_element(By.CSS_SELECTOR,
                                              '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(2) > div > div')
        advantages.click()
        time.sleep(2)
        # find preventing_surveillance button
        prevent_surveillance = self.driver.find_element(By.LINK_TEXT, 'Preventing surveillance')
        prevent_surveillance.click()
        time.sleep(2)
        # find h1 preventing_surveillance button
        h1_preventing_surveillance = self.driver.find_element(By.TAG_NAME, 'h1')
        return h1_preventing_surveillance

    def find_elements_advantages_secure_wi_fi(self):
        advantages = self.driver.find_element(By.CSS_SELECTOR,
                                              '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(2) > div > div')
        advantages.click()
        time.sleep(2)
        # find secur_wi_fi button
        secure_wi_fi = self.driver.find_element(By.LINK_TEXT, 'Secure Wi Fi')
        secure_wi_fi.click()
        time.sleep(2)
        # find h1 secure wi_fi
        h1_secure_wi_fi = self.driver.find_element(By.TAG_NAME, 'h1')
        return h1_secure_wi_fi

    def find_elements_advantages_streaming(self):
        advantages = self.driver.find_element(By.CSS_SELECTOR,
                                              '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(2) > div > div')
        advantages.click()
        time.sleep(2)
        # find streaming button
        streaming = self.driver.find_element(By.LINK_TEXT, 'Streaming')
        streaming.click()
        time.sleep(2)
        # find h1 streaming
        h1_streaming = self.driver.find_element(By.TAG_NAME, 'h1')
        return h1_streaming

    def find_elements_advantages_airline_tickets(self):
        advantages = self.driver.find_element(By.CSS_SELECTOR,
                                              '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(2) > div > div')
        advantages.click()
        time.sleep(2)
        # find airline_tickets button
        airline_tickets = self.driver.find_element(By.LINK_TEXT, 'Airline Tickets')
        airline_tickets.click()
        time.sleep(2)
        # find h1 airline_tickets_button
        h1_airline_tickets = self.driver.find_element(By.TAG_NAME, 'h1')
        return h1_airline_tickets

    def find_elements_advantages_online_anonymity(self):
        advantages = self.driver.find_element(By.CSS_SELECTOR,
                                              '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(2) > div > div')
        advantages.click()
        time.sleep(2)
        # find online_anonymity button
        online_anonymity = self.driver.find_element(By.LINK_TEXT, 'Online Anonymity')
        online_anonymity.click()
        time.sleep(2)
        # find h1 online_anonymity
        h1_online_anonymity = self.driver.find_element(By.TAG_NAME, 'h1')
        return h1_online_anonymity

    def find_elements_advantages_data_encryption(self):
        advantages = self.driver.find_element(By.CSS_SELECTOR,
                                              '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(2) > div > div')
        advantages.click()
        time.sleep(2)
        # find data_encryption button
        data_encryption = self.driver.find_element(By.LINK_TEXT, 'Data encryption')
        data_encryption.click()
        time.sleep(2)
        # find h1 data_encryption
        h1_data_encryption = self.driver.find_element(By.TAG_NAME, 'h1')
        return h1_data_encryption

    def find_elements_avantages_music(self):
        advantages = self.driver.find_element(By.CSS_SELECTOR,
                                              '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(2) > div > div')
        advantages.click()
        time.sleep(2)
        # find music button
        music = self.driver.find_element(By.LINK_TEXT, 'Music')
        music.click()
        time.sleep(2)
        # find h1_music
        h1_music = self.driver.find_element(By.TAG_NAME, 'h1')
        return h1_music

    def find_elements_advantages_booking_hotels(self):
        advantages = self.driver.find_element(By.CSS_SELECTOR,
                                              '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(2) > div > div')
        advantages.click()
        time.sleep(2)
        # find booking_hotels button
        booking_hotels = self.driver.find_element(By.LINK_TEXT, 'Booking Hotels')
        booking_hotels.click()
        time.sleep(2)
        # find h1 booking_hotels
        h1_booking_hotels = self.driver.find_element(By.TAG_NAME, 'h1')
        return h1_booking_hotels

    def find_elements_advantages_change_or_hid_ip(self):
        advantages = self.driver.find_element(By.CSS_SELECTOR,
                                              '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(2) > div > div')
        advantages.click()
        time.sleep(2)
        # find change_or_hid_ip button
        change_or_hid_ip = self.driver.find_element(By.LINK_TEXT, 'Change or Hide your IP')
        change_or_hid_ip.click()
        time.sleep(2)
        # find h1 change_or_gide_ip
        h1_change_or_hid_ip = self.driver.find_element(By.TAG_NAME, 'h1')
        return h1_change_or_hid_ip

    def find_elements_advantages_car_rentals(self):
        advantages = self.driver.find_element(By.CSS_SELECTOR,
                                              '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(2) > div > div')
        advantages.click()
        time.sleep(2)
        # find car_rentals button
        car_rentals = self.driver.find_element(By.LINK_TEXT, 'Car Rentals')
        car_rentals.click()
        time.sleep(2)
        # find h1 car_rentals
        h1_car_rentals = self.driver.find_element(By.TAG_NAME, 'h1')
        return h1_car_rentals

    def find_elements_advantages_torrents(self):
        advantages = self.driver.find_element(By.CSS_SELECTOR,
                                              '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(2) > div > div')
        advantages.click()
        time.sleep(2)
        # find torrents button
        torrents = self.driver.find_element(By.LINK_TEXT, 'Torrents')
        torrents.click()
        time.sleep(2)
        # find h1 torrents
        h1_torrents = self.driver.find_element(By.TAG_NAME, 'h1')
        return h1_torrents

    def find_elements_advantages_close_pop_up(self):
        advantages = self.driver.find_element(By.CSS_SELECTOR,
                                              '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(2) > div > div')
        advantages.click()
        time.sleep(2)
        # find close pop_up img x
        close_pop_up = self.driver.find_element(By.CSS_SELECTOR,
                                                '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div.nav-menu-item.expanded > div.nav-menu-item__submenu.advantages > div > button')
        close_pop_up.click()
        time.sleep(2)
        return close_pop_up

    def find_elements_products_android_pop_up(self):
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

        time.sleep(2)
        return self.driver

    def find_elements_products_chrome_pop_up(self):
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

        time.sleep(2)
        return self.driver

    def find_elements_products_windows_pop_up(self):
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

        time.sleep(2)
        return self.driver

