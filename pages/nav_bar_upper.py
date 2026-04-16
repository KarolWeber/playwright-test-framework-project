from playwright.sync_api import Page


class NavBarUpper:
    def __init__(self, page: Page):
        self.page = page
        self._auth_tab = page.get_by_role('link', name='Signup / Login')

    def go_to_auth(self):
        self._auth_tab.click()
