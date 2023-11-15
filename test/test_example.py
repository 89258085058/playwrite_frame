from pages.example_page import ExamplePage


class TestExample:
    def test_aaa(self, pw):
        page = ExamplePage(pw)
        page.go_to_main_page()
