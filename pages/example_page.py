from pages.base_page import BasePage


class ExamplePage(BasePage):

    def __int__(self, pw):
        super().__init__(pw)

    def go_to_main_page(self):
        self.pw.goto("https://playwright-todomvc.antonzimaiev.repl.co/#/")
        self.pw.get_by_placeholder("What needs to be done?").click()
        self.pw.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
        self.pw.get_by_placeholder("What needs to be done?").press("Enter")
