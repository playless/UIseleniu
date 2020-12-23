from webSelenium.pages.mainPage import MainPage


class TestContactsPage:
    def setup_class(self):
        self.contacts=MainPage().goto_contacts()
    def test_add_patry(self):
        self.contacts.add_patry()
    def testone(self):
        list1=self.contacts.get_member_list()
        print(list1)
        assert "potato1" in list1