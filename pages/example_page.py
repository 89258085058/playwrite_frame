import time

from playwright.async_api import expect

from pages.base_page import BasePage
from locators.main_locators import MainLocators
from constants.constants_main import MainConstants


class ExamplePage(BasePage):

    def __int__(self, pw):
        super().__init__(pw)

    def go_to_main_page(self):
        self.input_by_locator(locator=MainLocators.email, value=MainConstants.login)
        self.input_by_locator(locator=MainLocators.password, value=MainConstants.password)
        self.pw.locator(MainLocators.entry_button).click()
        time.sleep(3)

    def assert_url_page(self):
        element = self.pw.locator(MainLocators.header)
        assert "Устройста" in element.inner_text()


