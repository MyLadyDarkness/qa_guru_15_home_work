import pytest
from selene import browser

# @pytest.fixture(scope="function", autouse=True)
# def selenoid_browser():
#     browser.open("https://github.com/")
#
#     #desktop
#     #browser.config.window_height = 724
#     #browser.config.window_width = 982
#
#     #mobile iPhone14 Pro Max
#     #browser.config.window_height = 932
#     #browser.config.window_width = 430
#
#     yield
#
#     browser.quit()

# @pytest.fixture(params=["Desktop", "Mobile"])
# def browser_size(request):
#     #browser.config.base_url = 'https://demoqa.com'
#     #browser.open("https://github.com/")
#     if request.param == "Desktop":
#         browser.config.window_height = 724
#         browser.config.window_width = 982
#         return "Desktop"
#     if request.param == "Mobile":
#         browser.config.window_height = 932
#         browser.config.window_width = 430
#         return "Mobile"
#
#     yield
#
#     browser.quit()
#
# # def test_with_parametrized_fixture(browser):
# #     pass

import pytest
from selene import browser


@pytest.fixture
def desktop():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield
    browser.quit()


@pytest.fixture
def mobile():
    browser.config.window_width = 400
    browser.config.window_height = 700

    yield
    browser.quit()


@pytest.fixture(params=['desktop', 'mobile'])
def browser_size(request):
    if request.param == 'desktop':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    else:
        browser.config.window_width = 400
        browser.config.window_height = 700

    yield
    browser.quit()


@pytest.fixture(params=[(1920, 1080), (400, 700)])
def driver_setup(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
