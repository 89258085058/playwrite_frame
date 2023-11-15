from pages.base_page import BasePage
from locators.main_locators import MainLocators


class ExamplePage(BasePage):

    def __int__(self, pw):
        super().__init__(pw)

    def go_to_main_page(self):
        self.pw.get_by_placeholder(MainLocators.input_name).click()
        self.pw.get_by_placeholder(MainLocators.input_name).fill("Создать первый сценарий playwright")
        self.pw.get_by_placeholder(MainLocators.input_name).press("Enter")
