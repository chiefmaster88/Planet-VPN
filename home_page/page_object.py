# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
#
# class HomePage(object):
#     def find_why_vpn(self):
#         # Находим и кликаем по элементам
#         why_vpn = self.web_driver.find_element(By.CSS_SELECTOR,
#                                                "#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(1) > div > div")
#         why_vpn.click()
#         time.sleep(3)
#         what_is_a_vpn = self.web_driver.find_element(By.LINK_TEXT, 'What is a VPN?')
#         what_is_a_vpn.click()
#         time.sleep(3)
#         self.web_driver.quit()
#
#     def find_no_logs(self):
#         why_vpn = self.web_driver.find_element(By.CSS_SELECTOR,
#                                                "#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(1) > div > div")
#         why_vpn.click()
#         no_logs = self.web_driver.find_element(By.LINK_TEXT, 'No logs')
#         no_logs.click()
#         time.sleep(3)
#         self.web_driver.quit()
#
#     def get_title(self):
#         # Возвращает текущий заголовок страницы
#         return self.web_driver.title
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:
    url = 'https://freevpnplanet.com/'

    def __init__(self, browser):
        self.driver = browser

    def go_to(self):
        self.driver.get(HomePage.url)

    def find_elemts_why_vpn_wats_is_vpn(self):
        why_vpn = self.driver.find_element(By.CSS_SELECTOR,
                                           '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(1) > div > div')
        why_vpn.click()
        time.sleep(2)
        what_is_vpn = self.driver.find_element(By.LINK_TEXT, 'What is a VPN?')
        what_is_vpn.click()
        time.sleep(2)
        # find h1 what is vpn
        h1_wat_is_vpn = self.driver.find_element(By.TAG_NAME, 'h1')
        return h1_wat_is_vpn

    def find_elements_why_vpn_no_logs(self):
        why_vpn = self.driver.find_element(By.CSS_SELECTOR,
                                           '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(1) > div > div')
        why_vpn.click()
        time.sleep(2)
        # find no_logs button
        no_logs = self.driver.find_element(By.LINK_TEXT, 'No logs')
        no_logs.click()
        time.sleep(2)
        # find h1 no_logs
        h1_nologs = self.driver.find_element(By.TAG_NAME, 'h1')
        return h1_nologs

    def find_elements_why_vpn_what_is_proxy(self):
        why_vpn = self.driver.find_element(By.CSS_SELECTOR,
                                           '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(1) > div > div')
        why_vpn.click()
        time.sleep(2)
        # find what_is_proxy button
        what_is_proxy = self.driver.find_element(By.LINK_TEXT, 'What is Proxy')
        what_is_proxy.click()
        time.sleep(2)
        # find h1 what_is_proxy
        h1_what_is_proxy = self.driver.find_element(By.TAG_NAME, 'h1')
        return h1_what_is_proxy

    def find_elements_why_vpn_our_vpn_network(self):
        why_vpn = self.driver.find_element(By.CSS_SELECTOR,
                                           '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(1) > div > div')
        why_vpn.click()
        time.sleep(2)
        # find our_vpn_network button
        our_vpn_network = self.driver.find_element(By.LINK_TEXT, 'Our VPN network')
        our_vpn_network.click()
        time.sleep(2)
        # find h1 our_vpn_network
        h1_our_vpn_network = self.driver.find_element(By.TAG_NAME, 'h1')
        return h1_our_vpn_network

    def find_elemets_why_vpn_about_vpn_protocols(self):
        why_vpn = self.driver.find_element(By.CSS_SELECTOR,
                                           '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(1) > div > div')
        why_vpn.click()
        time.sleep(2)
        # find about_vpn_protocols button
        about_vpn_protocols = self.driver.find_element(By.LINK_TEXT, 'About VPN protocols')
        about_vpn_protocols.click()
        time.sleep(2)
        # find h1 about_vpn_protocols
        h1_about_vpn_protocols = self.driver.find_element(By.TAG_NAME, 'h1')
        return h1_about_vpn_protocols

    def find_elements_why_vpn_free_vpn(self):
        why_vpn = self.driver.find_element(By.CSS_SELECTOR,
                                           '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(1) > div > div')
        why_vpn.click()
        time.sleep(2)
        # find free_vpn button
        free_vpn = self.driver.find_element(By.LINK_TEXT, 'Free VPN')
        free_vpn.click()
        time.sleep(2)
        # find h1 free_vpn
        h1_free_vpn = self.driver.find_element(By.TAG_NAME, 'h1')
        return h1_free_vpn

    def find_elements_why_vpn_close_pop_up(self):
        why_vpn = self.driver.find_element(By.CSS_SELECTOR,
                                           '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div:nth-child(1) > div > div')
        why_vpn.click()
        time.sleep(2)
        # find close image
        close_pop_up = self.driver.find_element(By.CSS_SELECTOR,
                                                '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__menu > nav > div.nav-menu__menu > div.nav-menu-item.expanded > div.nav-menu-item__submenu.about > div > button > img')
        close_pop_up.click()
        time.sleep(2)
        return close_pop_up

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

