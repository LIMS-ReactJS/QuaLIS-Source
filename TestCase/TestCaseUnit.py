from GenericMethod.NameDescriptionDefaultStatus import AddDefaultStatusYes
from ObjectRepository.BaseMaster import ElementUnit
from TestData import TestDataFlow
from Utilities import BrowserOperation

driver=BrowserOperation.launchLIMS()
screenshot={"a":"a"}
AddDefaultStatusYes.addDefaultStatusYes(driver,ElementUnit.elementUnit(),screenshot,TestDataFlow.unit())
