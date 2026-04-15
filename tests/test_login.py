from playwright.sync_api import expect

from pages.auth import Auth
from pages.home import HomePage
from pages.nav_bar_upper import NavBarUpper


def test_user_can_login_with_valid_credentials(page, base_url, user_credentials):
    home_page = HomePage(page, base_url)
    nav_bar = NavBarUpper(page)
    auth = Auth(page)

    home_page.open_main_page()
    nav_bar.go_to_auth()
    auth.login(user_credentials)
    logged_in_as = home_page.logged_in_as_label()
    expect(logged_in_as).to_contain_text(user_credentials['name'])
