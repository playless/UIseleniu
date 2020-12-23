import pytest

from webSelenium.pages.mainPage import MainPage


class TestContactsPage:
    def setup_class(self):
        self.contacts=MainPage().goto_contacts()
    def teardown_class(self):
        pass


    def testone(self):
        list1=self.contacts.get_member_list()
        print(list1)
        assert "potato1" in list1
    @pytest.mark.parametrize("name,name_u",[("韩国","hanguo"),("赵国","zhaoguo")])
    def test_add_patry(self,name,name_u):
        self.contacts.add_patry(name,name_u)