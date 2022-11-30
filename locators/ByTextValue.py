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


ele_text = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("ENTER SOME VALUE")')
ele_text.click()

# ele_text = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("ENTER SOME VALUE")')
# ele_text.click()






