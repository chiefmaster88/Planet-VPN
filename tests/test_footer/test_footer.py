import time

from home_page.page_objects.footer_page_objects import *
import pytest


@pytest.mark.footer_links
def test_footer_links(browser):
    footer = FooterPageObjects(browser)

    expected_title = 'Proxy Types: Features and All You Need to Know | Planet VPN'

    assert footer.find_footer_links(expected_title)

    other_links_and_titles = [
        {'locator': (By.LINK_TEXT, 'About VPN protocols'),
         'expected_title': 'VPN Protocols: Everything You Need To Know | Planet VPN'},
        {'locator': (By.LINK_TEXT, 'No logs'),
         'expected_title': 'Best no logs VPN - free vpn no logs - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Our VPN network'),
         'expected_title': 'VPN servers - list of free vpn servers around the world - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Free VPN'),
         'expected_title': 'Free VPN Download - For all Devices with no Limits | Planet VPN'},
        # {'locator': (By.LINK_TEXT, 'VPN bot for Telegram'),
        #  'expected_title': 'Best no logs VPN - free vpn no logs - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Android'),
         'expected_title': 'Free VPN for Android - download best fast and safe VPN - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'iOS'),
         'expected_title': 'Free VPN iOS - VPN for iPhone and iPad without limits - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Chrome'),
         'expected_title': 'Free VPN for Chrome - download vpn Chrome extension - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Firefox'),
         'expected_title': 'Free VPN for Firefox - download firefox vpn extension - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Edge'),
         'expected_title': 'Free VPN Edge - download extension for Edge - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Opera'),
         'expected_title': 'Free VPN for Opera - best free Opera extension - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Yandex'),
         'expected_title': 'Free VPN for Yandex Browser - vpn extension - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Windows'),
         'expected_title': 'Free VPN for Windows - download without any limits - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'macOS'), 'expected_title': 'Free VPN for Mac - best client for macOS - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Linux'),
         'expected_title': 'Free VPN for Linux - best for Linux without registration - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Router'),
         'expected_title': 'VPN router configuration - setup vpn on router - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'OpenVPN'),
         'expected_title': 'OpenVPN configurations - client configurations for Windows - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Free VPN for Roblox'),
         'expected_title': 'Free VPN for Roblox - How to unblock in 2024 | Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Free VPN for Warzone'),
         'expected_title': 'Free VPN for Warzone - playing with low ping in 2024 | Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Free VPN for Netflix'),
         'expected_title': 'The best Free VPN for Netflix in 2024 - Play from anywhere | Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Free VPN for Twitter'),
         'expected_title': 'Free VPN for Twitter - access anywhere in 2024 | Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Free VPN for Reddit'),
         'expected_title': 'Free VPN for Reddit - the best choice of users in 2024 | Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Free VPN for PUBG'),
         'expected_title': 'The best Free VPN for PUBG in 2024 - Play from anywhere | Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Free VPN for Mobile Legends'),
         'expected_title': 'Free VPN for playing Mobile Legends online in 2024 | Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Free VPN for Instagram'),
         'expected_title': 'Free VPN for Instagram - watch anywhere in 2024 | Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Free VPN for Disney Plus'),
         'expected_title': 'Free VPN for Disney Plus - watch anywhere in 2024 | Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Free VPN for Gameloop'),
         'expected_title': 'Free VPN for Gameloop - Play from anywhere in 2024 | Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Free VPN for Free Fire'),
         'expected_title': 'Free VPN for playing Free Fire online in 2024 | Planet VPN'},

        {'locator': (By.LINK_TEXT, 'Free VPN for Firestick'),
         'expected_title': 'The Free VPN for Firestick and Fire TV in 2024 | Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Free VPN for Telegram'),
         'expected_title': 'Free VPN for Telegram - access anywhere in 2024 | Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Free VPN for WhatsApp'),
         'expected_title': 'Free VPN for WhatsApp - Access Anywhere in 2024 | Planet VPN'},
        {'locator': (By.LINK_TEXT, 'DNS Leak Test'),
         'expected_title': 'DNS check - Online DNS propagation check - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'WebRTC Leak Test'),
         'expected_title': 'WebRTC leak shield - online leak test - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Virus scan'),
         'expected_title': 'Free virus scan - check for viruses by file or url - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'What is my IP?'),
         'expected_title': 'What is my IP? Check my IP online - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Password generator'),
         'expected_title': 'Password generator - random and strong password - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Contact us'), 'expected_title': 'Planet VPN Contacts'},
        {'locator': (By.LINK_TEXT, 'About Us'), 'expected_title': 'About us - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Careers'), 'expected_title': 'Careers'},
        {'locator': (By.LINK_TEXT, 'Affiliate program'),
         'expected_title': 'Planet VPN Affiliate Program - the Best Conditions and Offers'},
        {'locator': (By.LINK_TEXT, 'Terms of use'),
         'expected_title': 'Terms of use - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Refund policy'),
         'expected_title': 'Refunds'},
        {'locator': (By.LINK_TEXT, 'Privacy policy'),
         'expected_title': 'Privacy policy - Planet VPN'},
        # {'locator': (By.LINK_TEXT, 'Support 24/7'),
        #  'expected_title': 'Best no logs VPN - free vpn no logs - Planet VPN'},--- pop up
        {'locator': (By.LINK_TEXT, 'Blog'), 'expected_title': 'Blog Planet VPN -'},

        # {'locator': (By.XPATH, '//*[@id="__layout"]/div/div[1]/footer/div/div/div/div[2]/div/a[3]'),
        #  'expected_title': 'AppGallery'},
        # {'locator': (By.XPATH, '//*[@id="__layout"]/div/div[1]/footer/div/div/div/div[2]/div/a[4]'),
        #  'expected_title': 'App Store: Бесплатный VPN от Planet VPN'},
        # {'locator': (By.LINK_TEXT, 'Telegram'), 'expected_title': 'Telegram: Contact @FreeVPNPlanet'},
        # {'locator': (By.LINK_TEXT, 'Facebook'), 'expected_title': 'Telegram: Contact @FreeVPNPlanet'},
        # {'locator': (By.LINK_TEXT, 'Twitter'), 'expected_title': 'Telegram: Contact @FreeVPNPlanet'},
        # {'locator': (By.LINK_TEXT, 'YouTube'), 'expected_title': 'Telegram: Contact @FreeVPNPlanet'},
        # {'locator': (By.LINK_TEXT, 'Instagram'), 'expected_title': 'Telegram: Contact @FreeVPNPlanet'},
        # {'locator': (By.LINK_TEXT, 'Pinterest'), 'expected_title': 'Telegram: Contact @FreeVPNPlanet'},
        # {'locator': (By.LINK_TEXT, 'TikTok'), 'expected_title': 'Telegram: Contact @FreeVPNPlanet'},

    ]

    for link_data in other_links_and_titles:
        wait = WebDriverWait(browser, 10)
        link_data_element = wait.until(EC.element_to_be_clickable(link_data['locator']))
        link_data_element.click()

        assert wait.until(EC.title_is(link_data['expected_title']))
        footer.go_back()


# @pytest.mark.test
# def test_support_pop_up(browser):
#     footer = FooterPageObjects(browser)
#     footer.find_footer_pop_support()
#     wait = WebDriverWait(browser, 10)
#
#     elements = [
#         (By.XPATH, '//*[@id="Embed"]/div/div')
#     ]
#
#     for element in elements:
#         element = wait.until(EC.visibility_of_element_located(element))
#         assert element is not None
#
#
# @pytest.mark.test
# def test_pop_up_chat(browser):
#     footer = FooterPageObjects(browser)
#     footer.find_footer_pop_up_chat()
#     wait = WebDriverWait(browser, 10)
#
#     elements = [
#         (By.XPATH, '//*[@id="Embed"]/div/div/div/div/div/div/form/footer/div/button')
#     ]
#
#     for element in elements:
#         element = wait.until(EC.element_to_be_clickable(element))
#         assert element is not None
#


@pytest.mark.footer_downloads
def test_footer_downloads(browser_and_download):
    driver, download_directory = browser_and_download
    download_footer = FooterPageDownloads(driver, download_directory)
    download_footer.go_to('https://freevpnplanet.com/')
    expected_filename = 'planetvpn.exe'
    file_path = download_footer.find_element_download_windows(expected_filename)

    assert os.path.exists(file_path), f'Файл {expected_filename} не загружен в папку {download_directory}'


@pytest.mark.footer_downloads
def test_footer_downloads_macOS(browser_and_download):
    driver, download_directory = browser_and_download
    download_footer = FooterPageDownloads(driver, download_directory)
    download_footer.go_to('https://freevpnplanet.com/')
    expected_filename = 'planetvpn.dmg'
    file_path = download_footer.find_element_download_macOS(expected_filename)

    assert os.path.exists(file_path), f'Файл {expected_filename} не загружен в папку {download_directory}'
