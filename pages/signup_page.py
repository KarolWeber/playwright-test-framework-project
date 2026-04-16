from playwright.sync_api import Page


class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        # Account
        self._password = page.locator('[data-qa="password"]')
        # Personal
        self._first_name = page.locator('[data-qa="first_name"]')
        self._last_name = page.locator('[data-qa="last_name"]')
        self._birth_day = page.locator('[data-qa="days"]')
        self._birth_month = page.locator('[data-qa="months"]')
        self._birth_year = page.locator('[data-qa="years"]')
        # Addresses
        self._company = page.locator('[data-qa="company"]')
        self._primary_address = page.locator('[data-qa="address"]')
        self._secondary_address = page.locator('[data-qa="address2"]')
        self._country = page.locator('[data-qa="country"]')
        self._state = page.locator('[data-qa="state"]')
        self._city = page.locator('[data-qa="city"]')
        self._zipcode = page.locator('[data-qa="zipcode"]')
        # Consents
        self._newsletter = page.locator('input[name="newsletter"]')
        self._marketing = page.locator('input[name="optin"]')
        # Contact
        self._mobile_number = page.locator('[data-qa="mobile_number"]')
        # Buttons
        self._create_account_button = page.locator('[data-qa="create-account"]')
        self._continue_button = page.locator('[data-qa="continue-button"]')

    def _select_gender(self, gender):
        return self.page.locator(f'input[value="{gender}"]')

    def fill_out_the_signup_form(self, user_data: dict):
        self._select_gender(user_data['gender']).check()
        self._password.fill(user_data['password'])
        self._birth_day.select_option(user_data['birth_day'])
        self._birth_month.select_option(user_data['birth_month'])
        self._birth_year.select_option(user_data['birth_year'])
        if user_data['newsletter']:
            self._newsletter.check()
        if user_data['marketing']:
            self._marketing.check()
        self._first_name.fill(user_data['first_name'])
        self._last_name.fill(user_data['last_name'])
        self._company.fill(user_data['company'])
        self._primary_address.fill(user_data['primary_address'])
        self._secondary_address.fill(user_data['secondary_address'])
        self._country.select_option(user_data['country'])
        self._state.fill(user_data['state'])
        self._city.fill(user_data['city'])
        self._zipcode.fill(user_data['zipcode'])
        self._mobile_number.fill(user_data['mobile_number'])

    def click_create_account(self):
        self._create_account_button.click()

    def click_continue(self):
        self._continue_button.click()
