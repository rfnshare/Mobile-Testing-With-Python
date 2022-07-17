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


class ConfigureAppium:
    service = AppiumService()
    options = UiAutomator2Options()

    def __init__(self, service, options):
        self.service = service
        self.options = options

    def launchApp(self, services, options):
        # service.start()
        # options.avd = 'Pixel_4_API_30'
        options.udid = '8RBDU19325003729'
        options.app = 'C:/Users/rfnsh/PycharmProjects/pythonMobileTesting/resources/ApiDemos-debug.apk'
        options.platformVersion = '11'
        options.app_package = 'io.appium.android.apis'
        options.app_activity = 'io.appium.android.apis.ApiDemos'
        # Enforces the server to dump the actual XML page source into the log if any error happens.
        options.print_page_source_on_find_failure = True
        # Skip the UiAutomator2 Server component installation on the device under test and all the related checks
        options.skip_server_installation = True
        # Device startup checks (whether it is ready and whether Settings app is installed) will be canceled.
        options.skip_device_initialization = True
        # Whether to grant all the requested application permissions automatically when a test starts
        options.auto_grant_permissions = True
        # If set to true then emulator starts in headless mode (e.g. no UI is shown).
        # options.is_headless = True
        # Unlocking Phone
        # options.unlock_strategy = 'locksettings'
        # options.unlock_type = 'pin'
        # options.unlock_key = '1234'

        driver = webdriver.Remote("http://127.0.0.1:1234", options=self.options)
        return driver

    def tearDown(self, service):
        driver = self.launchApp()
        driver.quit()
        # service.stop()
