from playwright.sync_api import Page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from locators.home import HomeLocators


class HomePage:
    def __init__(self, page: Page, url):
        self.page = page
        self.url = url

    def open_main_page(self):
        self.page.goto(self.url)
        try:
            self.cookies_accept()
        except PlaywrightTimeoutError:
            self._remove_overlay()

    def _remove_overlay(self):
        self.page.locator(".fc-consent-root").first.evaluate("el => el.remove()")

    def cookies_accept(self):
        try:
            self.page.get_by_role(**HomeLocators.ACCEPT_COOKIE).click()
        except PlaywrightTimeoutError:
            pass

    def logged_in_as_label(self):
        return self.page.get_by_text("Logged in as")
