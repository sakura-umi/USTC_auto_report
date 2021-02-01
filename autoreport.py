from selenium import webdriver
import time

#将账号密码填入
username="xxxxx"
passwd="xxxxxx"

# 创建chrome参数对象
opt = webdriver.ChromeOptions()

opt.headless = True #设置无界面模式，windows开启会出现跨域cookie报错需要关闭，linux可以正常开启，自动适配对应参数
opt.add_argument('--no-sandbox')
opt.add_argument('--disable-gpu')
opt.add_argument('--hide-scrollbars')
opt.add_argument('blink-settings=imagesEnabled=false') #无图模式，加载更快

browser = webdriver.Chrome('/usr/bin/chromedriver',options=opt)#此处填写chromedriver的路径
browser.get('https://weixine.ustc.edu.cn/2020/caslogin')

elem=browser.find_element_by_id("username")
elem.send_keys(username)
elem=browser.find_element_by_id("password")
elem.send_keys(passwd)

elem=browser.find_element_by_id("login")
elem.click()
browser.implicitly_wait(5)
browser.switch_to_window(browser.window_handles[-1])

elem=browser.find_element_by_id("report-submit-btn")
time.sleep(1)
elem.click()
time.sleep(1)
browser.quit()
