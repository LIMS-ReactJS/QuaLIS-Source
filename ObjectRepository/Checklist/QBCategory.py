########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 21st June 2022, ID - #59 ||
########################################################################################################################################################################################################################################################################################################################################################


from Setting import ObjectName

pin = "//a[@class='text-center nav-link']"

masterIcon="//a[@data-rb-event-key='MenuId_1']"

checklistManagementIcon="//span[text()='Checklist']"

QBCategoryIcon="//a[@href='#/qbCategory']"

QBCategoryAdd="//button[@data-tip='Add']"

QBCategoryRefresh="//button[@data-tip='Refresh']"

QBCategoryDownloadPDF="//button[@data-tip='Download PDF']"

QBCategoryDownloadExcel="//button[@data-tip='Download Excel']"

QBCategoryName="//input[@id='schecklistqbcategoryname'][@name='schecklistqbcategoryname']"

QBCategoryDescription="//textarea[@id='sdescription'][@name='sdescription']"

QBCategoryAddSubmit="//button[text()='Save']"

QBCategoryAddCancel="//button[text()='Cancel']"

QBCategoryEditSubmit="//button[text()='Save']"

QBCategoryEditCancel="//button[text()='Cancel']"

QBCategoryNameList="/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td[1]"

QBCategoryDescriptionList="//tbody[@role='presentation']/tr/td[2]"

QBCategoryDefaultStatusList="//tbody[@role='presentation']/tr/td[3]"

QBCategoryEditList="//tbody[@role='presentation']/tr/td[4]/a/span[1]"

QBCategoryDeleteList="//tbody[@role='presentation']/tr/td[4]/a/span[2]"

QBCategoryNameFilter="(//span[@class='k-icon k-i-more-vertical'])[1]"

QBCategoryDefaultStatusLabel="//label[@for='ndefaultstatus']"

QBCategoryDefaultStatusToggle="//input[@name='ndefaultstatus' and @type='checkbox']"

QBCategoryTotalCount="//div[@class='k-pager-info k-label']"

QBCategoryScreenHeader="//*[@class='navbar-brand']/h2"

QBCategoryAddPopupHeader="//div[@class='header-primary flex-grow-1 modal-title h4' and @id='add-user']"

module="Master"

subModule="Base Master"

screen="QBCategory"

def elementQBCategory():

    QBCategory={}

    QBCategory.update({ObjectName.moduleIcon:masterIcon})

    QBCategory.update({ObjectName.subModuleIcon:baseMasterIcon})

    QBCategory.update({ObjectName.screenIcon:QBCategoryIcon})

    QBCategory.update({ObjectName.add:QBCategoryAdd})

    QBCategory.update({ObjectName.name: QBCategoryName})

    QBCategory.update({ObjectName.description:QBCategoryDescription})

    QBCategory.update({ObjectName.addSubmit:QBCategoryAddSubmit})

    QBCategory.update({ObjectName.addCancel:QBCategoryAddCancel})

    QBCategory.update({ObjectName.screenHeader:QBCategoryScreenHeader})

    QBCategory.update({ObjectName.module:module})

    QBCategory.update({ObjectName.subModule:subModule})

    QBCategory.update({ObjectName.screen:screen})

    QBCategory.update({ObjectName.addPopupHeader:QBCategoryAddPopupHeader})

    QBCategory.update({ObjectName.totalCount:QBCategoryTotalCount})

    QBCategory.update({ObjectName.defaultStatusLabel:QBCategoryDefaultStatusLabel})

    QBCategory.update({ObjectName.defaultStatusToggle:QBCategoryDefaultStatusToggle})

    return QBCategory



