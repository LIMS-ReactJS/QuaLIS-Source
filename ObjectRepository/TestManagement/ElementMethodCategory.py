########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 21st June 2022, ID - #58 ||
########################################################################################################################################################################################################################################################################################################################################################


from Setting import ObjectName

pin = "//a[@class='text-center nav-link']"

masterIcon="//a[@data-rb-event-key='MenuId_1']"

testManagementIcon="//span[text()='Test Management']"

methodCategoryIcon="//a[@href='#/methodCategory']"

methodCategoryAdd="//button[@data-tip='Add']"

methodCategoryRefresh="//button[@data-tip='Refresh']"

methodCategoryDownloadPDF="//button[@data-tip='Download PDF']"

methodCategoryDownloadExcel="//button[@data-tip='Download Excel']"

methodCategoryName="//input[@id='smethodcatname'][@name='smethodcatname']"

methodCategoryDescription="//textarea[@id='sdescription'][@name='sdescription']"

methodCategoryAddSubmit="//button[text()='Save']"

methodCategoryAddCancel="//button[text()='Cancel']"

methodCategoryEditSubmit="//button[text()='Save']"

methodCategoryEditCancel="//button[text()='Cancel']"

methodCategoryNameList="/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td[1]"

methodCategoryDescriptionList="//tbody[@role='presentation']/tr/td[2]"

methodCategoryDefaultStatusList="//tbody[@role='presentation']/tr/td[3]"

methodCategoryEditList="//tbody[@role='presentation']/tr/td[4]/a/span[1]"

methodCategoryDeleteList="//tbody[@role='presentation']/tr/td[4]/a/span[2]"

methodCategoryNameFilter="(//span[@class='k-icon k-i-more-vertical'])[1]"

methodCategoryDefaultStatusLabel="//label[@for='ndefaultstatus']"

methodCategoryDefaultStatusToggle="//input[@name='ndefaultstatus' and @type='checkbox']"

methodCategoryTotalCount="//div[@class='k-pager-info k-label']"

methodCategoryScreenHeader="//*[@class='navbar-brand']/h2"

methodCategoryAddPopupHeader="//div[@class='header-primary flex-grow-1 modal-title h4' and @id='add-user']"

module="Master"

subModule="Base Master"

screen="methodCategory"

def elementMethodCategory():

    methodCategory={}

    methodCategory.update({ObjectName.moduleIcon:masterIcon})

    methodCategory.update({ObjectName.subModuleIcon:testManagementIcon})

    methodCategory.update({ObjectName.screenIcon:methodCategoryIcon})

    methodCategory.update({ObjectName.add:methodCategoryAdd})

    methodCategory.update({ObjectName.name: methodCategoryName})

    methodCategory.update({ObjectName.description:methodCategoryDescription})

    methodCategory.update({ObjectName.addSubmit:methodCategoryAddSubmit})

    methodCategory.update({ObjectName.addCancel:methodCategoryAddCancel})

    methodCategory.update({ObjectName.screenHeader:methodCategoryScreenHeader})

    methodCategory.update({ObjectName.module:module})

    methodCategory.update({ObjectName.subModule:subModule})

    methodCategory.update({ObjectName.screen:screen})

    methodCategory.update({ObjectName.addPopupHeader:methodCategoryAddPopupHeader})

    methodCategory.update({ObjectName.totalCount:methodCategoryTotalCount})

    methodCategory.update({ObjectName.defaultStatusLabel:methodCategoryDefaultStatusLabel})

    methodCategory.update({ObjectName.defaultStatusToggle:methodCategoryDefaultStatusToggle})

    return methodCategory



