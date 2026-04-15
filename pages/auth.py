from playwright.sync_api import Page


class Auth:
    def __init__(self, page: Page):
        self.page = page
        self.login_email_input = page.locator('[data-qa="login-email"]')
        self.login_password_input = self.page.locator('[data-qa="login-password"]')
        self.login_button = self.page.locator('[data-qa="login-button"]')

    def login(self, credentials: dict):
        self.login_email_input.fill(credentials['email'])
        self.login_password_input.fill(credentials['password'])
        self.login_button.click()

    def login_error_message(self):
        return self.page.get_by_text('Your email or password is incorrect!')
