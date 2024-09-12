def get_capabilities():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '13.0', 
        'deviceName': 'Android Emulator',
        'app': 'app/othoba.apk',  
        'automationName': 'UiAutomator2'
       
    }
    print("Desired Capabilities:", desired_caps)  
    return desired_caps
