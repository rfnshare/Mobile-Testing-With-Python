import time

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LaunchApp import capabilities

driver = capabilities()
driver.implicitly_wait(20)
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "text(\"Views\")").click()
origin_el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Animation")
destination_el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "WebView")
driver.scroll(origin_el, destination_el)
