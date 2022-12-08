from appium import webdriver
from appium.webdriver import appium_service
from appium.webdriver.common.appiumby import AppiumBy

import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps ['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'samsung SM-M015G'
desired_caps['app'] = ('/home/moin/Downloads/Appium/Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'


driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
print("Text on the button", ele_id.text)
print("Text on the button", ele_id.get_attribute("text"))
print("Text on the button", ele_id.get_attribute("content-desc"))
ele_id.click()

time.sleep(2)

ele_classname = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
ele_classname.send_keys("Skill2Lead")
time.sleep(2)
ele_classname.clear()
time.sleep(2)
ele_classname.send_keys("Skill2Lead")

time.sleep(2)
ele_classname.send_keys("Skill2Lead")

time.sleep(2)
driver.quit()






