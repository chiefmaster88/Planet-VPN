from home_page.page_object import HomePage
import pytest

'''Why VPN test'''


@pytest.mark.pop_up
def test_pop_up_why_vpn_what_is_vpn(browser):
    popup = HomePage(browser)
    popup.go_to()
    what_is_a_vpn = popup.find_elemts_why_vpn_wats_is_vpn()
    assert what_is_a_vpn.text == "What is a VPN and How to Use a VPN?"


@pytest.mark.pop_up
def test_pop_up_why_vpn_no_logs(browser):
    popup = HomePage(browser)
    popup.go_to()
    no_logs = popup.find_elements_why_vpn_no_logs()
    assert no_logs.text == 'VPN without logs'


@pytest.mark.pop_up
def test_pop_up_why_vpn_what_is_proxy(browser):
    popup = HomePage(browser)
    popup.go_to()
    what_is_proxy = popup.find_elements_why_vpn_what_is_proxy()
    assert what_is_proxy.text == 'Proxy Types, Their Features And Everything There Is To Know About Them'


@pytest.mark.pop_up
def test_pop_up_why_vpn_our_vpn_network(browser):
    popup = HomePage(browser)
    popup.go_to()
    our_vpn_network = popup.find_elements_why_vpn_our_vpn_network()
    assert our_vpn_network.text == 'Secure VPN servers around the world'


@pytest.mark.pop_up
def test_pop_up_why_vpn_about_vpn_protocols(browser):
    popup = HomePage(browser)
    popup.go_to()
    about_vpn_protocols = popup.find_elemets_why_vpn_about_vpn_protocols()
    assert about_vpn_protocols.text == 'VPN Protocols: What Are They And Where They Are Used'


@pytest.mark.pop_up
def test_pop_up_why_vpn_free_vpn(browser):
    popup = HomePage(browser)
    popup.go_to()
    free_vpn = popup.find_elements_why_vpn_free_vpn()
    assert free_vpn.text == 'Download Free VPN for PC, Mobile devices and Browsers'

@pytest.mark.pop_up
def test_pop_up_why_vpn_close_pop_up(browser):
    popup = HomePage(browser)
    popup.go_to()
    close_pop_up = popup.find_elements_why_vpn_close_pop_up()
    assert close_pop_up is not None, 'something went wrong'



'''Advantages button test'''


@pytest.mark.pop_up2
def test_pop_up_advantages_access(browser):
    pop_up = HomePage(browser)
    pop_up.go_to()
    advantages_access = pop_up.find_elements_advantages_access()
    assert advantages_access.text == 'Free VPN for access Gaming and Streaming'


@pytest.mark.pop_up2
def test_pop_up_advantages_steam(browser):
    pop_up = HomePage(browser)
    pop_up.go_to()
    advantages_steam = pop_up.find_elements_advantages_steam()
    assert advantages_steam.text == 'How to use a VPN to unlock Steam Games'

@pytest.mark.pop_up2
def test_pop_up_advantages_prebenting_surveillance(browser):
    pop_up = HomePage(browser)
    pop_up.go_to()
    advantages_preventing_surveillance = pop_up.find_elements_advantages_preventing_surveillance()
    assert advantages_preventing_surveillance.text == 'Free VPN for Internet Protection'

@pytest.mark.pop_up2
def test_pop_up_advantages_secure_wi_fi(browser):
    pop_up = HomePage(browser)
    pop_up.go_to()
    advantages_secure_wi = pop_up.find_elements_advantages_secure_wi_fi()
    assert advantages_secure_wi.text == 'Free VPN for public Wi-Fi'

@pytest.mark.pop_up2
def test_pop_up_advantages_streaming(browser):
    popup = HomePage(browser)
    popup.go_to()
    advantages_streaming = popup.find_elements_advantages_streaming()
    assert advantages_streaming.text == 'Live streaming VPN - Watch any online Live Streaming'

@pytest.mark.pop_up2
def test_pop_up_advantages_airline_tickets(browser):
    popup = HomePage(browser)
    popup.go_to()
    advantages_airline_tickets = popup.find_elements_advantages_airline_tickets()
    assert advantages_airline_tickets.text == 'Save on airline tickets with Planet VPN!'

@pytest.mark.pop_up2
def test_pop_up_advantages_online_anonymity(browser):
    popup = HomePage(browser)
    popup.go_to()
    advantages_online_anonymity = popup.find_elements_advantages_online_anonymity()
    assert advantages_online_anonymity.text == 'Anonymous internet surfing and browsing with Free VPN'

@pytest.mark.pop_up2
def test_pop_up_advantages_data_encryption(browser):
    popup = HomePage(browser)
    popup.go_to()
    advantages_data_encryption = popup.find_elements_advantages_data_encryption()
    assert advantages_data_encryption.text == 'Data encryption and security with free VPN'