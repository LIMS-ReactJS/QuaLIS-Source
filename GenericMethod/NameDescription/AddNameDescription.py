########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 21st June 2022, ID - #52 ||
########################################################################################################################################################################################################################################################################################################################################################

from selenium.webdriver.common.by import By
from Setting import ObjectName, FieldName
from selenium import webdriver

from Utilities import Utility, BrowserOperation
from selenium.webdriver.common.action_chains import ActionChains

def addNameDescription(driver, element, screenshot, value):
    BrowserOperation.refreshLogin(driver)
    screenshot = dict(screenshot)
    value = dict(value)
    element = dict(element)
    navigatePermission = "FAIL"
    Utility.click(driver,element.get(ObjectName.moduleIcon))
    Utility.scrollToElement(driver,element.get(ObjectName.subModuleIcon))
    Utility.click(driver,element.get(ObjectName.subModuleIcon))
    Utility.click(driver,element.get(ObjectName.screenIcon))
    Utility.click(driver, element.get(ObjectName.add))
    Utility.sendKeys(driver,element.get(ObjectName.name),value.get(FieldName.name))
    Utility.sendKeys(driver,element.get(ObjectName.description),value.get(FieldName.description))
    Utility.click(driver,element.get(ObjectName.addSubmit))
    Utility.click(driver,element.get(ObjectName.subModuleIcon))

