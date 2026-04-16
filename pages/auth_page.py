from playwright.sync_api import Page


class AuthPage:
    def __init__(self, page: Page):
        self.page = page
        # Login form
        self._login_email = page.locator('[data-qa="login-email"]')
        self._login_password = page.locator('[data-qa="login-password"]')
        self._login_button = page.locator('[data-qa="login-button"]')
        # Signup form
        self._signup_name = page.locator('[data-qa="signup-name"]')
        self._signup_email = page.locator('[data-qa="signup-email"]')
        self._signup_button = page.locator('[data-qa="signup-button"]')

    def login_password_fill(self, credentials: dict):
        self._login_email.fill(credentials['email'])
        self._login_password.fill(credentials['password'])

    def click_login(self):
        self._login_button.click()

    def signup_name_email_fill(self, user_data: dict):
        self._signup_name.fill(user_data['name'])
        self._signup_email.fill(user_data['email'])

    def click_signup(self):
        self._signup_button.click()

    def login_error_message(self):
        return self.page.get_by_text('Your email or password is incorrect!')

    def signup_error_message(self):
        return self.page.get_by_text('Email Address already exist!')
