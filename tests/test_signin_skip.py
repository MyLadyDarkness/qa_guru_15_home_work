import pytest
from selene import browser

from pages.click_button import signin
from pages.open_page import page


def test_signin_desktop(driver_setup):
    if browser.config.window_width < 1000:
        pytest.skip("mobile test")
    page.open_start_page()
    signin.click_desktop()


def test_signin_mobile(driver_setup):
    if browser.config.window_width > 1000:
        pytest.skip("desktop test")
    page.open_start_page()
    signin.click_mobile()