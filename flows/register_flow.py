import allure

from core.pages import Pages


class RegisterFlow:
    def __init__(self, pages: Pages):
        self.pages = pages

    def start_register(self, user_data: dict):
        with allure.step('Go to signup/login page'):
            self.pages.nav_bar_upper.go_to_auth()
        with allure.step('Fill in the name and email'):
            self.pages.auth.signup_name_email_fill(user_data)
        with allure.step('Click signup'):
            self.pages.auth.click_signup()

    def finish_register(self, user_data: dict):
        with allure.step('Fill out the registration form'):
            self.pages.signup.fill_out_the_signup_form(user_data)
        with allure.step('Click create account'):
            self.pages.signup.click_create_account()
