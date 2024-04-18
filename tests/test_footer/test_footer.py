from home_page.page_objects.footer_page_objects import *
import pytest


@pytest.mark.footer_links
def test_footer_links(browser):
    footer = FooterPageObjects(browser)

    expected_title = 'Приложения в Google Play – Бесплатный VPN от Planet VPN'

    assert footer.find_footer_links(expected_title)
    footer.go_to('https://freevpnplanet.com/')

    other_links_and_titles = [
        {'locator': (By.XPATH, '//*[@id="__layout"]/div/div[1]/footer/div/div/div/div[2]/div/a[3]'),
         'expected_title': 'AppGallery'},
        {'locator': (By.XPATH, '//*[@id="__layout"]/div/div[1]/footer/div/div/div/div[2]/div/a[4]'),
         'expected_title': 'App Store: Бесплатный VPN от Planet VPN'}
    ]

    for link_data in other_links_and_titles:
        wait = WebDriverWait(browser, 10)
        link_data_element = wait.until(EC.element_to_be_clickable(link_data['locator']))
        link_data_element.click()

        assert footer.find_footer_links(link_data['expected_title'])
        footer.go_to('https://freevpnplanet.com/')


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
