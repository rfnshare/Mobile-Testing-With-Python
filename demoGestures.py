import time

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

from LaunchApp import capabilities

driver = capabilities()
driver.implicitly_wait(20)
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "text(\"Views\")").click()
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("Expandable Lists")').click()
# Tapping
element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1. Custom Adapter")
touch = TouchAction(driver)
touch.tap(element).perform()
time.sleep(5)
