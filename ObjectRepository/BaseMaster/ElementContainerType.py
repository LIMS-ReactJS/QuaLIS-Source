########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 21st June 2022, ID - #55 ||
########################################################################################################################################################################################################################################################################################################################################################


from Setting import ObjectName

pin = "//a[@class='text-center nav-link']"

masterIcon="//a[@data-rb-event-key='MenuId_1']"

baseMasterIcon="//span[text()='Base Master']"

containerTypeIcon="//a[@href='#/containerType']"

containerTypeAdd="//button[@data-tip='Add']"

containerTypeRefresh="//button[@data-tip='Refresh']"

containerTypeDownloadPDF="//button[@data-tip='Download PDF']"

containerTypeDownloadExcel="//button[@data-tip='Download Excel']"

containerTypeName="//input[@id='scontainertype'][@name='scontainertype']"

containerTypeDescription="//textarea[@id='sdescription'][@name='sdescription']"

containerTypeAddSubmit="//button[text()='Save']"

containerTypeAddCancel="//button[text()='Cancel']"

containerTypeEditSubmit="//button[text()='Save']"

containerTypeEditCancel="//button[text()='Cancel']"

containerTypeNameList="/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td[1]"

containerTypeDescriptionList="//tbody[@role='presentation']/tr/td[2]"

containerTypeDefaultStatusList="//tbody[@role='presentation']/tr/td[3]"

containerTypeEditList="//tbody[@role='presentation']/tr/td[4]/a/span[1]"

containerTypeDeleteList="//tbody[@role='presentation']/tr/td[4]/a/span[2]"

containerTypeNameFilter="(//span[@class='k-icon k-i-more-vertical'])[1]"

containerTypeDefaultStatusLabel="//label[@for='ndefaultstatus']"

containerTypeDefaultStatusToggle="//input[@name='ndefaultstatus' and @type='checkbox']"

containerTypeTotalCount="//div[@class='k-pager-info k-label']"

containerTypeScreenHeader="//*[@class='navbar-brand']/h2"

containerTypeAddPopupHeader="//div[@class='header-primary flex-grow-1 modal-title h4' and @id='add-user']"

module="Master"

subModule="Base Master"

screen="Container Type"

def elementContainerType():

    containerType={}

    containerType.update({ObjectName.moduleIcon:masterIcon})

    containerType.update({ObjectName.subModuleIcon:baseMasterIcon})

    containerType.update({ObjectName.screenIcon:containerTypeIcon})

    containerType.update({ObjectName.add:containerTypeAdd})

    containerType.update({ObjectName.name: containerTypeName})

    containerType.update({ObjectName.description:containerTypeDescription})

    containerType.update({ObjectName.addSubmit:containerTypeAddSubmit})

    containerType.update({ObjectName.addCancel:containerTypeAddCancel})

    containerType.update({ObjectName.screenHeader:containerTypeScreenHeader})

    containerType.update({ObjectName.module:module})

    containerType.update({ObjectName.subModule:subModule})

    containerType.update({ObjectName.screen:screen})

    containerType.update({ObjectName.addPopupHeader:containerTypeAddPopupHeader})

    containerType.update({ObjectName.totalCount:containerTypeTotalCount})

    containerType.update({ObjectName.defaultStatusLabel:containerTypeDefaultStatusLabel})

    containerType.update({ObjectName.defaultStatusToggle:containerTypeDefaultStatusToggle})

    return containerType



