import pytest
from home_page.page_objects.body_page_objects import HomePageBody
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.downloads
def test_os_browsers_links(browser):
    links = HomePageBody(browser)
    links.go_to()
    expected_title = 'Free VPN for Android - download best fast and safe VPN - Planet VPN'

    assert links.find_os_and_browsers_links(expected_title), 'Expected OS and browser'

    other_links_and_titles = [
        {'locator': (By.CSS_SELECTOR,
                     '#__layout > div > div:nth-child(1) > main > div > article > header > div.page-section.light > div > div > div > a:nth-child(2)'),
         'expected_title': 'Free VPN iOS - VPN for iPhone and iPad without limits - Planet VPN'},
        # {'locator': (By.CSS_SELECTOR,
        #              '#__layout > div > div:nth-child(1) > main > header > div.page-section.light > div > div > div > a:nth-child(3)'),
        #  'expected_title': 'AppGallery'},
        {'locator': (By.CSS_SELECTOR,
                     '#__layout > div > div:nth-child(1) > main > header > div.page-section.light > div > div > div > a:nth-child(4)'),
         'expected_title': 'Free VPN for Chrome - download vpn Chrome extension - Planet VPN'},
        {'locator': (By.CSS_SELECTOR,
                     '#__layout > div > div:nth-child(1) > main > header > div.page-section.light > div > div > div > a:nth-child(5)'),
         'expected_title': 'Free VPN for Firefox - download firefox vpn extension - Planet VPN'},
        {'locator': (By.CSS_SELECTOR,
                     '#__layout > div > div:nth-child(1) > main > header > div.page-section.light > div > div > div > a:nth-child(6)'),
         'expected_title': 'Free VPN Edge - download extension for Edge - Planet VPN'},
        {'locator': (By.CSS_SELECTOR,
                     '#__layout > div > div:nth-child(1) > main > header > div.page-section.light > div > div > div > a:nth-child(7)'),
         'expected_title': 'Free VPN for Opera - best free Opera extension - Planet VPN'},
        {'locator': (By.CSS_SELECTOR,
                     '#__layout > div > div:nth-child(1) > main > header > div.page-section.light > div > div > div > a:nth-child(8)'),
         'expected_title': 'Free VPN for Yandex Browser - vpn extension - Planet VPN'},
        {'locator': (By.CSS_SELECTOR,
                     '#__layout > div > div:nth-child(1) > main > header > div.page-section.light > div > div > div > a:nth-child(9)'),
         'expected_title': 'Free VPN for Windows - download without any limits - Planet VPN'},
        {'locator': (By.CSS_SELECTOR,
                     '#__layout > div > div:nth-child(1) > main > header > div.page-section.light > div > div > div > a:nth-child(10)'),
         'expected_title': 'Free VPN for Mac - best client for macOS - Planet VPN'},
        {'locator': (By.CSS_SELECTOR,
                     '#__layout > div > div:nth-child(1) > main > header > div.page-section.light > div > div > div > a:nth-child(11)'),
         'expected_title': 'Free VPN for Linux - best for Linux without registration - Planet VPN'},
        {'locator': (By.CSS_SELECTOR,
                     '#__layout > div > div:nth-child(1) > main > header > div.page-section.light > div > div > div > a:nth-child(12)'),
         'expected_title': 'VPN router configuration - setup vpn on router - Planet VPN'},
        {'locator': (By.CSS_SELECTOR,
                     '#__layout > div > div:nth-child(1) > main > header > div.page-section.light > div > div > div > a:nth-child(13)'),
         'expected_title': 'OpenVPN configurations - client configurations for Windows - Planet VPN'},

    ]

    for link_data in other_links_and_titles:
        wait = WebDriverWait(browser, 10)
        link_element = wait.until(EC.element_to_be_clickable(link_data['locator']))
        link_element.click()

        assert wait.until(EC.title_is(
            link_data['expected_title'])), f"Expected title {link_data['expected_title']} but got {browser.title}"

        links.go_back()
