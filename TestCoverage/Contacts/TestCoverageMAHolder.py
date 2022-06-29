########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 29th June 2022, ID - #82 ||
########################################################################################################################################################################################################################################################################################################################################################
from ObjectRepository.Contact import ElementMAHolder
from Setting import FieldName
from Utilities import Utility

def MAHolderAdd(driver):
    Utility.click(driver,ElementMAHolder.masterIcon)
    Utility.scrollToElement(driver,ElementMAHolder.contactsIcon)
    Utility.click(driver,ElementMAHolder.contactsIcon)
    Utility.scrollToElement(driver,ElementMAHolder.MAHolderIcon)
    Utility.click(driver,ElementMAHolder.MAHolderIcon)
    
