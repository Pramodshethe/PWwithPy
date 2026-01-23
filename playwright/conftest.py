import asyncio
from idlelib.rpc import request_queue

import pytest
from playwright.sync_api import Playwright

# @pytest.fixture(scope="session")
# def event_loop():
#     """Create an instance of the default event loop for each test case."""
#     loop = asyncio.get_event_loop_policy().new_event_loop()
#     yield loop
#     loop.close()


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )
    parser.addoption(
        "--url_link", action="store", default="url", help="server selection"
    )

@pytest.fixture(scope="session")
def user_credentials(request):
    return request.user_credentials

@pytest.fixture #(scope="session")
def browser_instance(playwright: Playwright, request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == 'firefox':
        browser = playwright.firefox.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()
    yield  page
    context.close()
    browser.close()