import time
import unittest

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LaunchApp import ConfigureAppium


class DemoGesture(ConfigureAppium, unittest.TestCase):
    driver = ConfigureAppium().launchApp()

    def test_basicGesture(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "text(\"Views\")").click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("Expandable Lists")').click()
        # Tapping
        # touch = TouchAction(self.driver) //Deprecated
        element = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "1. Custom Adapter")
        # touch.tap(element).perform() //Deprecated
        self.driver.execute_script("mobile: clickGesture", {'elementId': element, 'duration': 1000})
        time.sleep(5)

        # Long click Gesture
        ppl_name = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='People Names']")
        # touch.long_press(ppl_name, 2000).release().perform() //Deprecated
        self.driver.execute_script("mobile: longClickGesture", {'elementId': ppl_name, 'duration': 2000})
        title = self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sample menu']")
        self.assertEqual("Sample menu", title.text)
        self.assertTrue(title.is_displayed())
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text ='Sample action']").click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Toast")))
        text = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Toast").text
        print(text)
        assert "People Names: Group 0" in text
        self.assertEqual("People Names: Group 0 clicked", text)
        self.driver.quit()
