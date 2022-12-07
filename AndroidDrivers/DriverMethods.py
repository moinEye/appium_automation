from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'samsung SM-M015G'
desired_caps['app'] = ('/home/moin/Downloads/Appium/Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

# Part 2 "WebDriver object"

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

print("Check if device is locked or not :", driver.is_locked())
print("Current Package :", driver.current_package)
print("Current Activity:", driver.current_activity)
print("Current Context:", driver.orientation)







