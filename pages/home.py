from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page, url):
        self.page = page
        self.url = url

    def open_main_page(self):
        self.page.goto(self.url)
        self._cookies_accept_of_remove()

    def _cookies_accept_of_remove(self):
        accept_button = self.page.get_by_role('button', name='Zgadzam się')

        if accept_button.is_visible(timeout=2000):
            accept_button.click()
        else:
            consent = self.page.locator('.fc-consent-root')
            if consent.count() > 0:
                consent.first.evaluate('el => el.remove()')

    def logged_in_as_label(self):
        return self.page.get_by_text('Logged in as')
