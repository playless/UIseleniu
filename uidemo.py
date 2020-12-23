import json
import time

from selenium import  webdriver
'''
selenium cookie登录
'''

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
driver.delete_all_cookies()
driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
# # cookies=driver.get_cookies()
# time.sleep(10)
# cookies=driver.get_cookies()
# print(cookies)
# print(type(cookies))
# with open("cookies.txt",'w') as f:
#     f.write(json.dumps(cookies))


with open(r"E:\UI\cookies.txt",'r') as f:
    cookie=f.read()
    cookie=json.loads(cookie)
# print(cookie)
# print(type(cookie))
for iteam in cookie:
    # print(type(c))
    # print(c["value"])
    cookie_dict={"name":iteam["name"],
                 "value":iteam["value"],

                 "path":iteam["path"],
                 "secure":iteam["secure"]}
    # print(cookie_dict)
    driver.add_cookie(cookie_dict)
driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
# driver.refresh()
time.sleep(5)
driver.close()

