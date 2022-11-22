#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from appium import webdriver

class TestConfig():
    driver = 'driver'
    check_loop_count = 3
    is_passed = False
    is_finished = False
    is_initialized = False
    res = []
    port = None
    sdkver = None
    dname = None
    udid = None
    auto = None
    ratio = None
    os = None
    user_name = None
    password = None

TEST_CONFIG = TestConfig()

def initialize_bp(target, argv):
    TEST_CONFIG.port = "4723"
    TEST_CONFIG.sdkver = "10"
    TEST_CONFIG.dname = "Galaxy Note 9"
    # TEST_CONFIG.dname = "Galaxy S10"
    # TEST_CONFIG.dname = "G7"
    # TEST_CONFIG.udid = "R39M3084V5A"
    # TEST_CONFIG.udid = "LMG710Nb7188cc8"
    TEST_CONFIG.udid = "2469e164b41c7ece"
    TEST_CONFIG.auto = "UIAutomator2"
    TEST_CONFIG.ratio = "3040 x 1440"
    TEST_CONFIG.os = "Android"
    TEST_CONFIG.user_name = "billy"
    TEST_CONFIG.password = "billy"
    app = '/Users/macbookpro/Git/Shoppingmoa/APKs/shoppingmoa.apk'

    TEST_CONFIG.driver = webdriver.Remote(
        # command_executor=f'http://127.0.0.1:{TEST_CONFIG.port}',
        command_executor=f'http://127.0.0.1:{TEST_CONFIG.port}/wd/hub',
        desired_capabilities={
            'app': app,
            "platformName": "Android",
            "appium:automationName": TEST_CONFIG.auto,
            "platformVersion": TEST_CONFIG.sdkver,
            "deviceName": TEST_CONFIG.dname,
            "appium:udid": TEST_CONFIG.udid,
            "newCommandTimeout": 10000,
            "appium:noReset": "true"
    }
    )
