########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 29th June 2022, ID - #79 ||
########################################################################################################################################################################################################################################################################################################################################################
from selenium.webdriver.common.by import By

from ObjectRepository.Contact import ElementClient
from Utilities import Utility


def clientAdd(driver):
    Utility.click(driver,ElementClient.masterIcon)
    Utility.scrollToElement(driver,ElementClient.contactsIcon)
    Utility.click(driver,ElementClient.contactsIcon)
    Utility.click(driver,ElementClient.clientIcon)
    Utility.click(driver,ElementClient.clientAdd)
    Utility.sendKeys(driver,ElementClient.clientName,"clientname")
    Utility.sendKeys(driver,ElementClient.clientAddressOne,"clientname")
    Utility.sendKeys(driver,ElementClient.clientAddressTwo,"clientname")
    Utility.sendKeys(driver,ElementClient.clientAddressThree,"clientname")
    Utility.sendKeys(driver,ElementClient.clientPhoneNumber,"9999999")
    Utility.sendKeys(driver,ElementClient.clientMobileNumber,"9999999")
    Utility.sendKeys(driver,ElementClient.clientFaxNumber,"9999999")
    Utility.sendKeys(driver,ElementClient.clientEmail,"murali.r@agaramtech.com")
    Utility.click(driver,ElementClient.clientCountry)
    countries=driver.find_elements(By.XPATH,"//*[@id='ncountrycode']/div[2]/div/div")
    for i in countries:
        if(i.text=="a"):
            i.click()
            break
    Utility.click(driver,ElementClient.clientActive)
    Utility.click(driver,ElementClient.clientAddSubmit)


