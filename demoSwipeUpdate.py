import time
import unittest

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LaunchApp import ConfigureAppium


class DemoSwipeGesture(ConfigureAppium, unittest.TestCase):
    driver = ConfigureAppium().launchApp()

    def test_basicSwipeGesture(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "text(\"Views\")").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Gallery").click()

        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text=\"1. Photos\"]").click()
        images = self.driver.find_elements(AppiumBy.XPATH, "//android.widget.ImageView")
        print(images[0].get_attribute("focusable"))
        print("Length of Images", len(images))
        assert "true" in images[0].get_attribute("focusable")
        # Swipe
        # while True:
        #     images = self.driver.find_elements(AppiumBy.XPATH, "//android.widget.ImageView")
        #     if 4 <= len(images):
        #         for i in range(len(images)):
        #             self.driver.execute_script('mobile: swipeGesture',
        #                                        {'elementId': images[i], 'direction': 'left',
        #                                         'percent': 0.75})
        #     else:
        #         break
        self.driver.execute_script('mobile: swipeGesture',
                                   {'elementId': images[0], 'direction': 'left',
                                    'percent': 0.75})

        assert "false" in images[0].get_attribute("focusable")
