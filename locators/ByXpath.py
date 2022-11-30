from appium import webdriver
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


ele_xpath = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Btn1"]')
# ele_xpath = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.code2lead.kwad:id/EnterValue"]' By using xpath and resource id
# ele_xpath = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="ENTER SOME VALUE"]')
# ele_xpath = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[3]') xpath and index value


ele_xpath.click()

time.sleep(2)

ele_xpath2 = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText')
ele_xpath2.send_keys("freddie")

time.sleep(2)

driver.quit()







