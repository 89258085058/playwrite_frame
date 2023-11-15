from pages.example_page import ExamplePage


class TestExample:
    def test_example(self, pw):
        page = ExamplePage(pw)
        page.go_to_main_page()
