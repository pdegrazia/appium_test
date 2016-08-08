from appium import webdriver
import unittest

# iOS environment
desired_caps = {}
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '9.3'
desired_caps['deviceName'] = 'iPhone 5s'
desired_caps['app'] = './Romeo_Feeder.app'

self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.launch_app()