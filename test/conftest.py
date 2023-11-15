import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def pw(request):
    with sync_playwright() as playwright:
        if request.config.getoption("--browser_name") == 'chrome':
            browser = playwright.chromium.launch(headless=False)
        elif request.config.getoption("--browser_name") == 'firefox':
            browser = playwright.firefox.launch(headless=False)
        elif request.config.getoption("--browser_name") == 'safari':
            browser = playwright.webkit.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        browser.close()

def pytest_addoption(parser):
    parser.addoption("--browser_name", action='store', default="chrome")

