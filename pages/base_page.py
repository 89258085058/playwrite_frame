from test.conftest import pw


class BasePage:

    def __init__(self, pw):
        self.pw = pw


    def input_by_locator(self, locator: str, value: str):
        self.pw.locator(locator).click()
        self.pw.locator(locator).fill(value)


