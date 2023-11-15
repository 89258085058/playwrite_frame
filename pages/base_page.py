from test.conftest import pw


class BasePage:

    def __init__(self, pw):
        self.pw = pw
