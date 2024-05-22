import pytest

from pages.click_button import signin
from pages.open_page import page


@pytest.mark.parametrize("browser_size", ['desktop'], indirect=True)
def test_signin_desktop(browser_size):
    page.open_start_page()
    signin.click_desktop()


@pytest.mark.parametrize("browser_size", ['mobile'], indirect=True)
def test_signin_mobile(browser_size):
        page.open_start_page()
        signin.click_mobile()
