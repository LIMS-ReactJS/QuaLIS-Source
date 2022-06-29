########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 29th June 2022, ID - #82 ||
########################################################################################################################################################################################################################################################################################################################################################
from selenium.webdriver.common.by import By

from ObjectRepository.Contact import ElementMAHolder
from Setting import FieldName
from Utilities import Utility

def MAHolderAdd(driver,MAHolder):
    Utility.click(driver,ElementMAHolder.masterIcon)
    Utility.scrollToElement(driver,ElementMAHolder.contactsIcon)
    Utility.click(driver,ElementMAHolder.contactsIcon)
    Utility.scrollToElement(driver,ElementMAHolder.MAHolderIcon)
    Utility.click(driver,ElementMAHolder.MAHolderIcon)
    Utility.click(driver,ElementMAHolder.MAHolderAdd)
    Utility.sendKeys(driver,ElementMAHolder.MAHolderName,MAHolder.get(FieldName.MAHolderName))
    Utility.sendKeys(driver,ElementMAHolder.MAHolderAddressOne,MAHolder.get(FieldName.MAHolderAddressOne))
    Utility.sendKeys(driver,ElementMAHolder.MAHolderAddressTwo,MAHolder.get(FieldName.MAHolderAddressTwo))
    Utility.sendKeys(driver,ElementMAHolder.MAHolderAddressThree,MAHolder.get(FieldName.MAHolderAddressThree))
    Utility.click(driver,ElementMAHolder.MAHolderCountry)
    countries=driver.find_elements(By.XPATH,"//*[@id='ncountrycode']/div[2]/div/div")
    for i in countries:
        print(i)
        if (i.text==MAHolder.get(FieldName.MAHolderCountry)):
            i.click()
            break
    Utility.click(driver,ElementMAHolder.MAHolderAddSubmit)

