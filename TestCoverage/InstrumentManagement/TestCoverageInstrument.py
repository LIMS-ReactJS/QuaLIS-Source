from ObjectRepository.InstrumentManagement import ElementInstrument
from Utilities import Utility

def instrumentAdd(driver):
    Utility.click(driver,ElementInstrument.masterIcon)
    Utility.click(driver,ElementInstrument.instrumentManagementIcon)
    Utility.click(driver,ElementInstrument.instrumentIcon)
    Utility.click(driver,ElementInstrument.instrumentAdd)