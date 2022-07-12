########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186-Murali.r , Date: 11th July 2022, ID - #85 ||
########################################################################################################################################################################################################################################################################################################################################################
from selenium.webdriver.common.by import By

from ObjectRepository.TestManagement import ElementTestMaster
from Setting import FieldName
from TestData import TestDataFlow
from Utilities import BrowserOperation, Utility


def testMasterAdd(driver,testMaster):
    testCategoryName=testMaster.get(FieldName.testMasterTestCategory)
    Utility.click(driver,ElementTestMaster.masterIcon)
    Utility.click(driver,ElementTestMaster.testManagementIcon)
    Utility.click(driver,ElementTestMaster.testIcon)
    Utility.click(driver,ElementTestMaster.testAdd)
    Utility.click(driver,ElementTestMaster.testTestCategory)
    testCategory=driver.find_elements(By.XPATH,"//*[@id='ntestcategorycode']/div[2]/div/div")

    print(testCategoryName)
    for i in testCategory:
        if i.text==testCategoryName:
            i.click()

    