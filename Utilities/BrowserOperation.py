import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Utilities import Utility


def launchBrowser():
    global driver
    driver = webdriver.Chrome("..\\chromedriver.exe")

