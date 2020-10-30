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
        'build': 'python-pre-run-test-last',
        'video': True,
        'network': True,
        'console': True,
        'visual': True,
        "platform": platform,
        "browser": browser,
        "browserVersion": browserVersion,
        "acceptInsecureCerts": True,
        # "selenium_version": "3.141.59",
        # "requireWindowFocus": True,
#/private/var/folders/bj/fg9bg19s3zjgp0wz1bbnp8780000gn/T/logs
        # "prerun": {F
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

    desiredCapabilities = {
        "_isOldEdge": True,
        "acceptInsecureCerts": True,
        "acceptSslCerts": True,
        "browserName": "MicrosoftEdge",
        "build": "test edge zoom fix final QA",
        "console": True,
        "extendedDebuging": True,
        "handlesAlerts": True,
        "headless": False,
        "javascriptEnabled": True,
        "locationContextEnabled": True,
        "loggingPrefs": {"browser": "ALL", "driver": "ALL", "server": "ALL"},
        "name": "edge_html_osx",
        "nativeEvents": True,
        "network": True,
        "platform": "win10",
        "resolution": "1920x1080",
        "rotatable": True,
        "selenium_version": "3.14.0",
        "testName": "Test edge zoom fix",
        "unexpectedAlertBehaviour": "accept",
        "version": "18.0",
        "video": True,
        "visual": True,
        "w3c": True,
        # "fixedIP": "10.81.103.231",
        "ignoreZoomSetting": True,
        "ie.compatibility": 11001
    }

    local_url = "http://localhost:4449/wd/hub"

    start = time.time()

    driver = webdriver.Remote(
        command_executor=url,
        desired_capabilities=capabilities,
    )
    time.sleep(5)

    # driver.get('https://abdullahh:oklT35Q0r4zPUQRuQTxarFxHj9g2bU5lVWM7oSz4MHAOE0MQlB@stage-hub.lambdatest.com/wd/hub')
    # driver.get('http://jsbin.testim.io/tuqu/1/')
    # driver.get('http://lens.lambdatest.io')
    # driver.maximize_window()
    driver.get("https://google.com/")
    time.sleep(2)
    driver.get("https://www.fast.com")
    time.sleep(5)
    driver.get("https://www.whatculture.com/wwe")
    time.sleep(5)
    driver.quit()

    # driver.get("http://jsbin.testim.io/fix/4/")
    # cookie = {"name": "MyName", "value": "Daniel", "domain": ".jsbin.testim.io", "httpOnly": False, "secure": False}
    # driver.add_cookie(cookie)
    # time.sleep(3)
    # # elem = driver.find_element_by_name("calc cookie text")
    # elem = driver.find_element_by_xpath('//button[text()="calc cookie text"]')
    # print("text is ", elem.text)
    # elem.send_keys("\n")
    # elem.click()
    #
    # cookie_result = driver.get_cookie("MyName")
    # print("cookie is", cookie_result)
