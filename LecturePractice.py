import time
import unittest

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LaunchApp import ConfigureAppium


class Practice(ConfigureAppium, unittest.TestCase):
    driver = ConfigureAppium().launchApp()

    def test_AlertPractice(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "text(\"App\")").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Alert Dialogs").click()

        self.driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/two_buttons").click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((AppiumBy.ID, "android:id/alertTitle")))
        text = self.driver.find_element(AppiumBy.ID, "android:id/alertTitle").text
        assert "Lorem ipsum" in text
        self.driver.find_element(AppiumBy.ID, "android:id/button1").click()
        time.sleep(5)
        self.driver.quit()
