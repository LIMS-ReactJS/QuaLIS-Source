########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 27th June 2022, ID - #72 ||
########################################################################################################################################################################################################################################################################################################################################################
from ObjectRepository.InstrumentManagement import ElementInstrumentCategory
from Setting import FieldName
from Utilities import Utility


def instrumentCategoryAdd(driver,instrumentCategory):
    Utility.click(driver,ElementInstrumentCategory.masterIcon)
    Utility.click(driver,ElementInstrumentCategory.instrumentManagementIcon)
    Utility.click(driver,ElementInstrumentCategory.instrumentCategoryIcon)
    Utility.click(driver,ElementInstrumentCategory.instrumentCategoryAdd)
    Utility.sendKeys(driver,ElementInstrumentCategory.instrumentCategoryName,instrumentCategory.get(FieldName.instrumentCategoryName))
    Utility.sendKeys(driver,ElementInstrumentCategory.instrumentCategoryDescription,instrumentCategory.get(FieldName.instrumentCategoryDescription))
    Utility.selectByText(driver,ElementInstrumentCategory.instrumentCategoryTechnique,instrumentCategory.get(FieldName.instrumentCategoryTechnique))
    Utility.selectByText(driver,ElementInstrumentCategory.instrumentCategoryInterfaceType,instrumentCategory.get(FieldName.instrumentCategoryInterface))
    Utility.click(driver,ElementInstrumentCategory.instrumentCategoryCategoryBasedFlow)
    Utility.click(driver,ElementInstrumentCategory.instrumentCategoryDefaultStatus)
    Utility.click(driver,ElementInstrumentCategory.instrumentCategoryAddSubmit)

