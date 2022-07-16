from Tools.scripts.win_add2path import PATH
from appium import webdriver
from appium.options.android import UiAutomator2Options


# Deprecated
# desired_caps = {
#         "appium:appPackage": "io.appium.android.apis",
#         "appium:appActivity": "io.appium.android.apis.ApiDemos",
#         "platformName": "Android",
#         "appium:uid": "emulator-5554",
#         "automationName": "UIAutomator2",
#     }
def capabilities():
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
