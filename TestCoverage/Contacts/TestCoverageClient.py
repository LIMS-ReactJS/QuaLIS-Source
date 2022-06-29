########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 29th June 2022, ID - #79 ||
########################################################################################################################################################################################################################################################################################################################################################
from selenium.webdriver.common.by import By

from ObjectRepository.Contact import ElementClient
from Setting import FieldName
from Utilities import Utility


def clientAdd(driver,client):
    Utility.click(driver,ElementClient.masterIcon)
    Utility.scrollToElement(driver,ElementClient.contactsIcon)
    Utility.click(driver,ElementClient.contactsIcon)
    Utility.click(driver,ElementClient.clientIcon)
    Utility.click(driver,ElementClient.clientAdd)
    Utility.sendKeys(driver,ElementClient.clientName,client.get(FieldName.clientName))
    Utility.sendKeys(driver,ElementClient.clientAddressOne,client.get(FieldName.clientAddressOne))
    Utility.sendKeys(driver,ElementClient.clientAddressTwo,client.get(FieldName.clientAddressTwo))
    Utility.sendKeys(driver,ElementClient.clientAddressThree,client.get(FieldName.clientAddressThree))
    Utility.sendKeys(driver,ElementClient.clientPhoneNumber,client.get(FieldName.clientPhoneNumber))
    Utility.sendKeys(driver,ElementClient.clientMobileNumber,client.get(FieldName.clientMobileNumber))
    Utility.sendKeys(driver,ElementClient.clientFaxNumber,client.get(FieldName.clientFaxNumber))
    Utility.sendKeys(driver,ElementClient.clientEmail,client.get(FieldName.clientEmail))
    Utility.click(driver,ElementClient.clientCountry)
    countries=driver.find_elements(By.XPATH,"//*[@id='ncountrycode']/div[2]/div/div")
    for i in countries:
        if(i.text==client.get(FieldName.clientCountry)):
            i.click()
            break
    Utility.click(driver,ElementClient.clientActive)
    Utility.click(driver,ElementClient.clientAddSubmit)


