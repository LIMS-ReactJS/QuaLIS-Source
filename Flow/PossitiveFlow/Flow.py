########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 20th June 2022, ID - #44 ||
########################################################################################################################################################################################################################################################################################################################################################

from GenericMethod.NameDescriptionDefaultStatus import AddDefaultStatusYes
from ObjectRepository.BaseMaster import ElementUnit, ElementStorageCondition, ElementSource
from ObjectRepository.Organisation import ElementDivision, ElementLab
from ObjectRepository.ProjectManagement import ElementProductCategory
from ObjectRepository.TestManagement import ElementTestCategory
from ObjectRepository.UserManagement import ElementDesignation
from Screenshot.PossitiveFlow import ScreenshotUnit
from TestData import TestDataFlow
from Utilities import BrowserOperation


driver=BrowserOperation.launchLIMS()
AddDefaultStatusYes.addDefaultStatusYes(driver,ElementProductCategory.elementProductCategory(),ScreenshotUnit.unit(),TestDataFlow.productCategory())
AddDefaultStatusYes.addDefaultStatusYes(driver,ElementTestCategory.elementTestCategory(),ScreenshotUnit.unit(),TestDataFlow.testCategory())
AddDefaultStatusYes.addDefaultStatusYes(driver,ElementLab.elementLab(),ScreenshotUnit.unit(),TestDataFlow.lab())
AddDefaultStatusYes.addDefaultStatusYes(driver,ElementDivision.elementDivision(),ScreenshotUnit.unit(),TestDataFlow.division())
AddDefaultStatusYes.addDefaultStatusYes(driver,ElementDesignation.elementDesignation(),ScreenshotUnit.unit(),TestDataFlow.designation())
AddDefaultStatusYes.addDefaultStatusYes(driver,ElementUnit.elementUnit(),ScreenshotUnit.unit(),TestDataFlow.unit())
AddDefaultStatusYes.addDefaultStatusYes(driver,ElementStorageCondition.elementStorageCondition(),ScreenshotUnit.unit(),TestDataFlow.storageCondition())
AddDefaultStatusYes.addDefaultStatusYes(driver,ElementSource.elementSource(),ScreenshotUnit.unit(),TestDataFlow.source())
