########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 20th June 2022, ID - #46 ||
########################################################################################################################################################################################################################################################################################################################################################

from Setting import ObjectName

pin = "//a[@class='text-center nav-link']"

masterIcon="//a[@data-rb-event-key='MenuId_1']"

userManagementIcon="//span[text()='User Management']"

designationIcon="//a[@href='#/designation']"

designationAdd="//button[@data-tip='Add']"

designationRefresh="//button[@data-tip='Refresh']"

designationDownloadPDF="//button[@data-tip='Download PDF']"

designationDownloadExcel="//button[@data-tip='Download Excel']"

designationName="//input[@id='sdesignationname'][@name='sdesignationname']"

designationDescription="//textarea[@id='sdescription'][@name='sdescription']"

designationAddSubmit="//button[text()='Save']"

designationAddCancel="//button[text()='Cancel']"

designationEditSubmit="//button[text()='Save']"

designationEditCancel="//button[text()='Cancel']"

designationNameList="/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td[1]"

designationDescriptionList="//tbody[@role='presentation']/tr/td[2]"

designationDefaultStatusList="//tbody[@role='presentation']/tr/td[3]"

designationEditList="//tbody[@role='presentation']/tr/td[4]/a/span[1]"

designationDeleteList="//tbody[@role='presentation']/tr/td[4]/a/span[2]"

designationNameFilter="(//span[@class='k-icon k-i-more-vertical'])[1]"

designationDefaultStatusLabel="//label[@for='ndefaultstatus']"

designationDefaultStatusToggle="//input[@name='ndefaultstatus' and @type='checkbox']"

designationTotalCount="//div[@class='k-pager-info k-label']"

designationScreenHeader="//*[@class='navbar-brand']/h2"

designationAddPopupHeader="//div[@class='header-primary flex-grow-1 modal-title h4' and @id='add-user']"

module="Master"

subModule="Base Master"

screen="designation"

def elementDesignation():

    designation={}

    designation.update({ObjectName.moduleIcon:masterIcon})

    designation.update({ObjectName.subModuleIcon:userManagementIcon})

    designation.update({ObjectName.screenIcon:designationIcon})

    designation.update({ObjectName.add:designationAdd})

    designation.update({ObjectName.name: designationName})

    designation.update({ObjectName.description:designationDescription})

    designation.update({ObjectName.addSubmit:designationAddSubmit})

    designation.update({ObjectName.addCancel:designationAddCancel})

    designation.update({ObjectName.screenHeader:designationScreenHeader})

    designation.update({ObjectName.module:module})

    designation.update({ObjectName.subModule:subModule})

    designation.update({ObjectName.screen:screen})

    designation.update({ObjectName.addPopupHeader:designationAddPopupHeader})

    designation.update({ObjectName.totalCount:designationTotalCount})

    designation.update({ObjectName.defaultStatusLabel:designationDefaultStatusLabel})

    designation.update({ObjectName.defaultStatusToggle:designationDefaultStatusToggle})

    return designation



