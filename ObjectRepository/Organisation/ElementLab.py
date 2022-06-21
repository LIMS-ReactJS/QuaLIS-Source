########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 20th June 2022, ID - #46 ||
########################################################################################################################################################################################################################################################################################################################################################

from Setting import ObjectName

pin = "//a[@class='text-center nav-link']"

masterIcon="//a[@data-rb-event-key='MenuId_1']"

organisationManagemenIcon="//span[text()='Organisation']"

labIcon="//a[@href='#/section']"

labAdd="//button[@data-tip='Add']"

labRefresh="//button[@data-tip='Refresh']"

labDownloadPDF="//button[@data-tip='Download PDF']"

labDownloadExcel="//button[@data-tip='Download Excel']"

labName="//input[@id='ssectionname'][@name='ssectionname']"

labDescription="//textarea[@id='sdescription'][@name='sdescription']"

labAddSubmit="//button[text()='Save']"

labAddCancel="//button[text()='Cancel']"

labEditSubmit="//button[text()='Save']"

labEditCancel="//button[text()='Cancel']"

labNameList="/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td[1]"

labDescriptionList="//tbody[@role='presentation']/tr/td[2]"

labDefaultStatusList="//tbody[@role='presentation']/tr/td[3]"

labEditList="//tbody[@role='presentation']/tr/td[4]/a/span[1]"

labDeleteList="//tbody[@role='presentation']/tr/td[4]/a/span[2]"

labNameFilter="(//span[@class='k-icon k-i-more-vertical'])[1]"

labDefaultStatusLabel="//label[@for='ndefaultstatus']"

labDefaultStatusToggle="//input[@name='ndefaultstatus' and @type='checkbox']"

labTotalCount="//div[@class='k-pager-info k-label']"

labScreenHeader="//*[@class='navbar-brand']/h2"

labAddPopupHeader="//div[@class='header-primary flex-grow-1 modal-title h4' and @id='add-user']"

module="Master"

subModule="Base Master"

screen="Lab"

def elementLab():

    lab={}

    lab.update({ObjectName.moduleIcon:masterIcon})

    lab.update({ObjectName.subModuleIcon:organisationManagemenIcon})

    lab.update({ObjectName.screenIcon:labIcon})

    lab.update({ObjectName.add:labAdd})

    lab.update({ObjectName.name: labName})

    lab.update({ObjectName.description:labDescription})

    lab.update({ObjectName.addSubmit:labAddSubmit})

    lab.update({ObjectName.addCancel:labAddCancel})

    lab.update({ObjectName.screenHeader:labScreenHeader})

    lab.update({ObjectName.module:module})

    lab.update({ObjectName.subModule:subModule})

    lab.update({ObjectName.screen:screen})

    lab.update({ObjectName.addPopupHeader:labAddPopupHeader})

    lab.update({ObjectName.totalCount:labTotalCount})

    lab.update({ObjectName.defaultStatusLabel:labDefaultStatusLabel})

    lab.update({ObjectName.defaultStatusToggle:labDefaultStatusToggle})

    return lab



