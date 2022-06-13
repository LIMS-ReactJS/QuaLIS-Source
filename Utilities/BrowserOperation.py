########################################################################################################################################################################################################################################################################################################################################################
# 1. launchBrowser() - || Author: ATE186, Date: 13th June 2022, ID - #15 || Editor: ATE186, Date: 13th June 2022, ID - #25 ||  Author: ATE186, Date: 13th June 2022, ID - #26
# 2. launchLIMS() - || Author: ATE186, Date: 13th June 2022, ID - #16 ||
########################################################################################################################################################################################################################################################################################################################################################

import time
from configparser import ConfigParser
from selenium import webdriver
from ObjectRepository.Login import ElementLogin
from Utilities import Utility
from ObjectRepository import *

configDriver=ConfigParser()
configDriver.read(Utility.projectDirectory()+"\\Configuration\\config.ini")

def launchBrowser():
    global driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(executable_path= "..\\chromedriver.exe",options=chrome_options)
    Utility.maximize(driver)
    Utility.implicitWait(driver, 10)
    return driver

def launchLIMS():
    driver = launchBrowser()
    Utility.get(driver,configDriver.get("Credential", "link"))
    Utility.sendKeys(driver,ElementLogin.username,configDriver.get("Credential", "username"))
    Utility.click(driver,ElementLogin.password)
    Utility.sleep(2)
    Utility.sendKeys(driver,ElementLogin.password,configDriver.get("Credential", "password"))
    Utility.selectByText(driver,ElementLogin.userRole,configDriver.get("Credential", "userrole"))
    Utility.selectByText(driver,ElementLogin.loginType,configDriver.get("Credential", "loginType"))
    Utility.click(driver,ElementLogin.login)

