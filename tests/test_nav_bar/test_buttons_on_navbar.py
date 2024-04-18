import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from home_page.page_objects.nav_bar_page_objects import HomePage
import pytest

'''Why VPN test'''


@pytest.mark.navbar_links
def test_why_vpn_why_vpn_what_is_vpn(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'Free VPN – best free online VPN, fast and secure | Planet VPN'

    assert popup.find_elements_why_vpn_wats_is_vpn(expected_title)

    other_links_and_titles = [

        {'locator': (By.LINK_TEXT, 'No logs'), 'expected_title': 'Best no logs VPN - free vpn no logs - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'What is a VPN?'),
         'expected_title': 'What is a VPN and How to Use a VPN: A Comprehensive Guide'},
        {'locator': (By.LINK_TEXT, 'What is Proxy'),
         'expected_title': 'Proxy Types: Features and All You Need to Know | Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Our VPN network'),
         'expected_title': 'VPN servers - list of free vpn servers around the world - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'About VPN protocols'),
         'expected_title': 'VPN Protocols: Everything You Need To Know | Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Free VPN'),
         'expected_title': 'Free VPN Download - For all Devices with no Limits | Planet VPN'},

    ]

    for link_data in other_links_and_titles:
        wait = WebDriverWait(browser, 10)
        link_element = wait.until(EC.element_to_be_clickable(link_data['locator']))
        link_element.click()

        assert wait.until(EC.title_is(
            link_data['expected_title'])), f"Expected title {link_data['expected_title']} but got {browser.title}"

        popup.go_back()
        popup.find_button_why_and_click()


@pytest.mark.navbar_links
def test_pop_up_advantages_close_pop_up(browser):
    popup = HomePage(browser)
    popup.go_to()
    close_pop_up = popup.find_element_close_pop_up()

    assert close_pop_up, 'Pop-up did not close successfully'


'''Advantages button test'''


@pytest.mark.navbar_links
def test_pop_up_advantages_access_to_games_and_movies(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'Free VPN – best free online VPN, fast and secure | Planet VPN'

    assert popup.find_elements_advantages_access_pop_up(expected_title)

    other_links_and_titles = [

        {'locator': (By.LINK_TEXT, 'Access to games and movies'),
         'expected_title': 'Free VPN for access Gaming and Streaming | Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Steam'),
         'expected_title': 'Free VPN for Steam - How to use a VPN to unlock Steam - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Preventing surveillance'),
         'expected_title': 'Free VPN for Internet Protection - Protect your data online'},
        {'locator': (By.LINK_TEXT, 'Secure Wi Fi'),
         'expected_title': 'Free VPN for public WiFi - Secure Your Wi-Fi Connection - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Streaming'),
         'expected_title': 'Live streaming With free VPN - Live Sports With a VPN - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Airline Tickets'),
         'expected_title': 'Save Money on Flights With a free VPN - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Online Anonymity'),
         'expected_title': 'Free VPN for anonymous browsing and surfing - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Data encryption'),
         'expected_title': 'Data encryption with free VPN - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Music'),
         'expected_title': 'VPN for downloading and listen music - your favorite music with VPN'},
        {'locator': (By.LINK_TEXT, 'Booking Hotels'),
         'expected_title': 'Save on Hotels booking with free VPN - How to save money'},
        {'locator': (By.LINK_TEXT, 'Change or Hide your IP'),
         'expected_title': 'How to Change and Hide IP address with a free VPN - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Car Rentals'),
         'expected_title': 'Save money renting cars with free VPN - ways to save - Free VPN'},
        {'locator': (By.LINK_TEXT, 'Torrents'),
         'expected_title': 'Free P2P VPN - Download and Set Up VPN'},
    ]

    for link_data in other_links_and_titles:
        wait = WebDriverWait(browser, 10)
        link_element = wait.until(EC.element_to_be_clickable(link_data['locator']))
        link_element.click()

        assert wait.until(EC.title_is(
            link_data['expected_title'])), f"Expected title {link_data['expected_title']} but got {browser.title}"

        popup.go_back()
        popup.find_advantages_button_and_click()


'''Products button test'''


@pytest.mark.navbar_links
def test_pop_up_products_android(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'Free VPN – best free online VPN, fast and secure | Planet VPN'

    assert popup.find_elements_products_android_pop_up(expected_title)

    other_links_and_titles = [

        {'locator': (By.LINK_TEXT, 'Android'),
         'expected_title': 'Free VPN for Android - download best fast and safe VPN - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Chrome'),
         'expected_title': 'Free VPN for Chrome - download vpn Chrome extension - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Windows'),
         'expected_title': 'Free VPN for Windows - download without any limits - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Router'),
         'expected_title': 'VPN router configuration - setup vpn on router - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'DNS Leak Test'),
         'expected_title': 'DNS check - Online DNS propagation check - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'iOS'),
         'expected_title': 'Free VPN iOS - VPN for iPhone and iPad without limits - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Firefox'),
         'expected_title': 'Free VPN for Firefox - download firefox vpn extension - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'macOS'),
         'expected_title': 'Free VPN for Mac - best client for macOS - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'OpenVPN'),
         'expected_title': 'OpenVPN configurations - client configurations for Windows - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'WebRTC Leak Test'),
         'expected_title': 'WebRTC leak shield - online leak test - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Edge'),
         'expected_title': 'Free VPN Edge - download extension for Edge - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Linux'),
         'expected_title': 'Free VPN for Linux - best for Linux without registration - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Virus scan'),
         'expected_title': 'Free virus scan - check for viruses by file or url - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Opera'),
         'expected_title': 'Free VPN for Opera - best free Opera extension - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'What is my IP?'),
         'expected_title': 'What is my IP? Check my IP online - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Yandex'),
         'expected_title': 'Free VPN for Yandex Browser - vpn extension - Planet VPN'},
        {'locator': (By.LINK_TEXT, 'Password generator'),
         'expected_title': 'Password generator - random and strong password - Planet VPN'},

    ]

    for link_data in other_links_and_titles:
        wait = WebDriverWait(browser, 10)
        link_element = wait.until(EC.element_to_be_clickable(link_data['locator']))
        link_element.click()

        assert wait.until(EC.title_is(
            link_data['expected_title'])), f"Expected title {link_data['expected_title']} but got {browser.title}"

        popup.go_back()
        popup.find_products_button_and_click()


'''Premium button & login & logo test'''


@pytest.mark.navbar_links
def test_premium_button(browser):
    premium = HomePage(browser)
    premium.go_to()
    expected_title = 'Buy best VPN - buy a vpn service subscription - Planet VPN'

    assert premium.find_elements_premium_and_login_and_logo_buttons(expected_title)

    other_links_and_titles = [
        {'locator': (By.CSS_SELECTOR,
                     '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__nav > div.page-header__logo > a > img'),
         'expected_title': 'Free VPN – best free online VPN, fast and secure | Planet VPN'},
        {'locator': (By.CSS_SELECTOR,
                     '#__layout > div > div:nth-child(1) > div > div.page-section.transparent.full-height > div > div > div.page-header__controls > div.header-cabinet > div.header-cabinet__button > a'),
         'expected_title': 'Login'},

    ]

    for link_data in other_links_and_titles:
        wait = WebDriverWait(browser, 10)
        link_element = wait.until(EC.element_to_be_clickable(link_data['locator']))
        link_element.click()

        assert wait.until(EC.title_is(link_data['expected_title']))


@pytest.mark.download
def test_download_button(browser):
    download_button = HomePage(browser)
    download_button.go_to()
    expected_title = 'Free VPN Download - For all Devices with no Limits | Planet VPN'

    assert download_button.find_elements_download_vpn(expected_title)


@pytest.mark.navbar_links
def test_localizations_button_pt(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    expected_title = 'Free VPN – best free online VPN, fast and secure | Planet VPN'

    assert localisations_button.find_elements_localizations_pt(expected_title)

    other_links_and_titles = [
        {'locator': (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[10]'),
         'expected_title': 'Free VPN e proxy - VPN gratis sem anúncios ou limites | Planet VPN'},
        {'locator': (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[1]'),
         'expected_title': 'أفضل برنامج VPN مجاني بدون اعلانات وموثوق به من 10 مليون مستخدم'},
        {'locator': (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[2]'),
         'expected_title': 'Zdarma VPN - nejlepší Free online VPN, rychlá a bezpečná | Planet VPN'},
        {'locator': (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[3]'),
         'expected_title': 'VPN Kostenlos – das beste Free VPN ohne Grenzen | Planet VPN'},
        {'locator': (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[4]'),
         'expected_title': 'Free VPN – best free online VPN, fast and secure | Planet VPN'},
        {'locator': (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[5]'),
         'expected_title': 'VPN Gratis y Proxy: Free VPN sin restricciones ni límites - Planet VPN'},
        {'locator': (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[6]'),
         'expected_title': 'VPN gratuit - le meilleur free VPN sans limites | Planet VPN'},
        {'locator': (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[7]'),
         'expected_title': 'VPN Gratis – VPN online gratis terbaik, cepat dan aman | VPN Planet'},
        {'locator': (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[8]'),
         'expected_title': 'VPN Gratis: la migliore VPN online Gratis, veloce e sicura - Planet VPN'},
        {'locator': (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[9]'),
         'expected_title': 'Darmowy VPN – najlepszy VPN online, szybki i bezpieczny | Planet VPN'},
        {'locator': (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[11]'),
         'expected_title': 'Free VPN - cel mai bun VPN online gratuit, rapid și sigur | Planet VPN'},
        {'locator': (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[12]'),
         'expected_title': 'Бесплатный VPN - ВПН без лимитов и регистрации | Planet VPN'},
        {'locator': (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[13]'),
         'expected_title': 'Gratis VPN och proxy - gratis vpn utan annonser | Planet VPN'},
        {'locator': (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[14]'),
         'expected_title': 'Free VPN & พร็อกซี่ - ไม่มีโฆษณา จำกัด ความเร็วและการรับส่งข้อมูล | Planet VPN'},
        {'locator': (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[15]'),
         'expected_title': 'Libreng VPN – pinakamahusay na libreng online na VPN, mabilis at secure | Planet VPN'},
        {'locator': (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[16]'),
         'expected_title': 'Free VPN ve Proxy - reklamsız ve sınırsız en iyi ücretsiz vpn | Planet VPN'},
        {'locator': (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[17]'),
         'expected_title': 'VPN безкоштовно - без реєстрації, обмежень швидкості та трафіку | Planet VPN'},
    ]

    for link_data in other_links_and_titles:
        wait = WebDriverWait(browser, 10)
        link_element = wait.until(EC.element_to_be_clickable(link_data['locator']))
        link_element.click()

        assert wait.until(EC.title_is(link_data['expected_title']))
        localisations_button.go_back()
        localisations_button.find_english_element_and_click()
