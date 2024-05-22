from selene import browser


class OpenPage:

    def open_start_page(self):
        browser.open("https://github.com/")
        return self


page = OpenPage()
