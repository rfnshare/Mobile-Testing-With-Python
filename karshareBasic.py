import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from LaunchApp import capabilities

driver = capabilities()
driver.implicitly_wait(30)
time.sleep(10)
btns = driver.find_elements(AppiumBy.XPATH,
                            "//android.widget.ImageView["
                            "@resource-id='com.karshare.app:id/navigation_bar_item_icon_view']")
print(len(btns))
btns[2].click()
driver.find_element(AppiumBy.ID, "com.karshare.app:id/sign_in").click()
driver.find_element(AppiumBy.ID, "com.karshare.app:id/btnSignIn").click()
driver.find_element(AppiumBy.ID, "com.karshare.app:id/etInput").send_keys("7212345678")
driver.find_element(AppiumBy.ID, "com.karshare.app:id/btnSignIn").click()
wait = WebDriverWait(driver, 30)
wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Toast")))
msg = driver.find_element(AppiumBy.XPATH, "//android.widget.Toast").text

create_list = msg.split(" ")
print(create_list[2])
driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText").send_keys(create_list[2])
wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.karshare.app:id/tvWelcomeText")))
# print(create_list[2])
print(create_list)
