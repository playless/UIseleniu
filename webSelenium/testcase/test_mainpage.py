from time import sleep
from webSelenium.pages.mainPage import MainPage

class TestMainPage:
    def setup_class(self):

        self.main=MainPage()
    def teardown_class(self):
        self.main.quite()

    def test_goto_contacts(self):
        self.main.goto_contacts()
    def test_goto_AddMemberPage(self):
        self.main.goto_AddMemberPage()

