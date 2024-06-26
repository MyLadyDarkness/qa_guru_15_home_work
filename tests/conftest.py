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
