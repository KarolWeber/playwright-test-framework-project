import os

import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Browser, Page

from core.app import App
from data_factory.user_factory import create_user

load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    url = os.getenv("BASE_URL")
    if not url:
        raise ValueError("BASE_URL is not set")
    return url


@pytest.fixture(scope="session")
def browser():
    pw = sync_playwright().start()
    browser = pw.chromium.launch()
    yield browser
    browser.close()
    pw.stop()


@pytest.fixture()
def page(browser: Browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()


@pytest.fixture()
def app(page: Page, base_url: str):
    return App(page, base_url)


@pytest.fixture()
def user_credentials():
    return {
        "email": os.getenv("USER_EMAIL"),
        "password": os.getenv("USER_PASSWORD"),
        "name": os.getenv("USER_NAME")
    }


@pytest.fixture()
def user_data():
    return create_user()
