from selenium.webdriver.common.by import By

from webSelenium.pages.addMemberPage import AddMemberPage
from webSelenium.pages.basePage import BasePage
from webSelenium.pages.contactsPage import ContactsPage



class MainPage(BasePage):
    '''首页'''
    def goto_contacts(self):

        '''跳转通讯录页面'''
        self.driver.find_element(By.ID,'menu_contacts').click()
        return ContactsPage(self.driver)
    def goto_AddMemberPage(self):
        '''跳转到添加成员页面'''
        self.driver.find_element(By.CSS_SELECTOR,'[node-type=addmember]').click()
        return AddMemberPage(self.driver)
    def goto_apps(self):
        '''跳转应用管理页面'''
        pass
    def goto_customer(self):
        '''跳转客户关系页面'''
        pass