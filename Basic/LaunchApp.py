from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# Part 1 "Desired Capabilities"

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

#Part 3 "Action on the app"
# driver.find_element("").click()
ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
ele_id.click()





