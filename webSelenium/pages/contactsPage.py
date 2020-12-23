from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from webSelenium.pages.basePage import BasePage
from webSelenium.pages.partyPage import PartyPage


class ContactsPage(BasePage):

    '''通讯录页面'''
    def add_mbmber(self):
        from webSelenium.pages.addMemberPage import AddMemberPage
        '''添加成员，并跳转到添加成员页面'''

        return AddMemberPage(self.driver)
    def add_patry(self):
        '''添加部门,并跳转部门添加成员页面'''
        self.driver.find_element(By.CSS_SELECTOR,'.member_colLeft_top_addBtnWrap ,.js_create_dropdown').click()
        self.driver.find_element(By.CSS_SELECTOR,'.js_create_party').click()
        self.driver.find_element(By.NAME,'name').send_keys("less1")
        self.driver.find_element(By.NAME,'name').send_keys("秦国")
        self.driver.find_element(By.NAME,'name_en').send_keys("qinguo")
        self.driver.find_element(By.CSS_SELECTOR,'.js_toggle_party_list').click()
        eles=self.driver.find_elements(By.XPATH,'//*[@id="1688854153665670_anchor"][1]')
        eles[1].click()


        self.driver.find_element(By.XPATH,"//*[text()='确定']").click()
        return PartyPage(self.driver)





    def get_member_list(self):

       list=self.driver.find_elements(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
       list2=[ i.text for i in list ]
       return list2

