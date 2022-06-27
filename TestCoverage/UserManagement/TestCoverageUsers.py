from ObjectRepository.UserManagement import ElementUsers
from Setting import FieldName
from Utilities import Utility


def userAdd(driver,testData):
    Utility.click(driver,ElementUsers.masterIcon)
    Utility.click(driver,ElementUsers.userManagementIcon)
    Utility.click(driver,ElementUsers.usersIcon)
    Utility.click(driver,ElementUsers.usersAdd)
    Utility.sendKeys(driver,ElementUsers.usersLoginID,testData.get(FieldName.usersLoginID))
    Utility.sendKeys(driver,ElementUsers.usersFirstName,testData.get(FieldName.usersFirstName))
    Utility.sendKeys(driver,ElementUsers.usersLastName,testData.get(FieldName.usersLastName))
    Utility.sendKeys(driver,ElementUsers.usersInitial,testData.get(FieldName.usersInitial))
    Utility.sendKeys(driver,ElementUsers.usersQualification,testData.get(FieldName.usersQualification))
    Utility.sendKeys(driver,ElementUsers.usersBloodGroup,testData.get(FieldName.usersQualification))
    Utility.sendKeys(driver,ElementUsers.usersJobDescription,testData.get(FieldName.usersJobDescription))
    Utility.sendKeys(driver,ElementUsers.usersEmail,testData.get(FieldName.usersEmail))
    Utility.sendKeys(driver,ElementUsers.usersMobileNumber,testData.get(FieldName.usersMobileNumber))
    Utility.sendKeys(driver,ElementUsers.usersPhoneNumber,testData.get(FieldName.usersPhoneNumber))
    Utility.selectByText(driver,ElementUsers.usersDivision,testData.get(FieldName.usersDivision))
    Utility.selectByText(driver,ElementUsers.usersDesignation,testData.get(FieldName.usersDesignation))
    Utility.selectByText(driver,ElementUsers.usersCountry,testData.get(FieldName.usersCountry))
    Utility.sendKeys(driver,ElementUsers.usersAddressOne,testData.get(FieldName.usersAddressOne))
    Utility.sendKeys(driver,ElementUsers.usersAddressTwo,testData.get(FieldName.usersAddressTwo))
    Utility.click(driver,ElementUsers.usersAddSubmit)



