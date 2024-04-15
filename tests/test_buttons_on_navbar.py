import time

from home_page.page_object import HomePage
import pytest

'''Why VPN test'''


@pytest.mark.why_vpn
def test_why_vpn_why_vpn_what_is_vpn(browser):
    popup = HomePage(browser)
    popup.go_to()
    what_is_a_vpn = popup.find_elements_why_vpn_wats_is_vpn()

    assert what_is_a_vpn.title == 'What is a VPN and How to Use a VPN: A Comprehensive Guide'


@pytest.mark.why_vpn
def test_pop_up_why_vpn_no_logs(browser):
    popup = HomePage(browser)
    popup.go_to()
    no_logs = popup.find_elements_why_vpn_no_logs()

    assert no_logs.title == 'Best no logs VPN - free vpn no logs - Planet VPN'


@pytest.mark.why_vpn
def test_pop_up_why_vpn_what_is_proxy(browser):
    popup = HomePage(browser)
    popup.go_to()
    what_is_proxy = popup.find_elements_why_vpn_what_is_proxy()

    assert what_is_proxy.title == 'Proxy Types: Features and All You Need to Know | Planet VPN'


@pytest.mark.why_vpn
def test_pop_up_why_vpn_our_vpn_network(browser):
    popup = HomePage(browser)
    popup.go_to()
    our_vpn_network = popup.find_elements_why_vpn_our_vpn_network()

    assert our_vpn_network.title == 'VPN servers - list of free vpn servers around the world - Planet VPN'


@pytest.mark.why_vpn
def test_pop_up_why_vpn_about_vpn_protocols(browser):
    popup = HomePage(browser)
    popup.go_to()
    about_vpn_protocols = popup.find_elemets_why_vpn_about_vpn_protocols()

    assert about_vpn_protocols.title == 'VPN Protocols: Everything You Need To Know | Planet VPN'


@pytest.mark.why_vpn
def test_pop_up_why_vpn_free_vpn(browser):
    popup = HomePage(browser)
    popup.go_to()
    free_vpn = popup.find_elements_why_vpn_free_vpn()

    assert free_vpn.title == 'Free VPN Download - For all Devices with no Limits | Planet VPN', "Free VPN  error"


@pytest.mark.why_vpn
def test_pop_up_why_vpn_close_pop_up(browser):
    popup = HomePage(browser)
    popup.go_to()
    close_pop_up = popup.find_elements_why_vpn_close_pop_up()

    assert close_pop_up, 'Pop-up did not close successfully'


'''Advantages button test'''


@pytest.mark.advantages
def test_pop_up_advantages_access_to_games_and_movies(browser):
    pop_up = HomePage(browser)
    pop_up.go_to()
    advantages_access = pop_up.find_elements_advantages_access_pop_up()

    assert advantages_access.title == 'Free VPN for access Gaming and Streaming | Planet VPN'


@pytest.mark.advantages
def test_pop_up_advantages_steam(browser):
    pop_up = HomePage(browser)
    pop_up.go_to()
    advantages_steam = pop_up.find_elements_advantages_steam()

    assert advantages_steam.title == 'Free VPN for Steam - How to use a VPN to unlock Steam - Planet VPN'


@pytest.mark.advantages
def test_pop_up_advantages_preventing_surveillance(browser):
    pop_up = HomePage(browser)
    pop_up.go_to()
    advantages_preventing_surveillance = pop_up.find_elements_advantages_preventing_surveillance()

    assert advantages_preventing_surveillance.title == 'Free VPN for Internet Protection - Protect your data online'


#
@pytest.mark.advantages
def test_pop_up_advantages_secure_wi_fi(browser):
    pop_up = HomePage(browser)
    pop_up.go_to()
    advantages_secure_wi = pop_up.find_elements_advantages_secure_wi_fi()

    assert advantages_secure_wi.title == 'Free VPN for public WiFi - Secure Your Wi-Fi Connection - Planet VPN'


#
#
@pytest.mark.advantages
def test_pop_up_advantages_streaming(browser):
    popup = HomePage(browser)
    popup.go_to()
    advantages_streaming = popup.find_elements_advantages_streaming()

    assert advantages_streaming.title == 'Live streaming With free VPN - Live Sports With a VPN - Planet VPN'


@pytest.mark.advantages
def test_pop_up_advantages_airline_tickets(browser):
    popup = HomePage(browser)
    popup.go_to()
    advantages_airline_tickets = popup.find_elements_advantages_airline_tickets()

    assert advantages_airline_tickets.title == 'Save Money on Flights With a free VPN - Planet VPN'


@pytest.mark.advantages
def test_pop_up_advantages_online_anonymity(browser):
    popup = HomePage(browser)
    popup.go_to()
    advantages_online_anonymity = popup.find_elements_advantages_online_anonymity()

    assert advantages_online_anonymity.title == 'Free VPN for anonymous browsing and surfing - Planet VPN'


@pytest.mark.advantages
def test_pop_up_advantages_data_encryption(browser):
    popup = HomePage(browser)
    popup.go_to()
    advantages_data_encryption = popup.find_elements_advantages_data_encryption()

    assert advantages_data_encryption.title == 'Data encryption with free VPN - Planet VPN'


@pytest.mark.advantages
def test_pop_up_advantages_music(browser):
    popup = HomePage(browser)
    popup.go_to()
    music = popup.find_elements_advantages_music()

    assert music.title == 'VPN for downloading and listen music - your favorite music with VPN'


@pytest.mark.advantages
def test_pop_up_advantages_booking_hotels(browser):
    popup = HomePage(browser)
    popup.go_to()
    booking_hotels = popup.find_elements_advantages_booking_hotels()

    assert booking_hotels.title == 'Save on Hotels booking with free VPN - How to save money'


@pytest.mark.advantages
def test_pop_up_advantages_change_or_hide_ip(browser):
    popup = HomePage(browser)
    popup.go_to()
    change_or_hide_ip = popup.find_elements_advantages_change_or_hid_ip()

    assert change_or_hide_ip.title == 'How to Change and Hide IP address with a free VPN - Planet VPN'


@pytest.mark.advantages
def test_pop_up_advantages_car_rentals(browser):
    popup = HomePage(browser)
    popup.go_to()
    car_rentals = popup.find_elements_advantages_car_rentals()

    assert car_rentals.title == 'Save money renting cars with free VPN - ways to save - Free VPN'


@pytest.mark.advantages
def test_pop_up_advantages_car_torrents(browser):
    popup = HomePage(browser)
    popup.go_to()
    car_torrents = popup.find_elements_advantages_torrents()

    assert car_torrents.title == 'Free P2P VPN - Download and Set Up VPN'


@pytest.mark.advantages
def test_pop_up_advantages_close_pop_up(browser):
    popup = HomePage(browser)
    popup.go_to()
    close_pop_up = popup.find_elements_advantages_close_pop_up()

    assert close_pop_up, 'Pop-up did not close successfully'


'''Products button test'''


@pytest.mark.products
def test_pop_up_products_android(browser):
    popup = HomePage(browser)
    popup.go_to()
    android = popup.find_elements_products_android_pop_up()

    assert android.title == 'Free VPN for Android - download best fast and safe VPN - Planet VPN'


@pytest.mark.products
def test_pop_up_products_chrome(browser):
    popup = HomePage(browser)
    popup.go_to()
    chrome = popup.find_elements_products_chrome_pop_up()

    assert chrome.title == 'Free VPN for Chrome - download vpn Chrome extension - Planet VPN'


@pytest.mark.products
def test_pop_up_products_windows(browser):
    popup = HomePage(browser)
    popup.go_to()
    windows = popup.find_elements_products_windows_pop_up()

    assert windows.title == 'Free VPN for Windows - download without any limits - Planet VPN'


@pytest.mark.products
def test_pop_up_products_router(browser):
    popup = HomePage(browser)
    popup.go_to()
    router = popup.find_elements_products_router_pop_up()

    assert router.title == 'VPN router configuration - setup vpn on router - Planet VPN'


@pytest.mark.products
def test_pop_up_products_dns_leak_test(browser):
    popup = HomePage(browser)
    popup.go_to()
    dns_leak_test = popup.find_elements_dns_leak_pop_up()

    assert dns_leak_test.title == 'DNS check - Online DNS propagation check - Planet VPN'


@pytest.mark.products
def test_pop_up_products_ios(browser):
    popup = HomePage(browser)
    popup.go_to()
    ios = popup.find_elements_products_ios_pop_up()

    assert ios.title == 'Free VPN iOS - VPN for iPhone and iPad without limits - Planet VPN'


@pytest.mark.products
def test_pop_up_products_firefox(browser):
    popup = HomePage(browser)
    popup.go_to()
    firefox = popup.find_elements_products_firefox_po_up()

    assert firefox.title == 'Free VPN for Firefox - download firefox vpn extension - Planet VPN'


@pytest.mark.products
def test_pop_up_products_macos(browser):
    popup = HomePage(browser)
    popup.go_to()
    macos = popup.find_elements_products_macos_pop_up()

    assert macos.title == 'Free VPN for Mac - best client for macOS - Planet VPN'


@pytest.mark.products
def test_pop_up_products_open_vpn(browser):
    popup = HomePage(browser)
    popup.go_to()
    openvpn = popup.find_elements_products_open_vpn_pop_up()

    assert openvpn.title == 'OpenVPN configurations - client configurations for Windows - Planet VPN'


@pytest.mark.products
def test_pop_up_products_web_rtc(browser):
    popup = HomePage(browser)
    popup.go_to()
    web_rtc = popup.find_elements_products_web_rtc_pop_up()

    assert web_rtc.title == 'WebRTC leak shield - online leak test - Planet VPN'


@pytest.mark.products
def test_pop_up_products_edge(browser):
    popup = HomePage(browser)
    popup.go_to()
    edge = popup.find_elements_products_edge()

    assert edge.title == 'Free VPN Edge - download extension for Edge - Planet VPN'


@pytest.mark.products
def test_pop_up_products_linux(browser):
    popup = HomePage(browser)
    popup.go_to()
    linux = popup.find_elements_products_linux()

    assert linux.title == 'Free VPN for Linux - best for Linux without registration - Planet VPN'


@pytest.mark.products
def test_pop_up_products_virus_scan(browser):
    popup = HomePage(browser)
    popup.go_to()
    virus_scan = popup.find_elements_products_virus_scan_pop_up()

    assert virus_scan.title == 'Free virus scan - check for viruses by file or url - Planet VPN'


@pytest.mark.products
def test_pop_up_products_opera(browser):
    popup = HomePage(browser)
    popup.go_to()
    opera = popup.find_elements_products_opera_pop_up()

    assert opera.title == 'Free VPN for Opera - best free Opera extension - Planet VPN'


@pytest.mark.products
def test_pop_up_products_what_is_my_ip(browser):
    popup = HomePage(browser)
    popup.go_to()
    what_is_my_ip = popup.find_elements_products_what_is_my_ip_pop_up()

    assert what_is_my_ip.title == 'What is my IP? Check my IP online - Planet VPN'


@pytest.mark.products
def test_pop_up_products_yandex(browser):
    popup = HomePage(browser)
    popup.go_to()
    yandex = popup.find_elements_product_yandex_pop_up()

    assert yandex.title == 'Free VPN for Yandex Browser - vpn extension - Planet VPN'


@pytest.mark.products
def test_pop_up_products_password_generator(browser):
    popup = HomePage(browser)
    popup.go_to()
    password_generator = popup.find_elements_products_password_generator_pop_up()

    assert password_generator.title == 'Password generator - random and strong password - Planet VPN'


@pytest.mark.products
def tes_pop_up_products_close(browser):
    popup = HomePage(browser)
    popup.go_to()
    close_pop_up = popup.find_elements_product_close_pop_up()

    assert close_pop_up, 'Pop-up should have been closed'


'''Premium button test'''


@pytest.mark.premium
def test_premium_button(browser):
    premium = HomePage(browser)
    premium.go_to()
    premium_button = premium.find_elements_premium_button()

    assert premium_button.title == 'Buy best VPN - buy a vpn service subscription - Planet VPN'


'''Planet vpn logo test'''


@pytest.mark.planet_vpn
def test_planet_vpn(browser):
    planet_vpn = HomePage(browser)
    planet_vpn.go_to()
    planet_vpn_button = planet_vpn.find_elements_planet_vpn_logo()

    assert planet_vpn_button.title == 'Free VPN – best free online VPN, fast and secure | Planet VPN'


@pytest.mark.download
def test_download_button(browser):
    download_button = HomePage(browser)
    download_button.go_to()
    download = download_button.find_elements_download_vpn()

    assert download.title == 'Free VPN Download - For all Devices with no Limits | Planet VPN'


@pytest.mark.login
def test_login_button(browser):
    login_button = HomePage(browser)
    login_button.go_to()
    login = login_button.find_elements_login()

    assert login.title == 'Login'


@pytest.mark.localizations
def test_localizations_button_pt(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    localisations = localisations_button.find_elements_localizations_pt()

    assert localisations.title == 'Free VPN e proxy - VPN gratis sem anúncios ou limites | Planet VPN'


@pytest.mark.localizations
def test_localizations_button_ro(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    localisations = localisations_button.find_elements_localizations_ro()

    assert localisations.title == 'Free VPN - cel mai bun VPN online gratuit, rapid și sigur | Planet VPN'


@pytest.mark.localizations
def test_localizations_button_ru(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    localisations = localisations_button.find_elements_localizations_ru()

    assert localisations.title == 'Бесплатный VPN - ВПН без лимитов и регистрации | Planet VPN'


@pytest.mark.localizations
def test_localizations_button_sv(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    localisations = localisations_button.find_elements_localizations_sv()

    assert localisations.title == 'Gratis VPN och proxy - gratis vpn utan annonser | Planet VPN'


@pytest.mark.localizations
def test_localizations_button_th(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    localisations = localisations_button.find_elements_localizations_th()

    assert localisations.title == 'Free VPN & พร็อกซี่ - ไม่มีโฆษณา จำกัด ความเร็วและการรับส่งข้อมูล | Planet VPN'


@pytest.mark.localizations
def test_localizations_button_tl(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    localisations = localisations_button.find_elements_localizations_tl()

    assert localisations.title == 'Libreng VPN – pinakamahusay na libreng online na VPN, mabilis at secure | Planet VPN'


@pytest.mark.localizations
def test_localizations_button_tr(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    localisations = localisations_button.find_elements_localizations_tr()

    assert localisations.title == 'Free VPN ve Proxy - reklamsız ve sınırsız en iyi ücretsiz vpn | Planet VPN'


@pytest.mark.localizations
def test_localizations_button_ua(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    localisations = localisations_button.find_elements_localizations_ua()

    assert localisations.title == 'VPN безкоштовно - без реєстрації, обмежень швидкості та трафіку | Planet VPN'


@pytest.mark.localizations
def test_localizations_button_ar(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    localisations = localisations_button.find_elements_localizations_ar()

    assert localisations.title == 'أفضل برنامج VPN مجاني بدون اعلانات وموثوق به من 10 مليون مستخدم'


@pytest.mark.localizations
def test_localizations_button_cs(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    localisations = localisations_button.find_elements_localizations_cs()

    assert localisations.title == 'Zdarma VPN - nejlepší Free online VPN, rychlá a bezpečná | Planet VPN'


@pytest.mark.localizations
def test_localizations_button_de(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    localisations = localisations_button.find_elements_localizations_de()

    assert localisations.title == 'VPN Kostenlos – das beste Free VPN ohne Grenzen | Planet VPN'


@pytest.mark.localizations
def test_localizations_button_en(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    localisations = localisations_button.find_elements_localizations_en()

    assert localisations.title == 'Free VPN – best free online VPN, fast and secure | Planet VPN'


@pytest.mark.localizations
def test_localizations_button_es(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    localisations = localisations_button.find_elements_localizations_es()

    assert localisations.title == 'VPN Gratis y Proxy: Free VPN sin restricciones ni límites - Planet VPN'


@pytest.mark.localizations
def test_localizations_button_fr(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    localisations = localisations_button.find_elements_localizations_fr()

    assert localisations.title == 'VPN gratuit - le meilleur free VPN sans limites | Planet VPN'


@pytest.mark.localizations
def test_localizations_button_id(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    localisations = localisations_button.find_elements_localizations_id()

    assert localisations.title == 'VPN Gratis – VPN online gratis terbaik, cepat dan aman | VPN Planet'


@pytest.mark.localizations
def test_localizations_button_it(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    localisations = localisations_button.find_elements_localizations_it()

    assert localisations.title == 'VPN Gratis: la migliore VPN online Gratis, veloce e sicura - Planet VPN'


@pytest.mark.localizations
def test_localizations_button_pl(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    localisations = localisations_button.find_elements_localizations_pl()

    assert localisations.title == 'Darmowy VPN – najlepszy VPN online, szybki i bezpieczny | Planet VPN'
