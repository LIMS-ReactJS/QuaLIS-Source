########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 24th June 2022, ID - #66 ||
########################################################################################################################################################################################################################################################################################################################################################
from ObjectRepository.Contact import ElementCountry
from Setting import FieldName
from Utilities import Utility


def countryAdd(driver,testData):
    Utility.click(driver,ElementCountry.masterIcon)
    Utility.scrollToElement(driver,ElementCountry.contactsIcon)
    Utility.click(driver,ElementCountry.contactsIcon)
    Utility.scrollToElement(driver,ElementCountry.countryIcon)
    Utility.click(driver,ElementCountry.countryIcon)
    Utility.click(driver,ElementCountry.countryAdd)
    Utility.sendKeys(driver,ElementCountry.countryName,testData.get(FieldName.countryName))
    Utility.sendKeys(driver,ElementCountry.countryShortName,testData.get(FieldName.countryShortName))
    Utility.sendKeys(driver,ElementCountry.countryTwoChar,testData.get(FieldName.countryTwoChar))
    Utility.sendKeys(driver,ElementCountry.countryThreeChar,testData.get(FieldName.countryThreeChar))
    Utility.click(driver,ElementCountry.countryAddSubmit)



