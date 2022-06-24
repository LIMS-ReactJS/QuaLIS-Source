########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 24th June 2022, ID - #66 ||
########################################################################################################################################################################################################################################################################################################################################################
from ObjectRepository.Contact import ElementCountry
from Utilities import Utility


def countryAdd(driver, countryName,countryShortName,countryTwoChar,countryThreeChar):
    Utility.click(driver,ElementCountry.masterIcon)
    Utility.scrollToElement(driver,ElementCountry.contactsIcon)
    Utility.click(driver,ElementCountry.contactsIcon)
    Utility.scrollToElement(driver,ElementCountry.countryIcon)
    Utility.click(driver,ElementCountry.countryIcon)
    Utility.click(driver,ElementCountry.countryAdd)
    Utility.sendKeys(driver,ElementCountry.countryName,countryName)
    Utility.sendKeys(driver,ElementCountry.countryShortName,countryShortName)
    Utility.sendKeys(driver,ElementCountry.countryTwoChar,countryTwoChar)
    Utility.sendKeys(driver,ElementCountry.countryThreeChar,countryThreeChar)
    Utility.click(driver,ElementCountry.countryAddSubmit)



