class AuthLocators:
    class Login:
        EMAIL = {"locator": "form",
                 "has_text": "Login",
                 "placeholder": "Email address"}
        PASSWORD = {"role": "textbox",
                    "name": "Password"}
        LOGIN_BUTTON = {"role": "button",
                        "name": "Login"}
