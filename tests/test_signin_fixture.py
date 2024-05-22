from pages.click_button import signin
from pages.open_page import page


def test_signin_desktop(desktop):
    page.open_start_page()
    signin.click_desktop()


def test_signin_mobile(mobile):
    page.open_start_page()
    signin.click_mobile()
