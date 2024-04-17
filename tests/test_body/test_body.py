import pytest
from home_page.page_objects.body_page_objects import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.mark.browsers_os
def test_os_body_links_and_buttons(browser):
    links = HomePageBody(browser)
    links.go_to()
    expected_title = 'Free VPN for Android - download best fast and safe VPN - Planet VPN'

    assert links.find_body_links_and_buttons(expected_title), 'Expected OS and browser'

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
        {'locator': (By.CSS_SELECTOR,
                     '#__layout > div > div:nth-child(1) > main > div:nth-child(4) > div > section > div.home-platforms > div.home-platforms__cards > div.home-platforms__card.mobile > div.home-platforms__links > a:nth-child(2)'),
         'expected_title': 'Free VPN iOS - VPN for iPhone and iPad without limits - Planet VPN'},

        {'locator': (By.CSS_SELECTOR,
                     '#__layout > div > div:nth-child(1) > main > div:nth-child(4) > div > section > div.home-platforms > div.home-platforms__cards > div.home-platforms__card.desktop > div.home-platforms__links > a:nth-child(1)'),
         'expected_title': 'Free VPN for Windows - download without any limits - Planet VPN'},
        {'locator': (By.CSS_SELECTOR,
                     '#__layout > div > div:nth-child(1) > main > div:nth-child(4) > div > section > div.home-platforms > div.home-platforms__cards > div.home-platforms__card.desktop > div.home-platforms__links > a:nth-child(2)'),
         'expected_title': 'Free VPN for Mac - best client for macOS - Planet VPN'},
        {'locator': (By.CSS_SELECTOR,
                     '#__layout > div > div:nth-child(1) > main > div:nth-child(4) > div > section > div.home-platforms > div.home-platforms__cards > div.home-platforms__card.desktop > div.home-platforms__links > a:nth-child(3)'),
         'expected_title': 'Free VPN for Linux - best for Linux without registration - Planet VPN'},
        {'locator': (By.CSS_SELECTOR,
                     '#__layout > div > div:nth-child(1) > main > div:nth-child(4) > div > section > div.home-platforms > div.home-platforms__cards > div.home-platforms__card.browser > div.home-platforms__links > a:nth-child(1)'),
         'expected_title': 'Free VPN for Chrome - download vpn Chrome extension - Planet VPN'},
        {'locator': (By.CSS_SELECTOR,
                     '#__layout > div > div:nth-child(1) > main > div:nth-child(4) > div > section > div.home-platforms > div.home-platforms__cards > div.home-platforms__card.browser > div.home-platforms__links > a:nth-child(2)'),
         'expected_title': 'Free VPN for Firefox - download firefox vpn extension - Planet VPN'},
        {'locator': (By.CSS_SELECTOR,
                     '#__layout > div > div:nth-child(1) > main > div:nth-child(4) > div > section > div.home-platforms > div.home-platforms__cards > div.home-platforms__card.browser > div.home-platforms__links > a:nth-child(3)'),
         'expected_title': 'Free VPN Edge - download extension for Edge - Planet VPN'},
        {'locator': (By.CSS_SELECTOR,
                     '#__layout > div > div:nth-child(1) > main > div:nth-child(4) > div > section > div.home-platforms > div.home-platforms__cards > div.home-platforms__card.browser > div.home-platforms__links > a:nth-child(5)'),
         'expected_title': 'Free VPN for Yandex Browser - vpn extension - Planet VPN'},
        {'locator': (By.CSS_SELECTOR,
                     '#__layout > div > div:nth-child(1) > main > div.home-network > div > div > section > div.home-network__route > a'),
         'expected_title': 'VPN servers - list of free vpn servers around the world - Planet VPN'},
        {'locator': (By.LINK_TEXT,
                     'Get all the benefits'),
         'expected_title': 'Buy best VPN - buy a vpn service subscription - Planet VPN'}

    ]

    for link_data in other_links_and_titles:
        wait = WebDriverWait(browser, 10)
        link_element = wait.until(EC.element_to_be_clickable(link_data['locator']))
        link_element.click()

        assert wait.until(EC.title_is(
            link_data['expected_title'])), f"Expected title {link_data['expected_title']} but got {browser.title}"

        links.go_back()


@pytest.mark.downloads
def test_file_download_center_body(browser_and_download):
    driver, download_directory = browser_and_download
    download_page = DownloadPage(driver, download_directory)
    download_page.go_to_download('https://freevpnplanet.com')
    expected_filename = 'planetvpn.dmg'
    file_path = download_page.download_file(expected_filename)

    assert os.path.exists(file_path), f'Файл {expected_filename} не загружен в папку {download_directory}'


@pytest.mark.downloads
def test_file_download_get_for_free(browser_and_download):
    driver, download_directory = browser_and_download
    download_page = DownloadPage(driver, download_directory)
    download_page.go_to_download('https://freevpnplanet.com')
    expected_filename = 'planetvpn.dmg'
    file_path = download_page.download_file(expected_filename)

    assert os.path.exists(file_path), f'Файл {expected_filename} не загружен в папку {download_directory}'


@pytest.mark.dropdown
def test_dropdown_menu(browser):
    dropdown_page = HomePageBody(browser)

    dropdown_locator = (By.CLASS_NAME, 'faq-item__question')

    menu_text_locators = [
        ((By.TAG_NAME, 'p'),
         "A free VPN, when run properly, can offer a good balance between security and accessibility. Our free VPN aims to provide reliable connections and protect user data. While many may doubt the effectiveness of free services, our VPN aims to challenge that notion by maintaining a level of performance and reliability. As always,  users should assess their needs and do due diligence before making a choice."),
        # ((By.TAG_NAME, 'p'),
        #  "Absolutely! While concerns can arise with some free VPNs, our service prioritizes user safety above all. We utilize advanced encryption standards and strict no-log policies to ensure your online activities remain private and secure. Regularly audited and committed to transparency, our free VPN is designed with the user's security in mind. Enjoy peace of mind knowing that your online presence is protected with us."),
        # ((By.TAG_NAME, 'p'),
        #  "There are several reputable free VPNs out there, and among them, Planet VPN is a notable choice. Planet VPN strikes a good balance between user privacy, speed, and global server coverage. While ensuring the security of user data with advanced encryption, its performance remains consistently high. It's always a good thing for users to compare features and reviews, but Planet VPN is definitely a strong contender in the free VPN category."),

    ]

    dropdown_menus = dropdown_page.find_dropdown_menu(dropdown_locator)

    dropdown_page.click_and_verify_dropdown_text(dropdown_menus, menu_text_locators)
