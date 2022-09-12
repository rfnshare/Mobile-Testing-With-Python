import time
import unittest

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LaunchApp import ConfigureAppium


class DemoDragGesture(ConfigureAppium, unittest.TestCase):
    driver = ConfigureAppium().launchApp()

    def DragAndDrop(self, element, x, y):
        self.driver.execute_script('mobile: dragGesture',
                                   {'elementId': element, 'endX': x,
                                    'endY': y})

    def test_basicDragGesture(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "text(\"Views\")").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Drag and Drop").click()
        element = self.driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/drag_dot_1")
        self.DragAndDrop(element, 619, 560)
        assert "Dropped!" in self.driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/drag_result_text").text
