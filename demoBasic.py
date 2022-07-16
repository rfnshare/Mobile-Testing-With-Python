import time

from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

from LaunchApp import capabilities
service = AppiumService()
driver = capabilities()
driver.find_element(AppiumBy.CSS_SELECTOR, "android.widget.TextView[content-desc='Preference']").click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "3. Preference dependencies").click()
driver.find_element(AppiumBy.ID, "android:id/checkbox").click()
# wifi_settings = driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@resource-id='android:id/title']")
# print(len(wifi_settings))
# for i in wifi_settings:
#     print(i.get_attribute("text"))
# wifi_settings[2].click()
driver.find_element(AppiumBy.XPATH, "(//android.widget.TextView[@resource-id='android:id/title'])[3]").click()
driver.find_element(AppiumBy.ID, "android:id/edit").send_keys("Sample_WiFi")
driver.find_element(AppiumBy.ID, "android:id/button1").click()
time.sleep(5)
driver.quit()
service.stop()
