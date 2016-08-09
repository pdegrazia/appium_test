from appium import webdriver
import unittest

# iOS environment
desired_caps = {}
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '9.3'
desired_caps['deviceName'] = 'iPhone 6s Plus'
desired_caps['app'] = './UICatalog.app'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.launch_app()

el = driver.find_element_by_accessibility_id('Animation')

assert(el is not None)

driver.close_app()