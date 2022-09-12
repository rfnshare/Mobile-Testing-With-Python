import time
import unittest
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LaunchKarshareApp import ConfigureAppium


class DemoScrollGesture(ConfigureAppium, unittest.TestCase):
    driver = ConfigureAppium().launchApp()

    def scroll(self, txt):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 f"new UiScrollable(new UiSelector()).scrollIntoView(text(\"{txt}\"))")

    def test_basicScrollGesture(self):
        time.sleep(30)
        destination_element = self.driver.find_element(AppiumBy.ID, "com.karshare.app:id/results")

        scroll_more = self.driver.execute_script('mobile: scrollGesture',
                                                 {'elementId': destination_element, 'direction': 'down',
                                                  'percent': 3.0})
        print("---->", scroll_more)

        while scroll_more is True:
            scroll_more = self.driver.execute_script('mobile: scrollGesture',
                                                     {'elementId': destination_element, 'direction': 'down',
                                                      'percent': 3.0})
            print("----<", scroll_more)
