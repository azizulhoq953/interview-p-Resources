from appium import webdriver

def setup_appium():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "Android Emulator",
        "app": "./apk/othoba.apk",  # Path to the APK
        "automationName": "UiAutomator2"
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    return driver
