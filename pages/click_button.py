from selene import browser


class ClickButton:

    def click_desktop(self):
        browser.element('.HeaderMenu-link--sign-in').click()
        return self

    def click_mobile(self):
        browser.element('[href="/login"].d-inline-block').click()
        return self


signin = ClickButton()
