from selenium import webdriver
import os
import time
import random

# QQ空间模拟登录
# driver = webdriver.Chrome()
driver = webdriver.PhantomJS()
print('准备登陆QQ空间')
driver.get('https://qzone.qq.com/')

driver.switch_to_frame('login_frame')
driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').clear()
driver.find_element_by_id('u').send_keys(os.environ.get('QQ'))
driver.find_element_by_id('p').clear()
driver.find_element_by_id('p').send_keys(os.environ.get('QQ_PWD'))
driver.find_element_by_id('login_button').click()
print('登陆成功')
time.sleep(3)

# driver.maximize_window()
# driver.set_window_size(1300, 860)
# 签到
print('准备签到')
driver.find_element_by_id('checkin_button').click()
driver.switch_to_frame('checkin_likeTipsFrame')
# driver.find_element_by_xpath("//img[@src='http://qzonestyle.gtimg.cn/qzone/em/stamp/50002_l.jpg']").click() # 天气
labels = driver.find_elements_by_class_name("li_mouseout")
label = random.choice(labels)
print('签到标签:'+label.text)
label.click()
time.sleep(3)

# driver.find_element_by_id('idEditorTextarea').click()
# driver.find_element_by_id('$1_substitutor_content').click()
# driver.find_element_by_id('$1_substitutor_content').send_keys('123')
# if driver.find_element_by_id('$1_substitutor_content').is_displayed():
# if driver.find_element_by_id('$1_content_content').is_displayed():

try:
	driver.find_element_by_id('idEditorTextarea').click()
	driver.find_element_by_id('$1_content_content').send_keys('待爬取发布的信息...')
	driver.find_element_by_id('idEditorPublishBtn').click()
	print('签到成功!')
except Exception as e:
	print(driver.find_element_by_id('idEditorTextarea').location)
	print(driver.find_element_by_id('$1_content_content').location)
	


# # 批量点赞
# for button in driver.find_elements_by_class_name('icon-op-praise'):
# 	button.click()

# driver.find_elements_by_class_name('ck-btn').click()

# driver.refresh()
driver.quit()