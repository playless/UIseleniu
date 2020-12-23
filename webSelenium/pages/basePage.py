

import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self,base_driver=None):
        base_driver:WebDriver
        if base_driver is None:
            self.driver=webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
            self.__cookie_login()
        else:
            self.driver=base_driver
        self.driver.implicitly_wait(10)
    def __cookie_login(self):

        with open("E:/UI/webSelenium/pages/data.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def quite(self):
        self.driver.quit()