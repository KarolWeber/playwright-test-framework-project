import allure

from core.pages import Pages


class LoginFlow:
    def __init__(self, pages: Pages):
        self.pages = pages

    def login(self, credentials: dict):
        with allure.step('Go to signup/login page'):
            self.pages.nav_bar_upper.go_to_auth()
        with allure.step('Fill in the login and password'):
            self.pages.auth.login_password_fill(credentials)
        with allure.step('Click login'):
            self.pages.auth.click_login()
