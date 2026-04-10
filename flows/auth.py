from playwright.sync_api import Page
from pages.auth import Auth

class AuthFlows:
    def __init__(self, page: Page, credentials):
        self.page = page
        self.credentials = credentials

    def user_login(self):
        auth = Auth(self.page)
        auth.login_fill_in_email(self.credentials['email'])
        auth.login_fill_in_password(self.credentials['password'])
        auth.login_click_the_button()