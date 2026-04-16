from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page, url):
        self.page = page
        self.url = url

    def open(self):
        self.page.goto(self.url)
        self._cookies_accept_of_remove()

    def _cookies_accept_of_remove(self):
        accept_button = self.page.get_by_role('button', name='Zgadzam się')
        if accept_button.is_visible(timeout=5000):
            accept_button.click()
        else:
            consent = self.page.locator('.fc-consent-root')
            if consent.count() > 0:
                consent.first.evaluate('el => el.remove()')

    def logged_in_as_label(self):
        return self.page.get_by_text('Logged in as')

    def click_logout(self):
        self.page.get_by_role("link", name='Logout').click()

    def click_delete_account(self):
        self.page.get_by_role('link', name='Delete Account').click()

    def signup_confirmation_information(self):
        return self.page.locator('[data-qa="account-created"]')

    def account_deletion_confirmation_information(self):
        return self.page.locator('[data-qa="account-deleted"]')
