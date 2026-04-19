import allure
from playwright.sync_api import expect


@allure.suite("User login")
@allure.title("User login with correct credentials")
def test_user_can_login_and_logout(app, user_credentials):
    app.pages.home.open_ready()
    app.flows.login.login(user_credentials)

    expect(app.pages.home.logged_in_as_label()).to_contain_text(user_credentials['name'])
    app.pages.home.click_logout()

    expect(app.page).to_have_url(f'{app.base_url}/login')


@allure.suite("User login")
@allure.title("User login with incorrect credentials")
def test_user_login_with_invalid_password(app, user_credentials):
    expected_login_message = 'Your email or password is incorrect!'
    app.pages.home.open_ready()
    app.flows.login.login({
        'email': user_credentials['email'],
        'password': 'invalid_password'})

    expect(app.pages.auth.login_error_message()).to_contain_text(expected_login_message)
