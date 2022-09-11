import time
import unittest

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LaunchApp import ConfigureAppium


class DemoScrollGesture(ConfigureAppium, unittest.TestCase):
    driver = ConfigureAppium().launchApp()

    def scroll(self, txt):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                 f"new UiScrollable(new UiSelector()).scrollIntoView(text(\"{txt}\"))")

    def scroll_more(self):
        can_scroll_more = self.driver.execute_script('mobile: scrollGesture', {
            'left': 100, 'top': 500, 'width': 900, 'height': 500,
            'direction': 'down',
            'percent': 3.0
        })
        while can_scroll_more is True:
            can_scroll_more = self.driver.execute_script('mobile: scrollGesture', {
                'left': 100, 'top': 500, 'width': 900, 'height': 500,
                'direction': 'down',
                'percent': 3.0
            })
            print(can_scroll_more)

    def test_basicScrollGesture(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "text(\"Views\")").click()

        # Google Built In Scrolling
        # self.scroll('WebView')

        # Scroll Gesture (Until End)
        # self.scroll_more()

        # origin_el = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Animation")
        destination_el = self.driver.find_element(AppiumBy.ID, "android:id/list")

        can_scroll_more = self.driver.execute_script('mobile: scrollGesture',
                                   {'elementId': destination_el, 'direction': 'down', 'percent': 3.0})
        print("---->", can_scroll_more)

        while can_scroll_more is True:
            can_scroll_more = self.driver.execute_script('mobile: scrollGesture',
                                                         {'elementId': destination_el, 'direction': 'down',
                                                          'percent': 3.0})
            print("----<", can_scroll_more)
