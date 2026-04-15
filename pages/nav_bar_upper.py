from playwright.sync_api import Page


class NavBarUpper:
    def __init__(self, page: Page):
        self.page = page

    def go_to_auth(self):
        self.page.get_by_role('link', name='Signup / Login').click()
