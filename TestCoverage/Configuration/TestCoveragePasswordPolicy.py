########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 23th June 2022, ID - #63 ||
########################################################################################################################################################################################################################################################################################################################################################
import time

from selenium.webdriver.common.by import By

from ObjectRepository.UserManagement import ElementPasswordPolicy
from Utilities import Utility, BrowserOperation

policyName="PWD004"

def passwordPolicyAddApprove(driver,userRole):
    BrowserOperation.refreshLogin(driver)
    Utility.click(driver,ElementPasswordPolicy.masterIcon)
    Utility.click(driver,ElementPasswordPolicy.userManagementIcon)
    Utility.click(driver,ElementPasswordPolicy.passwordPolicyIcon)
    Utility.click(driver,ElementPasswordPolicy.passwordPolicyFilterIcon)
    Utility.click(driver,ElementPasswordPolicy.paswordPolicyUserRole)
    elements=driver.find_elements(By.XPATH,"//*[@id='nuserrolepolicycode']/div[2]/div/div")
    print(len(elements))
    for i in elements:
        name=i.text
        print(name)
        if(name==userRole):
            i.click()
            break
    Utility.click(driver,ElementPasswordPolicy.filterSubmit)
    Utility.click(driver,ElementPasswordPolicy.passwordPolicyAdd)
    Utility.sendKeys(driver,ElementPasswordPolicy.paswordPolicyName,policyName)
    Utility.sendKeys(driver,ElementPasswordPolicy.minimumNumberOfNumberCharacter,"1")
    Utility.sendKeys(driver,ElementPasswordPolicy.minimumNumberOfLowerCharacter,"0")
    Utility.sendKeys(driver,ElementPasswordPolicy.minimumNumberOfUpperCharacter,"0")
    Utility.sendKeys(driver,ElementPasswordPolicy.minimumNumberOfSpecialCharacter,"0")
    Utility.sendKeys(driver,ElementPasswordPolicy.minimumPasswordLength,"1")
    Utility.sendKeys(driver,ElementPasswordPolicy.maximumPasswordLength,"3")
    Utility.sendKeys(driver,ElementPasswordPolicy.numberOfFailedAttempt,"9")
    Utility.click(driver,ElementPasswordPolicy.passwordPolicyAddSubmit)
    Utility.click(driver,ElementPasswordPolicy.passwordPolicyApprove)

def passwordPolicyCopyApprove(driver,userRole):
    Utility.click(driver,ElementPasswordPolicy.masterIcon)
    Utility.click(driver,ElementPasswordPolicy.userManagementIcon)
    Utility.click(driver,ElementPasswordPolicy.passwordPolicyIcon)
    Utility.click(driver,ElementPasswordPolicy.passwordPolicyFilterIcon)
    Utility.click(driver,ElementPasswordPolicy.paswordPolicyUserRole)
    elements=driver.find_elements(By.XPATH,"//*[@id='nuserrolepolicycode']/div[2]/div/div")
    print(len(elements))
    for i in elements:
        name=i.text
        if(name==userRole):
            i.click()
            break
    Utility.click(driver,ElementPasswordPolicy.filterSubmit)
    Utility.click(driver,ElementPasswordPolicy.passwordPolicyCopy)
    Utility.sendKeys(driver,ElementPasswordPolicy.paswordPolicyName,"PWP002")
    Utility.click(driver,"//*[@id='nuserrolecode']/div[1]/div[1]")
    userRoleElements=driver.find_elements(By.XPATH,"//*[@id='nuserrolecode']/div[2]/div/div")
    userRoleElements[0].click()
    print(userRoleElements[0].text)