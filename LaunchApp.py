import time

from Tools.scripts.win_add2path import PATH
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService

# Deprecated
# desired_caps = {
#         "appium:appPackage": "io.appium.android.apis",
#         "appium:appActivity": "io.appium.android.apis.ApiDemos",
#         "platformName": "Android",
#         "appium:uid": "emulator-5554",
#         "automationName": "UIAutomator2",
#     }

service = AppiumService()


def capabilities():
    service.start()
    options = UiAutomator2Options()
    options.device_name = 'Pixel 4 API 30'
    options.app = 'C:/Users/rfnsh/PycharmProjects/pythonMobileTesting/resources/ApiDemos-debug.apk'
    # options.platformVersion = '11'
    # options.udid = 'emulator-5554'
    # options.app_package = 'io.appium.android.apis'
    # options.app_activity = 'io.appium.android.apis.ApiDemos'

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    return driver


if __name__ == '__main__':
    driver = capabilities()
    driver.implicitly_wait(20)
    time.sleep(5)
    driver.quit()
    service.stop()
