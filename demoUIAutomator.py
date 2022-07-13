import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from LaunchApp import capabilities

driver = capabilities()
driver.implicitly_wait(10)
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "text(\"Views\")").click()
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "text(\"Animation\")").click()
a = driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().clickable(true)')  # Find by property value
print(len(a))
