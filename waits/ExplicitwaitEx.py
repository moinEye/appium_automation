from datetime import time

from appium import webdriver
from appium.webdriver import appium_service
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

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

wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])

ele = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue"))
ele.click()

ele = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText"))
ele.send_keys("Skill2Lead")

time.sleep(4)
driver.quit()









