import time

from appium import webdriver
from appium.webdriver import appium_service
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps ['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'samsung SM-M015G'
desired_caps['app'] = ('/home/moin/Downloads/Appium/Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

# Part 2 "WebDriver object"

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

element = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")

for x in element:
    print(x.text)

for x in element:
    button = x.text
    if button == "ScrollView":
        x.click()
        break

time.sleep(2)
driver.quit()









