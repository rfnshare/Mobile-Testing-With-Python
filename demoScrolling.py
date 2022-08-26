import time
import unittest

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LaunchApp import ConfigureAppium


class DemoScrollGesture(ConfigureAppium, unittest.TestCase):
    driver = ConfigureAppium().launchApp()

    def test_basicScrollGesture(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "text(\"Views\")").click()
        # can_scroll_more = self.driver.execute_script('mobile: scrollGesture', {
        #     'left': 100, 'top': 100, 'width': 200, 'height': 200,
        #     'direction': 'down',
        #     'percent': 3.0
        # })
        # print(can_scroll_more)
        # while can_scroll_more is True:
        #     can_scroll_more = self.driver.execute_script('mobile: scrollGesture', {
        #         'left': 100, 'top': 100, 'width': 200, 'height': 200,
        #         'direction': 'down',
        #         'percent': 3.0
        #     })
        #     print(can_scroll_more)

        # self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()).scrollIntoView(text(\"ImageView\"))')
        origin_el = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Animation")
        destination_el = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "WebView")
        self.driver.scroll(origin_el, destination_el)
        # self.driver.execute_script('mobile: scrollGesture',
        #                            {'elementId': destination_el, 'direction': 'up', 'percent': 3.0})
