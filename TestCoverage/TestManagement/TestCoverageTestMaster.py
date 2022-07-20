########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186-Murali.r , Date: 11th July 2022, ID - #85 ||
########################################################################################################################################################################################################################################################################################################################################################
import time

from selenium.webdriver.common.by import By

from ObjectRepository.TestManagement import ElementTestMaster
from Setting import FieldName, YesNo, ParameterType
from TestData import TestDataFlow
from Utilities import BrowserOperation, Utility


def testMasterAdd(driver,testMaster):
    testCategoryName=testMaster.get(FieldName.testMasterTestCategory)
    testName=testMaster.get(FieldName.testMasterTestName)
    testAbbreviation=testMaster.get(FieldName.testMasterTestAbbreviation)
    testDescription=testMaster.get(FieldName.testMasterTestDescription)
    testCost=testMaster.get(FieldName.testMasterTestCost)
    lab=testMaster.get(FieldName.testMasterLab)
    method=testMaster.get(FieldName.testMasterMethod)
    instrumentCategory=testMaster.get(FieldName.testMasterInstrumentCategory)
    active=testMaster.get(FieldName.testMasterActive)
    accredited=testMaster.get(FieldName.testMasterAccredited)
    parameterName=testMaster.get(FieldName.testMasterParameterName)
    parameterAbbreviation=testMaster.get(FieldName.testMasterParameterAbbreviation)
    parameterType=testMaster.get(FieldName.testMasterParameterType)
    parameterUnit=testMaster.get(FieldName.testMasterUnit)
    parameterRoundingDigit=testMaster.get(FieldName.testMasterRoundingDigit)

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
            break

    Utility.sendKeys(driver,ElementTestMaster.testName,testName)
    Utility.clear(driver,ElementTestMaster.testAbbreviation)
    Utility.sendKeys(driver,ElementTestMaster.testAbbreviation,testAbbreviation)
    Utility.sendKeys(driver,ElementTestMaster.testDescription,testDescription)
    Utility.sendKeys(driver,ElementTestMaster.testCost,testCost)

    Utility.click(driver,ElementTestMaster.testLab)
    labList=driver.find_elements(By.XPATH,"//*[@id='nsectioncode']/div[2]/div/div")
    for i in labList:
        if i.text==lab:
            i.click()
            break

    Utility.click(driver,ElementTestMaster.testMethod)
    methodList=driver.find_elements(By.XPATH,"//*[@id='nmethodcode']/div[2]/div/div")
    for i in methodList:
        if i.text==method:
            i.click()
            break

    Utility.click(driver,ElementTestMaster.testInstrumentCategory)
    instrumentCategoryList=driver.find_elements(By.XPATH,"//*[@id='ninstrumentcatcode']/div[2]/div/div")
    for i in instrumentCategoryList:
        if i.text==instrumentCategory:
            i.click()
            break

    currentAccreditedStatus=driver.find_element(By.XPATH,"//*[@id='naccredited']").get_attribute('value')

    if(accredited==YesNo.yes):
        if currentAccreditedStatus=="false":
            Utility.click(driver,ElementTestMaster.testAccredited)
    else:
        print("accredited is no")




    currentActiveStatus= driver.find_element(By.XPATH,"//*[@id='ntransactionstatus']").get_attribute('value')

    if(active==YesNo.yes):
        if currentActiveStatus=="false":
            Utility.click(driver,ElementTestMaster.testActive)


    Utility.clear(driver,ElementTestMaster.testParameterName)
    Utility.sendKeys(driver,ElementTestMaster.testParameterName,parameterName)
    Utility.clear(driver,ElementTestMaster.testParameterAbbreviation)
    Utility.sendKeys(driver,ElementTestMaster.testParameterAbbreviation,parameterAbbreviation)

    time.sleep(20)
    Utility.click(driver,ElementTestMaster.testAddSubmit)