########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 20th June 2022, ID - #44 ||
########################################################################################################################################################################################################################################################################################################################################################

from GenericMethod.NameDescriptionDefaultStatus import AddDefaultStatusYes
from ObjectRepository.BaseMaster import ElementUnit, ElementStorageCondition, ElementSource
from ObjectRepository.Organisation import ElementDivision, ElementLab
from ObjectRepository.TestManagement import ElementTestCategory
from ObjectRepository.UserManagement import ElementDesignation
from Screenshot.PossitiveFlow import ScreenshotUnit
from TestData import TestDataFlow
from Utilities import BrowserOperation

driver=BrowserOperation.launchLIMS()

AddDefaultStatusYes.addDefaultStatusYes(driver,ElementProductCategory,ScreenshotUnit.unit(),TestDataFlow.unit())

AddDefaultStatusYes.addDefaultStatusYes(driver,ElementTestCategory.elementCestCategory(),ScreenshotUnit.unit(),TestDataFlow.unit())
#AddDefaultStatusYes.addDefaultStatusYes(driver,ElementLab.elementLab(),ScreenshotUnit.unit(),TestDataFlow.unit())
#AddDefaultStatusYes.addDefaultStatusYes(driver,ElementDivision.elementDivision(),ScreenshotUnit.unit(),TestDataFlow.unit())
#AddDefaultStatusYes.addDefaultStatusYes(driver,ElementDesignation.elementDesignation(),ScreenshotUnit.unit(),TestDataFlow.unit())
#AddDefaultStatusYes.addDefaultStatusYes(driver,ElementUnit.elementUnit(),ScreenshotUnit.unit(),TestDataFlow.unit())
#AddDefaultStatusYes.addDefaultStatusYes(driver,ElementStorageCondition.elementStorageCondition(),ScreenshotUnit.unit(),TestDataFlow.unit())
#AddDefaultStatusYes.addDefaultStatusYes(driver,ElementSource.elementSource(),ScreenshotUnit.unit(),TestDataFlow.unit())
