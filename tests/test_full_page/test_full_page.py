import pytest
from home_page.page_objects.full_screen_page_objects import *
from PIL import Image


@pytest.mark.screen
def test_compare_full_page_screenshots(full_screen):
    directory = '/Users/ivanhrytsyna/PycharmProjects/vpn_planet/screen_shots_path'

    home_page = PageObject(full_screen)

    home_page.go_to('https://freevpnplanet.com/')

    home_page = home_page.take_full_page_screenshot('planeteng.png', directory)

    mirror_page = PageObject(full_screen)

    mirror_page.go_to('https://planetvpnarab.com/')

    mirror_page = mirror_page.take_full_page_screenshot('planetarab.png', directory)

    home_page_eng = Image.open(home_page)
    mirror_page_ar = Image.open(mirror_page)

    assert home_page_eng.size[1] == mirror_page_ar.size[1]

    width = min(home_page_eng.size[0], mirror_page_ar.size[0])

    for x in range(width):
        for y in range(home_page_eng.size[1]):
            pixel1 = home_page_eng.getpixel((x, y))
            pixel2 = mirror_page_ar.getpixel((x, y))
            assert pixel1 == pixel2, f'Пиксели в координатах ({x}, {y}) отличаются: {pixel1} != {pixel2}'
