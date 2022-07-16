import time

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LaunchApp import capabilities

driver = capabilities()
driver.implicitly_wait(20)
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "text(\"Views\")").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Date Widgets").click()
driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@content-desc="2. Inline"]').click()
driver.find_element(AppiumBy.XPATH,
                    '//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc="6"]').click()

touch = TouchAction(driver)
option1 = driver.find_element(AppiumBy.XPATH,
                              '//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc="15"]')
option2 = driver.find_element(AppiumBy.XPATH,
                              '//android.widget.RadialTimePickerView.RadialPickerTouchHelper[@content-desc="45"]')
# touch.long_press(option1, 2000).move_to(option2).release().perform()
driver.tap([(100, 20), (100, 60), (100, 100)], 500)
