########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 20th June 2022, ID - #44 ||
########################################################################################################################################################################################################################################################################################################################################################

from GenericMethod.NameDescriptionDefaultStatus import AddDefaultStatusYes
from ObjectRepository.BaseMaster import ElementUnit, ElementStorageCondition, ElementSource
from Screenshot.PossitiveFlow import ScreenshotUnit
from TestData import TestDataFlow
from Utilities import BrowserOperation

driver=BrowserOperation.launchLIMS()
#AddDefaultStatusYes.addDefaultStatusYes(driver,ElementUnit.elementUnit(),ScreenshotUnit.unit(),TestDataFlow.unit())
#AddDefaultStatusYes.addDefaultStatusYes(driver,ElementStorageCondition.elementStorageCondition(),ScreenshotUnit.unit(),TestDataFlow.unit())
AddDefaultStatusYes.addDefaultStatusYes(driver,ElementSource.elementSource(),ScreenshotUnit.unit(),TestDataFlow.unit())
