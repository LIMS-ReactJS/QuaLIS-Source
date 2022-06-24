########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 20th June 2022, ID - #44 ||
########################################################################################################################################################################################################################################################################################################################################################
from GenericMethod.NameDescription import AddNameDescription
from GenericMethod.NameDescriptionDefaultStatus import AddDefaultStatusYes
from ObjectRepository.BaseMaster import ElementUnit, ElementStorageCondition, ElementSource, ElementStorageLocation, \
    ElementContainerType
from ObjectRepository.Checklist import ElementQBCategory
from ObjectRepository.CompetenceManagement import ElementTechnique
from ObjectRepository.Contact import ElementSupplierCategory
from ObjectRepository.Organisation import ElementDivision, ElementLab, ElementSection
from ObjectRepository.ProjectManagement import ElementProductCategory
from ObjectRepository.TestManagement import ElementTestCategory, ElementMethodCategory
from ObjectRepository.UserManagement import ElementDesignation, ElementUserRole
from Screenshot.PossitiveFlow import ScreenshotUnit
from TestCoverage.Configuration import TestCoveragePasswordPolicy
from TestData import TestDataFlow
from Utilities import BrowserOperation, Utility

driver=BrowserOperation.launchLIMS()

TestCoveragePasswordPolicy.passwordPolicyAddApprove(driver,TestDataFlow.userRoleReviewer)
TestCoveragePasswordPolicy.passwordPolicyAddApprove(driver,TestDataFlow.userRoleApprover)
TestCoveragePasswordPolicy.passwordPolicyAddApprove(driver,TestDataFlow.userRoleAnalyst)
quit()
AddNameDescription.addNameDescription(driver,ElementSupplierCategory.elementSupplierCategory(),ScreenshotUnit.unit(),TestDataFlow.productCategory())
AddNameDescription.addNameDescription(driver,ElementQBCategory.elementQBCategory(),ScreenshotUnit.unit(),TestDataFlow.productCategory())
AddNameDescription.addNameDescription(driver,ElementMethodCategory.elementMethodCategory(),ScreenshotUnit.unit(),TestDataFlow.productCategory())
AddNameDescription.addNameDescription(driver,ElementSection.elementSection(),ScreenshotUnit.unit(),TestDataFlow.productCategory())
AddNameDescription.addNameDescription(driver,ElementUserRole.elementUserRole(),ScreenshotUnit.unit(),TestDataFlow.productCategory())
AddNameDescription.addNameDescription(driver,ElementContainerType.elementContainerType(),ScreenshotUnit.unit(),TestDataFlow.productCategory())
AddNameDescription.addNameDescription(driver,ElementStorageLocation.elementStorageLocation(),ScreenshotUnit.unit(),TestDataFlow.productCategory())
AddDefaultStatusYes.addDefaultStatusYes(driver,ElementProductCategory.elementProductCategory(),ScreenshotUnit.unit(),TestDataFlow.productCategory())
AddDefaultStatusYes.addDefaultStatusYes(driver,ElementTestCategory.elementTestCategory(),ScreenshotUnit.unit(),TestDataFlow.testCategory())
AddDefaultStatusYes.addDefaultStatusYes(driver,ElementLab.elementLab(),ScreenshotUnit.unit(),TestDataFlow.lab())
AddDefaultStatusYes.addDefaultStatusYes(driver,ElementDivision.elementDivision(),ScreenshotUnit.unit(),TestDataFlow.division())
AddDefaultStatusYes.addDefaultStatusYes(driver,ElementDesignation.elementDesignation(),ScreenshotUnit.unit(),TestDataFlow.designation())
AddDefaultStatusYes.addDefaultStatusYes(driver,ElementUnit.elementUnit(),ScreenshotUnit.unit(),TestDataFlow.unit())
AddDefaultStatusYes.addDefaultStatusYes(driver,ElementStorageCondition.elementStorageCondition(),ScreenshotUnit.unit(),TestDataFlow.storageCondition())
AddDefaultStatusYes.addDefaultStatusYes(driver,ElementSource.elementSource(),ScreenshotUnit.unit(),TestDataFlow.source())
