from playwright.sync_api import Page

from locators.auth import AuthLocators


class Auth:
    def __init__(self, page: Page):
        self.page = page

    def login_fill_in_email(self, email: str = None):
        self.page.locator(AuthLocators.Login.EMAIL["locator"]).filter(
            has_text=AuthLocators.Login.EMAIL["has_text"]).get_by_placeholder(
            AuthLocators.Login.EMAIL["placeholder"]).fill(email)

    def login_fill_in_password(self, password: str = None):
        self.page.get_by_role(**AuthLocators.Login.PASSWORD).fill(password)

    def login_click_the_button(self):
        self.page.get_by_role(**AuthLocators.Login.LOGIN_BUTTON).click()
