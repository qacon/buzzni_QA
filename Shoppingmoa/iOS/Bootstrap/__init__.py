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
    TEST_CONFIG.sdkver = "13.4.1"
    TEST_CONFIG.dname = "iPhone 11"
    TEST_CONFIG.udid = "00008030-0002712A36E0802E"
    TEST_CONFIG.auto = "XCUITest"
    # TEST_CONFIG.bundleId = "buzzni.homeshoppingmoa.webapp.dev"
    TEST_CONFIG.bundleId = "buzzni.homeshoppingmoa.webapp"
    TEST_CONFIG.ratio = "2688 x 1242"
    TEST_CONFIG.os = "iOS"
    TEST_CONFIG.user_name = "billy"
    TEST_CONFIG.password = "billy"

    TEST_CONFIG.driver = webdriver.Remote(
        command_executor=f'http://127.0.0.1:{TEST_CONFIG.port}/wd/hub',
        desired_capabilities={
            "platformName": "iOS",
            "bundleId": TEST_CONFIG.bundleId,
            "appium:automationName": TEST_CONFIG.auto,
            "platformVersion": TEST_CONFIG.sdkver,
            "deviceName": TEST_CONFIG.dname,
            "appium:udid": TEST_CONFIG.udid,
            "newCommandTimeout": 10000,
            "appium:noReset": "true"
        }
    )
