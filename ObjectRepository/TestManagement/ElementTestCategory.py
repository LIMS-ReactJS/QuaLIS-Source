########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 21st June 2022, ID - #49 ||
########################################################################################################################################################################################################################################################################################################################################################

from Setting import ObjectName

pin = "//a[@class='text-center nav-link']"

masterIcon="//a[@data-rb-event-key='MenuId_1']"

userManagementIcon="//span[text()='Test Management']"

testCategoryIcon="//a[@href='#/testCategory']"

testCategoryAdd="//button[@data-tip='Add']"

testCategoryRefresh="//button[@data-tip='Refresh']"

testCategoryDownloadPDF="//button[@data-tip='Download PDF']"

testCategoryDownloadExcel="//button[@data-tip='Download Excel']"

testCategoryName="//input[@id='stestcategoryname'][@name='stestcategoryname']"

testCategoryDescription="//textarea[@id='sdescription'][@name='sdescription']"

testCategoryAddSubmit="//button[text()='Save']"

testCategoryAddCancel="//button[text()='Cancel']"

testCategoryEditSubmit="//button[text()='Save']"

testCategoryEditCancel="//button[text()='Cancel']"

testCategoryNameList="/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td[1]"

testCategoryDescriptionList="//tbody[@role='presentation']/tr/td[2]"

testCategoryDefaultStatusList="//tbody[@role='presentation']/tr/td[3]"

testCategoryEditList="//tbody[@role='presentation']/tr/td[4]/a/span[1]"

testCategoryDeleteList="//tbody[@role='presentation']/tr/td[4]/a/span[2]"

testCategoryNameFilter="(//span[@class='k-icon k-i-more-vertical'])[1]"

testCategoryDefaultStatusLabel="//label[@for='ndefaultstatus']"

testCategoryDefaultStatusToggle="//input[@name='ndefaultstatus' and @type='checkbox']"

testCategoryTotalCount="//div[@class='k-pager-info k-label']"

testCategoryScreenHeader="//*[@class='navbar-brand']/h2"

testCategoryAddPopupHeader="//div[@class='header-primary flex-grow-1 modal-title h4' and @id='add-user']"

module="Master"

subModule="Base Master"

screen="testCategory"

def elementCestCategory():

    testCategory={}

    testCategory.update({ObjectName.moduleIcon:masterIcon})

    testCategory.update({ObjectName.subModuleIcon:userManagementIcon})

    testCategory.update({ObjectName.screenIcon:testCategoryIcon})

    testCategory.update({ObjectName.add:testCategoryAdd})

    testCategory.update({ObjectName.name: testCategoryName})

    testCategory.update({ObjectName.description:testCategoryDescription})

    testCategory.update({ObjectName.addSubmit:testCategoryAddSubmit})

    testCategory.update({ObjectName.addCancel:testCategoryAddCancel})

    testCategory.update({ObjectName.screenHeader:testCategoryScreenHeader})

    testCategory.update({ObjectName.module:module})

    testCategory.update({ObjectName.subModule:subModule})

    testCategory.update({ObjectName.screen:screen})

    testCategory.update({ObjectName.addPopupHeader:testCategoryAddPopupHeader})

    testCategory.update({ObjectName.totalCount:testCategoryTotalCount})

    testCategory.update({ObjectName.defaultStatusLabel:testCategoryDefaultStatusLabel})

    testCategory.update({ObjectName.defaultStatusToggle:testCategoryDefaultStatusToggle})

    return testCategory



