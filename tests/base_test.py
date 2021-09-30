import os
import sys
import time

sys.path.append(os.path.dirname(__file__))

from altunityrunner import AltUnityDriver
import unittest
import pytest
import os
from appium import webdriver
from altunityrunner import AltUnityAndroidPortForwarding, AltUnityiOSPortForwarding


class TestBase(unittest.TestCase):
    platform = None

    @classmethod
    def setUpClass(cls):
        if os.getenv("APPIUM_PLATFORM", "android") == 'android':
            cls.platform = 'android'
        else:
            cls.platform = 'ios'
        print("Running on " + cls.platform)
        cls.desired_caps = {}
        cls.desired_caps['platformName'] = os.getenv('APPIUM_PLATFORM', 'Android')
        cls.desired_caps['deviceName'] = os.getenv('APPIUM_DEVICE', 'device')
        cls.desired_caps['app'] = os.getenv("APPIUM_APPFILE", "application.apk")
        cls.desired_caps['automationName'] = os.getenv('APPIUM_AUTOMATION', 'UIAutomator2')

        ##  Headspin data
        #cls.desired_caps['appPackage'] = os.getenv('APP_PACKAGE', 'com.Altom.TrashCat')
        #cls.desired_caps['appActivity'] = os.getenv('APP_ACTIVITY', 'com.unity3d.player.UnityPlayerActivity')

        #cls.desired_caps['udid'] = os.getenv('UDID_DETAIL', 'R9AN70CT3BJ')
        #cls.desired_caps['autoAcceptAlerts'] = os.getenv('AUTO_ACCEPT_ALERTS', 'true')
########################

        cls.appium_driver = webdriver.Remote('http://localhost:4723/wd/hub', cls.desired_caps)


        # Headspin data
        #cls.appium_driver = webdriver.Remote('https://dev-us-mia-0.headspin.io:7018/v0/86b1f5e8842f49bbbf920da797f2ad15/wd/hub', cls.desired_caps, strict_ssl= False)
####################
        print("Appium driver started")
        cls.setup_port_forwarding()
        time.sleep(10)
        cls.altdriver = AltUnityDriver()

    @classmethod
    def setup_port_forwarding(cls):
        try:
            AltUnityAndroidPortForwarding().remove_forward_port_device()
        except:
            print("No adb forward was present")
        try:
            AltUnityiOSPortForwarding.kill_all_iproxy_process()
        except:
            print("No iproxy forward was present")

        if cls.platform == 'android':
            AltUnityAndroidPortForwarding().forward_port_device()
            print("Port forwarded (Android).")
        else:
            AltUnityiOSPortForwarding().forward_port_device()
            print("Port forwarded (iOS).")

    @classmethod
    def tearDownClass(cls):
        print("Ending")
        cls.altdriver.stop()
        cls.appium_driver.quit()
