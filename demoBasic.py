import time
import unittest

from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from LaunchApp import ConfigureAppium


class DemoBasic(ConfigureAppium, unittest.TestCase):
    driver = ConfigureAppium().launchApp()

    def test_basic(self):
        self.driver.find_element(AppiumBy.CSS_SELECTOR, "android.widget.TextView[content-desc='Preference']").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "3. Preference dependencies").click()
        self.driver.find_element(AppiumBy.ID, "android:id/checkbox").click()
        wifi_settings = self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView["
                                                                  "@resource-id='android:id/title']")
        print(len(wifi_settings))
        for i in wifi_settings:
            print(i.get_attribute("text"))
        wifi_settings[2].click()
        alert_title = self.driver.find_element(AppiumBy.ID, "android:id/alertTitle").text
        assert 'settings' in alert_title
        self.assertEqual("WiFi settings", alert_title)
        # self.driver.find_element(AppiumBy.XPATH, "(//android.widget.TextView[@resource-id='android:id/title'])[
        # 3]").click()
        self.driver.find_element(AppiumBy.ID, "android:id/edit").send_keys("Sample_WiFi")
        self.driver.find_element(AppiumBy.ID, "android:id/button1").click()
        self.driver.quit()
