import sys
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

if __name__ == '__main__':
    url_mapping = {
        'stage': "https://abdullahh:oklT35Q0r4zPUQRuQTxarFxHj9g2bU5lVWM7oSz4MHAOE0MQlB@stage-hub.lambdatest.com/wd/hub",
        'QA': "https://koshinder:UxrWmlu7baHM9oOVWMigibPjeAatsktCzmXD4bTeCRHYq9hSP9@stage-hub.lambdatest.com/wd/hub",
        'dev': "http://abdullahh:oklT35Q0r4zPUQRuQTxarFxHj9g2bU5lVWM7oSz4MHAOE0MQlB@127.0.0.1:4449/wd/hub",
        'prod': "https://abdullahh:4s6ogqXTEDlVTv9lXdg0VZzYsd7jHkRezvFoYIo1hABDji12j9@hub.lambdatest.com/wd/hub",
        'beta': "https://abdullahh:4s6ogqXTEDlVTv9lXdg0VZzYsd7jHkRezvFoYIo1hABDji12j9@beta-hub.lambdatest.com/wd/hub",
    }

    if len(sys.argv) > 1:
        url = url_mapping.get(sys.argv[1], "dev")
    else:
        url = url_mapping.get("dev")

    if len(sys.argv) > 2:
        platform = sys.argv[2]
    else:
        platform = "Windows 10"

    if len(sys.argv) > 3:
        browser = sys.argv[3]
    else:
        browser = "Chrome"

    if len(sys.argv) > 4:
        browserVersion = sys.argv[4]
    else:
        browserVersion = "75.0"

    if len(sys.argv) > 5:
        fixedIP = sys.argv[5]
    else:
        fixedIP = None

    capabilities = {
        'build': 'python-pre-run-test-git',
        'video': True,
        'network': False,
        'console': True,
        'visual': True,
        "platform": platform,
        "browser": browser,
        "browserVersion": browserVersion,
        # "selenium_version": "3.141.59",
        # "requireWindowFocus": True,
#/private/var/folders/bj/fg9bg19s3zjgp0wz1bbnp8780000gn/T/logs
        # "prerun": {
        #     "url": "lambda:pandi_certificate/pre/dev_cert_1.bat"
        # },

        # "prerun": {
        #     "url": "lambda:HttpDialogCompiled/pre/httpdialog.exe",
        #     "background": False,
        # },
        # "prerun": {
        #     "url": "lambda:IE_ZOOM/pre/ie_zoom_out.ps1"
        # },

        # "prerun": {
        #     "url": "lambda:Warning/pre/safari_disable_warning.sh",
        #     "background": False,
        # },
        # "prerun": {
        #     "url": "lambda:SimpleWin1/pre/scrip1Win.bat"
        # },
        "loggingPrefs": {"browser": "ALL", "driver": "ALL", "server": "ALL"},
        "ignoreZoomSetting": True,
        # "region": "eu",
        # "build": "your build name",
        # "name": "your test name",
        # "platformName": "iOS",
        # "deviceName": "iPad (6th generation)",
        # "platformVersion": "13.1"
        # "safari.popups": True,
        # "safari.cookies": True
        "ie.compatibility": 11001,
    }

    if fixedIP:
        capabilities["fixedIP"] = fixedIP

    start = time.time()

    driver = webdriver.Remote(
        command_executor=url,
        desired_capabilities=capabilities,
    )
    # driver.get('https://abdullahh:oklT35Q0r4zPUQRuQTxarFxHj9g2bU5lVWM7oSz4MHAOE0MQlB@stage-hub.lambdatest.com/wd/hub')
    # driver.get('http://jsbin.testim.io/tuqu/1/')
    # driver.get('http://lens.lambdatest.io')
    driver.get("https://www.google.com")
    driver.get("https://www.fast.com")
    #
    # driver.execute_script("throttleNetwork", {
    #
    # })
    time.sleep(5)
    driver.quit()

    end = time.time()
    print("total time took - ", end-start, "seconds")
