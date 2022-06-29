########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 29th June 2022, ID - #78 ||
########################################################################################################################################################################################################################################################################################################################################################
from selenium.webdriver.common.by import By

from ObjectRepository.Contact import ElementCourier
from Setting import FieldName
from Utilities import Utility


def courierAdd(driver,courier):
    Utility.click(driver,ElementCourier.masterIcon)
    Utility.scrollToElement(driver,ElementCourier.contactsIcon)
    Utility.click(driver,ElementCourier.contactsIcon)
    Utility.click(driver,ElementCourier.courierIcon)
    Utility.click(driver,ElementCourier.courierAdd)
    Utility.sendKeys(driver,ElementCourier.courierName,courier.get(FieldName.courierName))
    Utility.sendKeys(driver,ElementCourier.courierContactsPerson,courier.get(FieldName.courierContactPerson))
    Utility.sendKeys(driver,ElementCourier.courierAddressOne,courier.get(FieldName.courierAddressOne))
    Utility.sendKeys(driver,ElementCourier.courierAddressTwo,courier.get(FieldName.courierAddressTwo))
    Utility.sendKeys(driver,ElementCourier.courierAddressThree,courier.get(FieldName.courierAddressThree))
    Utility.sendKeys(driver,ElementCourier.courierPhoneNumber,courier.get(FieldName.courierPhoneNumber))
    Utility.sendKeys(driver,ElementCourier.courierMobileNumber,courier.get(FieldName.courierMobileNumber))
    Utility.sendKeys(driver,ElementCourier.courierFaxNumber,courier.get(FieldName.courierFaxNumber))
    Utility.sendKeys(driver,ElementCourier.courierEmail,courier.get(FieldName.courierEmail))
    Utility.click(driver,ElementCourier.courierCountry)
    countries=driver.find_elements(By.XPATH,"//*[@id='ncountrycode']/div[2]/div/div")
    for i in countries:
        print(i.text)
        print(courier.get(FieldName.courierCountry))
        if (i.text==courier.get(FieldName.courierCountry)):
            i.click()
            print("matched")
            break
    Utility.click(driver,ElementCourier.courierAddSubmit)