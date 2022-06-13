########################################################################################################################################################################################################################################################################################################################################################
# 1. launchBrowser() - || Author: ATE186, Date: 13th June 2022, ID - #15 || Editor: ATE186, Date: 13th June 2022, ID - #25 ||  Author: ATE186, Date: 13th June 2022, ID - #26
########################################################################################################################################################################################################################################################################################################################################################

import time
from selenium import webdriver
from Utilities import Utility

def launchBrowser():
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(executable_path= "..\\chromedriver.exe",options=chrome_options)
    Utility.maximize(driver)
    Utility.implicitWait(driver, 10)
    return driver

def launchLIMS():

