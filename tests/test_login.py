from playwright.sync_api import expect
from pages.home import HomePage
from pages.nav_bar_upper import NavBarUpper
from flows.auth import AuthFlows


def test_user_can_login_with_valid_credentials(page, base_url, user_credentials):
    home_page = HomePage(page, base_url)
    nav_bar = NavBarUpper(page)
    auth = AuthFlows(page, user_credentials)

    nav_bar.go_to_auth()
    auth.user_login()

    logged_in_as = home_page.logged_in_as()
    expect(logged_in_as).to_contain_text(user_credentials['name'])
