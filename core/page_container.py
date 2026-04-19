from pages.auth_page import AuthPage
from pages.home_page import HomePage
from pages.nav_bar_upper import NavBarUpper
from pages.signup_page import SignupPage


class Pages:
    def __init__(self, page, base_url):
        self.page = page
        self.base_url = base_url

        self.home = HomePage(page, base_url)
        self.nav_bar_upper = NavBarUpper(page)
        self.auth = AuthPage(page)
        self.signup = SignupPage(page)
