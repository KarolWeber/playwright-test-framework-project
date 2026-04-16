from playwright.sync_api import expect


def test_user_can_login_and_logout(app, user_credentials):
    app.pages.home.open()
    app.flows.login.login(user_credentials)

    expect(app.pages.home.logged_in_as_label()).to_contain_text(user_credentials['name'])
    app.pages.home.click_logout()

    expect(app.page).to_have_url(f'{app.base_url}/login')


def test_user_login_with_invalid_password(app, user_credentials):
    expected_login_message = 'Your email or password is incorrect!'
    app.pages.home.open()
    app.flows.login.login({
        'email': user_credentials['email'],
        'password': 'invalid_password'})

    expect(app.pages.auth.login_error_message()).to_contain_text(expected_login_message)
