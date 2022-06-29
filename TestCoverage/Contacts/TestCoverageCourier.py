########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 29th June 2022, ID - #78 ||
########################################################################################################################################################################################################################################################################################################################################################
from ObjectRepository.Contact import ElementCourier
from Utilities import Utility


def courierAdd(driver,courier):
    Utility.click(driver,ElementCourier.masterIcon)
    Utility.scrollToElement(driver,ElementCourier.contactsIcon)
    Utility.click(driver,ElementCourier.contactsIcon)
    Utility.click(driver,ElementCourier.courierIcon)
    Utility.click(driver,ElementCourier.courierAdd)
    