from selenium.webdriver.common.by import By

from webSelenium.pages.basePage import BasePage




class AddMemberPage(BasePage):

    '''添加成员页面'''
    def save(self):
        from webSelenium.pages.mainPage import MainPage

        '''添加成员并保存,跳转到首页'''
        self.driver.find_element(By.ID,'username').send_keys("potato1")
        self.driver.find_element(By.ID,'memberAdd_acctid').send_keys('potato1')
        self.driver.find_element(By.ID,'memberAdd_phone').send_keys('11111111111')
        self.driver.find_element(By.CSS_SELECTOR,'.js_btn_save').click()
        return MainPage(self.driver)
    def save_faile(self):
        self.driver.find_element(By.ID, 'username').send_keys("potato1")
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys('potato1')
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys('11111111111')
        self.driver.find_element(By.CSS_SELECTOR,'.js_btn_save').click()
        list1=self.driver.find_elements(By.CSS_SELECTOR,'.ww_inputWithTips_tips')
        erro_list=[i.text for i in list1]
        print(erro_list)
        return erro_list

