########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 27th June 2022, ID - #71 ||
########################################################################################################################################################################################################################################################################################################################################################
from ObjectRepository.BaseMaster import ElementChargeBand
from Setting import FieldName
from Utilities import Utility


def chargeBandAdd(driver,chargeBand):
    Utility.click(driver,ElementChargeBand.masterIcon)
    Utility.click(driver,ElementChargeBand.baseMasterIcon)
    Utility.click(driver,ElementChargeBand.chargeBandIcon)
    Utility.click(driver,ElementChargeBand.chargeBandAdd)
    Utility.sendKeys(driver,ElementChargeBand.chargeBandName,chargeBand.get(FieldName.chargeBandName))
    Utility.sendKeys(driver,ElementChargeBand.chargeBandDescription,chargeBand.get(FieldName.chargeBandDescription))
    Utility.sendKeys(driver,ElementChargeBand.chargeBandPrice,chargeBand.get(FieldName.chargeBandDescription))
    Utility.click(driver,ElementChargeBand.chargeBandAddSubmit)
