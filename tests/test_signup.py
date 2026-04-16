import allure
from playwright.sync_api import expect


@allure.suite("User signup")
@allure.title("User signup with correct data")
def test_user_can_create_and_delete_account(app, user_data):
    account_created_message = 'Account Created!'
    account_deleted_message = 'Account Deleted!'

    app.pages.home.open_ready()
    app.flows.register.start_register(user_data)
    app.flows.register.finish_register(user_data)

    expect(app.pages.home.signup_confirmation_information()).to_contain_text(account_created_message)

    app.pages.signup.click_continue()

    app.pages.home.click_delete_account()

    expect(app.pages.home.account_deletion_confirmation_information()).to_contain_text(account_deleted_message)


@allure.suite("User signup")
@allure.title("User signup with existed email")
def test_user_try_to_signup_with_existing_email(app, user_credentials):
    expected_signup_massage = 'Email Address already exist!'

    app.pages.home.open_ready()
    app.flows.register.start_register(user_credentials)

    expect(app.pages.auth.signup_error_message()).to_contain_text(expected_signup_massage)
