from playwright.sync_api import Page

from locators.nav_bar_upper import UpperNavBarLocators


class NavBarUpper:
    def __init__(self, page: Page):
        self.page = page

    def go_to_auth(self):
        self.page.get_by_role(**UpperNavBarLocators.AUTH).click()
