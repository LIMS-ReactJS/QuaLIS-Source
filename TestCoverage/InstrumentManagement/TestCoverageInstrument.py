import time

from selenium.webdriver.common.by import By

from ObjectRepository.InstrumentManagement import ElementInstrument
from Setting import FieldName
from Utilities import Utility

def instrumentAdd(driver,instrument):
    Utility.click(driver,ElementInstrument.masterIcon)
    Utility.click(driver,ElementInstrument.instrumentManagementIcon)
    Utility.click(driver,ElementInstrument.instrumentIcon)
    Utility.click(driver,ElementInstrument.instrumentAdd)
    Utility.click(driver,ElementInstrument.instrumentCategoryName)
    instrumentCategory=driver.find_elements(By.XPATH,"//*[@id='ninstrumentcatcode']/div[2]/div/div")
    for i in instrumentCategory:
        if (i.text==instrument.get(FieldName.instrumentCategoryName)):
            i.click()
            break
    Utility.sendKeys(driver,ElementInstrument.instrumentID,instrument.get(FieldName.instrumentID))
    Utility.sendKeys(driver,ElementInstrument.instrumentName,instrument.get(FieldName.instrumentName))
    Utility.click(driver,ElementInstrument.instrumentSupplier)
    suppliers=driver.find_elements(By.XPATH,"//*[@id='nsuppliercode']/div[2]/div/div")
    for i in suppliers:
        if (i.text==instrument.get(FieldName.instrumentSupplier)):
            i.click()
            break
        else:
           pass
    Utility.sendKeys(driver,ElementInstrument.instrumentSerialNumber,instrument.get(FieldName.instrumentSerialNumber))
    Utility.calender(driver,ElementInstrument.instrumentManufacturerDate,instrument.get(FieldName.instrumentManufacturerDate))
    Utility.calender(driver,ElementInstrument.instrumentPODate,instrument.get(FieldName.instrumentPODate))
    Utility.calender(driver,ElementInstrument.instrumentReceivedDate,instrument.get(FieldName.instrumentReceivedDate))
    Utility.calender(driver,ElementInstrument.instrumentInstallationDate,instrument.get(FieldName.instrumentInstallationDate))
    Utility.calender(driver,ElementInstrument.instrumentExpireDate,instrument.get(FieldName.instrumentExpireDate))
