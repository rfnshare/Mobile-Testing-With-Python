import time
import unittest

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LaunchApp import ConfigureAppium


class Practice(ConfigureAppium, unittest.TestCase):
    driver = ConfigureAppium().launchApp()

    def wait(self, method, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((method, locator)))

    def test_AlertPractice(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "text(\"App\")").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Alert Dialogs").click()
        self.driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/two_buttons").click()
        self.wait(AppiumBy.ID, "android:id/alertTitle")
        text = self.driver.find_element(AppiumBy.ID, "android:id/alertTitle").text
        assert "Lorem ipsum" in text
        self.driver.find_element(AppiumBy.ID, "android:id/button1").click()
        time.sleep(5)
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc=\"List dialog\"]").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Command two']").click()
        self.wait(AppiumBy.ID, 'android:id/message')
        assert "Command two" in self.driver.find_element(AppiumBy.ID, 'android:id/message').text
        self.driver.back()
        time.sleep(5)
        self.driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/progress_button").click()
        self.driver.quit()
