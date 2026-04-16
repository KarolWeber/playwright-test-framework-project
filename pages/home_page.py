from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError


class HomePage:
    def __init__(self, page: Page, url):
        self.page = page
        self.url = url

    def open(self):
        self.page.goto(self.url)

    def accept_cookies(self):
        try:
            self.page.locator("button.fc-cta-consent").click(timeout=3000)
        except PlaywrightTimeoutError:
            pass

    def open_ready(self):
        self.open()
        self.accept_cookies()

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
