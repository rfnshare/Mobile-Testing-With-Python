import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "appium:appPackage": "com.code2lead.kwad",
    "appium:appActivity": "com.code2lead.kwad.MainActivity",
    "platformName": "Android",
    "appium:uid": "emulator-5554",
    "automationName": "UIAutomator2",
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue").click()
time.sleep(2)
driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Et1").send_keys("10")
driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Btn1").click()
ok = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Tv1").text
print(ok)