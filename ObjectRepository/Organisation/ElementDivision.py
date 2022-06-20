########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 20th June 2022, ID - #46 ||
########################################################################################################################################################################################################################################################################################################################################################

from Setting import ObjectName

pin = "//a[@class='text-center nav-link']"

masterIcon="//a[@data-rb-event-key='MenuId_1']"

userManagementIcon="//span[text()='Organisation']"

divisionIcon="//a[@href='#/department']"

divisionAdd="//button[@data-tip='Add']"

divisionRefresh="//button[@data-tip='Refresh']"

divisionDownloadPDF="//button[@data-tip='Download PDF']"

divisionDownloadExcel="//button[@data-tip='Download Excel']"

divisionName="//input[@id='sdeptname'][@name='sdeptname']"

divisionDescription="//textarea[@id='sdescription'][@name='sdescription']"

divisionAddSubmit="//button[text()='Save']"

divisionAddCancel="//button[text()='Cancel']"

divisionEditSubmit="//button[text()='Save']"

divisionEditCancel="//button[text()='Cancel']"

divisionNameList="/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td[1]"

divisionDescriptionList="//tbody[@role='presentation']/tr/td[2]"

divisionDefaultStatusList="//tbody[@role='presentation']/tr/td[3]"

divisionEditList="//tbody[@role='presentation']/tr/td[4]/a/span[1]"

divisionDeleteList="//tbody[@role='presentation']/tr/td[4]/a/span[2]"

divisionNameFilter="(//span[@class='k-icon k-i-more-vertical'])[1]"

divisionDefaultStatusLabel="//label[@for='ndefaultstatus']"

divisionDefaultStatusToggle="//input[@name='ndefaultstatus' and @type='checkbox']"

divisionTotalCount="//div[@class='k-pager-info k-label']"

divisionScreenHeader="//*[@class='navbar-brand']/h2"

divisionAddPopupHeader="//div[@class='header-primary flex-grow-1 modal-title h4' and @id='add-user']"

module="Master"

subModule="Base Master"

screen="division"

def elementDivision():

    division={}

    division.update({ObjectName.moduleIcon:masterIcon})

    division.update({ObjectName.subModuleIcon:userManagementIcon})

    division.update({ObjectName.screenIcon:divisionIcon})

    division.update({ObjectName.add:divisionAdd})

    division.update({ObjectName.name: divisionName})

    division.update({ObjectName.description:divisionDescription})

    division.update({ObjectName.addSubmit:divisionAddSubmit})

    division.update({ObjectName.addCancel:divisionAddCancel})

    division.update({ObjectName.screenHeader:divisionScreenHeader})

    division.update({ObjectName.module:module})

    division.update({ObjectName.subModule:subModule})

    division.update({ObjectName.screen:screen})

    division.update({ObjectName.addPopupHeader:divisionAddPopupHeader})

    division.update({ObjectName.totalCount:divisionTotalCount})

    division.update({ObjectName.defaultStatusLabel:divisionDefaultStatusLabel})

    division.update({ObjectName.defaultStatusToggle:divisionDefaultStatusToggle})

    return division



