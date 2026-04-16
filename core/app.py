from core.flows import Flows
from core.pages import Pages


class App:
    def __init__(self, page, base_url):
        self.page = page
        self.base_url = base_url

        self.pages = Pages(page, base_url)
        self.flows = Flows(self.pages)
