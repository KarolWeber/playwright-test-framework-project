from flows.login_flow import LoginFlow
from flows.register_flow import RegisterFlow


class Flows:
    def __init__(self, pages):
        self.page = pages
        self.login = LoginFlow(pages)
        self.register = RegisterFlow(pages)
