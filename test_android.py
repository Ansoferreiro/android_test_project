import pytest
from appium import webdriver
import time

class TestAndroid:
    
    @pytest.fixture(scope="class")
    def setup(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "Android Emulator",
            "appPackage": "com.android.calculator2",
            "appActivity": "com.android.calculator2.Calculator",
            "automationName": "UiAutomator2"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        yield
        self.driver.quit()

    def test_calculator(self, setup):
        self.driver.find_element_by_id("digit_1").click()
        self.driver.find_element_by_accessibility_id("plus").click()
        self.driver.find_element_by_id("digit_2").click()
        self.driver.find_element_by_accessibility_id("equals").click()
        time.sleep(2)

    def test_camera(self, setup):
        self.driver.start_activity("com.android.camera", "com.android.camera.Camera")
        time.sleep(2)
        self.driver.find_element_by_id("com.android.camera:id/shutter_button").click()
        time.sleep(2)

if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html"])
