########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 27th June 2022, ID - #73 ||
########################################################################################################################################################################################################################################################################################################################################################


from Setting import ObjectName

pin = "//a[@class='text-center nav-link']"

masterIcon="//a[@data-rb-event-key='MenuId_1']"

instrumentManagementIcon="//span[text()='Instrument Management']"

instrumentCategoryIcon="//a[@href='#/instrumentCategory'][@nformcode='27']"

instrumentCategoryAdd="//button[@data-tip='Add']"

instrumentCategoryRefresh="//button[@data-tip='Refresh']"

instrumentCategoryDownloadPDF="//button[@data-tip='Download PDF']"

instrumentCategoryDownloadExcel="//button[@data-tip='Download Excel']"

instrumentCategoryName="//input[@id='sinstrumentcatname'][@name='sinstrumentcatname']"

instrumentCategoryDescription="//*[@id='sdescription'][@name='sdescription']"

instrumentCategoryTechnique="//*[@id='ntechniquecode']"

instrumentCategoryInterfaceType="//*[@id='ninterfacetype']"

instrumentCategoryDefaultStatus="//*[@for='ndefaultstatus']"

instrumentCategoryCategoryBasedFlow="//*[@for='ncategorybasedflow']"

instrumentCategoryAddSubmit="//button[text()='Save']"

instrumentCategoryAddCancel="//button[text()='Cancel']"

instrumentCategoryEditSubmit="//button[text()='Save']"

instrumentCategoryEditCancel="//button[text()='Cancel']"

instrumentCategoryNameList="/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td[1]"

instrumentCategoryDescriptionList="//tbody[@role='presentation']/tr/td[2]"

instrumentCategoryDefaultStatusList="//tbody[@role='presentation']/tr/td[3]"

instrumentCategoryEditList="//tbody[@role='presentation']/tr/td[4]/a/span[1]"

instrumentCategoryDeleteList="//tbody[@role='presentation']/tr/td[4]/a/span[2]"

instrumentCategoryNameFilter="(//span[@class='k-icon k-i-more-vertical'])[1]"

instrumentCategoryDefaultStatusLabel="//label[@for='ndefaultstatus']"

instrumentCategoryDefaultStatusToggle="//input[@name='ndefaultstatus' and @type='checkbox']"

instrumentCategoryTotalCount="//div[@class='k-pager-info k-label']"

instrumentCategoryScreenHeader="//*[@class='navbar-brand']/h2"

instrumentCategoryAddPopupHeader="//div[@class='header-primary flex-grow-1 modal-title h4' and @id='add-user']"

module="Master"

subModule="Instrument Management"

screen="Instrument Category"

def elementInstrumentCategory():

    instrumentCategory={}

    instrumentCategory.update({ObjectName.moduleIcon:masterIcon})

    instrumentCategory.update({ObjectName.subModuleIcon:instrumentManagementIcon})

    instrumentCategory.update({ObjectName.screenIcon:instrumentCategoryIcon})

    instrumentCategory.update({ObjectName.add:instrumentCategoryAdd})

    instrumentCategory.update({ObjectName.name: instrumentCategoryName})

    instrumentCategory.update({ObjectName.description:instrumentCategoryDescription})

    instrumentCategory.update({ObjectName.addSubmit:instrumentCategoryAddSubmit})

    instrumentCategory.update({ObjectName.addCancel:instrumentCategoryAddCancel})

    instrumentCategory.update({ObjectName.screenHeader:instrumentCategoryScreenHeader})

    instrumentCategory.update({ObjectName.module:module})

    instrumentCategory.update({ObjectName.subModule:subModule})

    instrumentCategory.update({ObjectName.screen:screen})

    instrumentCategory.update({ObjectName.addPopupHeader:instrumentCategoryAddPopupHeader})

    instrumentCategory.update({ObjectName.totalCount:instrumentCategoryTotalCount})

    instrumentCategory.update({ObjectName.defaultStatusLabel:instrumentCategoryDefaultStatusLabel})

    instrumentCategory.update({ObjectName.defaultStatusToggle:instrumentCategoryDefaultStatusToggle})

    return instrumentCategory



