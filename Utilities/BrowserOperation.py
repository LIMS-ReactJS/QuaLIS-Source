############################################################################################################################################################################
# 1. launchBrowser() - || Author: ATE186, Date: 13th June 2022, ID - #11 ||
############################################################################################################################################################################

import time
from selenium import webdriver


def launchBrowser():
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(executable_path= "..\\chromedriver.exe",options=chrome_options)
    return driver
