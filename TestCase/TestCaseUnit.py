from GenericMethod.NameDescriptionDefaultStatus import AddDefaultStatusYes
from ObjectRepository.BaseMaster import ElementUnit
from Screenshot.PossitiveFlow import ScreenshotUnit
from TestData import TestDataFlow
from Utilities import BrowserOperation

driver=BrowserOperation.launchLIMS()
AddDefaultStatusYes.addDefaultStatusYes(driver,ElementUnit.elementUnit(),ScreenshotUnit.unit(),TestDataFlow.unit())
