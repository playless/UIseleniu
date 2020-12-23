from webSelenium.pages.mainPage import MainPage


class TestAddMember:
    def setup_class(self):
        self.main=MainPage()
    # def teardown(self):
    #     self.main.quite()
    def test_save(self):
        self.main.goto_AddMemberPage().save()
    def test_save_faile(self):
        err0_list=self.main.goto_AddMemberPage().save_faile()
        assert "该帐号已被“potato1”占有" in err0_list