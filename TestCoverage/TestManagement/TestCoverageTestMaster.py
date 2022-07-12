########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186-Murali.r , Date: 11th July 2022, ID - #85 ||
########################################################################################################################################################################################################################################################################################################################################################
from ObjectRepository.TestManagement import ElementTestMaster
from Utilities import BrowserOperation, Utility


def testMasterAdd(driver):
    Utility.click(driver,ElementTestMaster.masterIcon)
    Utility.click(driver,ElementTestMaster.testManagementIcon)
    Utility.click(driver,ElementTestMaster.testIcon)
    Utility.click(driver,ElementTestMaster.testAdd)

