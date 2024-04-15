from home_page.navbar.page_object import HomePage
import pytest

'''Why VPN test'''


@pytest.mark.why_vpn
def test_why_vpn_why_vpn_what_is_vpn(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'What is a VPN and How to Use a VPN: A Comprehensive Guide'

    assert popup.find_elements_why_vpn_wats_is_vpn(expected_title)



@pytest.mark.why_vpn
def test_pop_up_why_vpn_no_logs(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'Best no logs VPN - free vpn no logs - Planet VPN'

    assert popup.find_elements_why_vpn_no_logs(expected_title)




@pytest.mark.why_vpn
def test_pop_up_why_vpn_what_is_proxy(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'Proxy Types: Features and All You Need to Know | Planet VPN'
    assert popup.find_elements_why_vpn_what_is_proxy(expected_title)




@pytest.mark.why_vpn
def test_pop_up_why_vpn_our_vpn_network(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'VPN servers - list of free vpn servers around the world - Planet VPN'
    assert popup.find_elements_why_vpn_our_vpn_network(expected_title)



@pytest.mark.why_vpn
def test_pop_up_why_vpn_about_vpn_protocols(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'VPN Protocols: Everything You Need To Know | Planet VPN'

    assert popup.find_elemets_why_vpn_about_vpn_protocols(expected_title)

#
#
@pytest.mark.why_vpn
def test_pop_up_why_vpn_free_vpn(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'Free VPN Download - For all Devices with no Limits | Planet VPN'
    assert popup.find_elements_why_vpn_free_vpn(expected_title)



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
    expected_title = 'Free VPN for access Gaming and Streaming | Planet VPN'

    assert pop_up.find_elements_advantages_access_pop_up(expected_title)




@pytest.mark.advantages
def test_pop_up_advantages_steam(browser):
    pop_up = HomePage(browser)
    pop_up.go_to()
    expected_title = 'Free VPN for Steam - How to use a VPN to unlock Steam - Planet VPN'

    assert pop_up.find_elements_advantages_steam(expected_title)




@pytest.mark.advantages
def test_pop_up_advantages_preventing_surveillance(browser):
    pop_up = HomePage(browser)
    pop_up.go_to()
    expected_title = 'Free VPN for Internet Protection - Protect your data online'

    assert pop_up.find_elements_advantages_preventing_surveillance(expected_title)




#
@pytest.mark.advantages
def test_pop_up_advantages_secure_wi_fi(browser):
    pop_up = HomePage(browser)
    pop_up.go_to()
    expected_title = 'Free VPN for public WiFi - Secure Your Wi-Fi Connection - Planet VPN'

    assert pop_up.find_elements_advantages_secure_wi_fi(expected_title)




#
#
@pytest.mark.advantages
def test_pop_up_advantages_streaming(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'Live streaming With free VPN - Live Sports With a VPN - Planet VPN'

    assert popup.find_elements_advantages_streaming(expected_title)




@pytest.mark.advantages
def test_pop_up_advantages_airline_tickets(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'Save Money on Flights With a free VPN - Planet VPN'

    assert popup.find_elements_advantages_airline_tickets(expected_title)




@pytest.mark.advantages
def test_pop_up_advantages_online_anonymity(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'Free VPN for anonymous browsing and surfing - Planet VPN'

    assert popup.find_elements_advantages_online_anonymity(expected_title)




@pytest.mark.advantages
def test_pop_up_advantages_data_encryption(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'Data encryption with free VPN - Planet VPN'

    assert popup.find_elements_advantages_data_encryption(expected_title)




@pytest.mark.advantages
def test_pop_up_advantages_music(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'VPN for downloading and listen music - your favorite music with VPN'

    assert popup.find_elements_advantages_music(expected_title)




@pytest.mark.advantages
def test_pop_up_advantages_booking_hotels(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'Save on Hotels booking with free VPN - How to save money'

    assert popup.find_elements_advantages_booking_hotels(expected_title)




@pytest.mark.advantages
def test_pop_up_advantages_change_or_hide_ip(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'How to Change and Hide IP address with a free VPN - Planet VPN'

    assert popup.find_elements_advantages_change_or_hid_ip(expected_title)




@pytest.mark.advantages
def test_pop_up_advantages_car_rentals(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'Save money renting cars with free VPN - ways to save - Free VPN'

    assert popup.find_elements_advantages_car_rentals(expected_title)




@pytest.mark.advantages
def test_pop_up_advantages_car_torrents(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'Free P2P VPN - Download and Set Up VPN'

    assert popup.find_elements_advantages_torrents(expected_title)




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
    expected_title = 'Free VPN for Android - download best fast and safe VPN - Planet VPN'

    assert popup.find_elements_products_android_pop_up(expected_title)




@pytest.mark.products
def test_pop_up_products_chrome(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'Free VPN for Chrome - download vpn Chrome extension - Planet VPN'

    assert popup.find_elements_products_chrome_pop_up(expected_title)




@pytest.mark.products
def test_pop_up_products_windows(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'Free VPN for Windows - download without any limits - Planet VPN'

    assert popup.find_elements_products_windows_pop_up(expected_title)


@pytest.mark.products
def test_pop_up_products_router(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'VPN router configuration - setup vpn on router - Planet VPN'

    assert popup.find_elements_products_router_pop_up(expected_title)




@pytest.mark.products
def test_pop_up_products_dns_leak_test(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'DNS check - Online DNS propagation check - Planet VPN'

    assert popup.find_elements_dns_leak_pop_up(expected_title)




@pytest.mark.products
def test_pop_up_products_ios(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'Free VPN iOS - VPN for iPhone and iPad without limits - Planet VPN'

    assert popup.find_elements_products_ios_pop_up(expected_title)




@pytest.mark.products
def test_pop_up_products_firefox(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'Free VPN for Firefox - download firefox vpn extension - Planet VPN'

    assert popup.find_elements_products_firefox_po_up(expected_title)




@pytest.mark.products
def test_pop_up_products_macos(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'Free VPN for Mac - best client for macOS - Planet VPN'

    assert popup.find_elements_products_macos_pop_up(expected_title)




@pytest.mark.products
def test_pop_up_products_open_vpn(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'OpenVPN configurations - client configurations for Windows - Planet VPN'

    assert popup.find_elements_products_open_vpn_pop_up(expected_title)




@pytest.mark.products
def test_pop_up_products_web_rtc(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'WebRTC leak shield - online leak test - Planet VPN'

    assert popup.find_elements_products_web_rtc_pop_up(expected_title)




@pytest.mark.products
def test_pop_up_products_edge(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'Free VPN Edge - download extension for Edge - Planet VPN'

    assert popup.find_elements_products_edge(expected_title)




@pytest.mark.products
def test_pop_up_products_linux(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'Free VPN for Linux - best for Linux without registration - Planet VPN'

    assert popup.find_elements_products_linux(expected_title)




@pytest.mark.products
def test_pop_up_products_virus_scan(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'Free virus scan - check for viruses by file or url - Planet VPN'

    assert popup.find_elements_products_virus_scan_pop_up(expected_title)




@pytest.mark.products
def test_pop_up_products_opera(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'Free VPN for Opera - best free Opera extension - Planet VPN'

    assert popup.find_elements_products_opera_pop_up(expected_title)




@pytest.mark.products
def test_pop_up_products_what_is_my_ip(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'What is my IP? Check my IP online - Planet VPN'

    assert popup.find_elements_products_what_is_my_ip_pop_up(expected_title)




@pytest.mark.products
def test_pop_up_products_yandex(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'Free VPN for Yandex Browser - vpn extension - Planet VPN'

    assert popup.find_elements_product_yandex_pop_up(expected_title)




@pytest.mark.products
def test_pop_up_products_password_generator(browser):
    popup = HomePage(browser)
    popup.go_to()
    expected_title = 'Password generator - random and strong password - Planet VPN'

    assert popup.find_elements_products_password_generator_pop_up(expected_title)




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
    expected_title = 'Buy best VPN - buy a vpn service subscription - Planet VPN'

    assert premium.find_elements_premium_button(expected_title)




'''Planet vpn logo test'''


@pytest.mark.planet_vpn
def test_planet_vpn(browser):
    planet_vpn = HomePage(browser)
    planet_vpn.go_to()
    expected_title = 'Free VPN – best free online VPN, fast and secure | Planet VPN'

    assert planet_vpn.find_elements_planet_vpn_logo(expected_title)


@pytest.mark.download
def test_download_button(browser):
    download_button = HomePage(browser)
    download_button.go_to()
    expected_title = 'Free VPN Download - For all Devices with no Limits | Planet VPN'

    assert download_button.find_elements_download_vpn(expected_title)




@pytest.mark.login
def test_login_button(browser):
    login_button = HomePage(browser)
    login_button.go_to()
    expected_title = 'Login'

    assert login_button.find_elements_login(expected_title)




@pytest.mark.localizations
def test_localizations_button_pt(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    expected_title = 'Free VPN e proxy - VPN gratis sem anúncios ou limites | Planet VPN'

    assert localisations_button.find_elements_localizations_pt(expected_title)




@pytest.mark.localizations
def test_localizations_button_ro(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    expected_title = 'Free VPN - cel mai bun VPN online gratuit, rapid și sigur | Planet VPN'

    assert localisations_button.find_elements_localizations_ro(expected_title)




@pytest.mark.localizations
def test_localizations_button_ru(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    expected_title = 'Бесплатный VPN - ВПН без лимитов и регистрации | Planet VPN'

    assert localisations_button.find_elements_localizations_ru(expected_title)




@pytest.mark.localizations
def test_localizations_button_sv(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    expected_title = 'Gratis VPN och proxy - gratis vpn utan annonser | Planet VPN'

    assert localisations_button.find_elements_localizations_sv(expected_title)




@pytest.mark.localizations
def test_localizations_button_th(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    expected_title = 'Free VPN & พร็อกซี่ - ไม่มีโฆษณา จำกัด ความเร็วและการรับส่งข้อมูล | Planet VPN'

    assert localisations_button.find_elements_localizations_th(expected_title)




@pytest.mark.localizations
def test_localizations_button_tl(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    expected_title = 'Libreng VPN – pinakamahusay na libreng online na VPN, mabilis at secure | Planet VPN'

    assert localisations_button.find_elements_localizations_tl(expected_title)




@pytest.mark.localizations
def test_localizations_button_tr(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    expected_title = 'Free VPN ve Proxy - reklamsız ve sınırsız en iyi ücretsiz vpn | Planet VPN'

    assert localisations_button.find_elements_localizations_tr(expected_title)




@pytest.mark.localizations
def test_localizations_button_ua(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    expected_title = 'VPN безкоштовно - без реєстрації, обмежень швидкості та трафіку | Planet VPN'

    assert localisations_button.find_elements_localizations_ua(expected_title)




@pytest.mark.localizations
def test_localizations_button_ar(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    expected_title = 'أفضل برنامج VPN مجاني بدون اعلانات وموثوق به من 10 مليون مستخدم'

    assert localisations_button.find_elements_localizations_ar(expected_title)




@pytest.mark.localizations
def test_localizations_button_cs(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    expected_title = 'Zdarma VPN - nejlepší Free online VPN, rychlá a bezpečná | Planet VPN'

    assert localisations_button.find_elements_localizations_cs(expected_title)




@pytest.mark.localizations
def test_localizations_button_de(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    expected_title = 'VPN Kostenlos – das beste Free VPN ohne Grenzen | Planet VPN'

    assert localisations_button.find_elements_localizations_de(expected_title)




@pytest.mark.localizations
def test_localizations_button_en(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    expected_title = 'Free VPN – best free online VPN, fast and secure | Planet VPN'

    assert localisations_button.find_elements_localizations_en(expected_title)




@pytest.mark.localizations
def test_localizations_button_es(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    expected_title = 'VPN Gratis y Proxy: Free VPN sin restricciones ni límites - Planet VPN'

    assert localisations_button.find_elements_localizations_es(expected_title)




@pytest.mark.localizations
def test_localizations_button_fr(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    expected_title = 'VPN gratuit - le meilleur free VPN sans limites | Planet VPN'

    assert localisations_button.find_elements_localizations_fr(expected_title)




@pytest.mark.localizations
def test_localizations_button_id(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    expected_title = 'VPN Gratis – VPN online gratis terbaik, cepat dan aman | VPN Planet'

    assert localisations_button.find_elements_localizations_id(expected_title)




@pytest.mark.localizations
def test_localizations_button_it(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    expected_title = 'VPN Gratis: la migliore VPN online Gratis, veloce e sicura - Planet VPN'

    assert localisations_button.find_elements_localizations_it(expected_title)




@pytest.mark.localizations
def test_localizations_button_pl(browser):
    localisations_button = HomePage(browser)
    localisations_button.go_to()
    expected_title = 'Darmowy VPN – najlepszy VPN online, szybki i bezpieczny | Planet VPN'

    assert localisations_button.find_elements_localizations_pl(expected_title)


