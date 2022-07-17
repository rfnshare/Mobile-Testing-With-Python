from appium.webdriver.common.appiumby import AppiumBy
from LaunchApp import launchApp


class CommonMethods:
    driver = launchApp()

    def find_element_by_xpath(self, locator):
        self.driver.find_element(AppiumBy.XPATH, locator)
