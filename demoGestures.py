import time

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LaunchApp import capabilities

driver = capabilities()
driver.implicitly_wait(20)
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "text(\"Views\")").click()
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("Expandable Lists")').click()
# Tapping
touch = TouchAction(driver)
element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1. Custom Adapter")
touch.tap(element).perform()
time.sleep(5)
ppl_name = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='People Names']")
touch.long_press(ppl_name, 2000).release().perform()
time.sleep(2)
driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text ='Sample action']").click()
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Toast")))
text = driver.find_element(AppiumBy.XPATH, "//android.widget.Toast").text
print(text)
assert "People Names: Group 0" in text
time.sleep(5)
