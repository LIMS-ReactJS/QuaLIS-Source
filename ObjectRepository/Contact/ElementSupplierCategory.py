########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 21st June 2022, ID - #60 ||
########################################################################################################################################################################################################################################################################################################################################################


from Setting import ObjectName

pin = "//a[@class='text-center nav-link']"

masterIcon="//a[@data-rb-event-key='MenuId_1']"

contactsIcon="//span[text()='Contacts']"

supplierCategoryIcon="//a[@href='#/supplierCategory']"

supplierCategoryAdd="//button[@data-tip='Add']"

supplierCategoryRefresh="//button[@data-tip='Refresh']"

supplierCategoryDownloadPDF="//button[@data-tip='Download PDF']"

supplierCategoryDownloadExcel="//button[@data-tip='Download Excel']"

supplierCategoryName="//input[@id='ssuppliercatname'][@name='ssuppliercatname']"

supplierCategoryDescription="//textarea[@id='sdescription'][@name='sdescription']"

supplierCategoryAddSubmit="//button[text()='Save']"

supplierCategoryAddCancel="//button[text()='Cancel']"

supplierCategoryEditSubmit="//button[text()='Save']"

supplierCategoryEditCancel="//button[text()='Cancel']"

supplierCategoryNameList="/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td[1]"

supplierCategoryDescriptionList="//tbody[@role='presentation']/tr/td[2]"

supplierCategoryDefaultStatusList="//tbody[@role='presentation']/tr/td[3]"

supplierCategoryEditList="//tbody[@role='presentation']/tr/td[4]/a/span[1]"

supplierCategoryDeleteList="//tbody[@role='presentation']/tr/td[4]/a/span[2]"

supplierCategoryNameFilter="(//span[@class='k-icon k-i-more-vertical'])[1]"

supplierCategoryDefaultStatusLabel="//label[@for='ndefaultstatus']"

supplierCategoryDefaultStatusToggle="//input[@name='ndefaultstatus' and @type='checkbox']"

supplierCategoryTotalCount="//div[@class='k-pager-info k-label']"

supplierCategoryScreenHeader="//*[@class='navbar-brand']/h2"

supplierCategoryAddPopupHeader="//div[@class='header-primary flex-grow-1 modal-title h4' and @id='add-user']"

module="Master"

subModule="Base Master"

screen="supplierCategory"

def elementsupplierCategory():

    supplierCategory={}

    supplierCategory.update({ObjectName.moduleIcon:masterIcon})

    supplierCategory.update({ObjectName.subModuleIcon:baseMasterIcon})

    supplierCategory.update({ObjectName.screenIcon:supplierCategoryIcon})

    supplierCategory.update({ObjectName.add:supplierCategoryAdd})

    supplierCategory.update({ObjectName.name: supplierCategoryName})

    supplierCategory.update({ObjectName.description:supplierCategoryDescription})

    supplierCategory.update({ObjectName.addSubmit:supplierCategoryAddSubmit})

    supplierCategory.update({ObjectName.addCancel:supplierCategoryAddCancel})

    supplierCategory.update({ObjectName.screenHeader:supplierCategoryScreenHeader})

    supplierCategory.update({ObjectName.module:module})

    supplierCategory.update({ObjectName.subModule:subModule})

    supplierCategory.update({ObjectName.screen:screen})

    supplierCategory.update({ObjectName.addPopupHeader:supplierCategoryAddPopupHeader})

    supplierCategory.update({ObjectName.totalCount:supplierCategoryTotalCount})

    supplierCategory.update({ObjectName.defaultStatusLabel:supplierCategoryDefaultStatusLabel})

    supplierCategory.update({ObjectName.defaultStatusToggle:supplierCategoryDefaultStatusToggle})

    return supplierCategory



