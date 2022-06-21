########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 21st June 2022, ID - #57 ||
########################################################################################################################################################################################################################################################################################################################################################

from Setting import ObjectName

pin = "//a[@class='text-center nav-link']"

masterIcon="//a[@data-rb-event-key='MenuId_1']"

organisationManagemenIcon="//span[text()='Organisation']"

sectionIcon="//a[@href='#/lab']"

sectionAdd="//button[@data-tip='Add']"

sectionRefresh="//button[@data-tip='Refresh']"

sectionDownloadPDF="//button[@data-tip='Download PDF']"

sectionDownloadExcel="//button[@data-tip='Download Excel']"

sectionName="//input[@id='slabname'][@name='slabname']"

sectionDescription="//textarea[@id='sdescription'][@name='sdescription']"

sectionAddSubmit="//button[text()='Save']"

sectionAddCancel="//button[text()='Cancel']"

sectionEditSubmit="//button[text()='Save']"

sectionEditCancel="//button[text()='Cancel']"

sectionNameList="/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td[1]"

sectionDescriptionList="//tbody[@role='presentation']/tr/td[2]"

sectionDefaultStatusList="//tbody[@role='presentation']/tr/td[3]"

sectionEditList="//tbody[@role='presentation']/tr/td[4]/a/span[1]"

sectionDeleteList="//tbody[@role='presentation']/tr/td[4]/a/span[2]"

sectionNameFilter="(//span[@class='k-icon k-i-more-vertical'])[1]"

sectionDefaultStatussectionel="//sectionel[@for='ndefaultstatus']"

sectionDefaultStatusToggle="//input[@name='ndefaultstatus' and @type='checkbox']"

sectionTotalCount="//div[@class='k-pager-info k-sectionel']"

sectionScreenHeader="//*[@class='navbar-brand']/h2"

sectionAddPopupHeader="//div[@class='header-primary flex-grow-1 modal-title h4' and @id='add-user']"

module="Master"

subModule="Organisation"

screen="section"

def elementsection():

    section={}

    section.update({ObjectName.moduleIcon:masterIcon})

    section.update({ObjectName.subModuleIcon:organisationManagemenIcon})

    section.update({ObjectName.screenIcon:sectionIcon})

    section.update({ObjectName.add:sectionAdd})

    section.update({ObjectName.name: sectionName})

    section.update({ObjectName.description:sectionDescription})

    section.update({ObjectName.addSubmit:sectionAddSubmit})

    section.update({ObjectName.addCancel:sectionAddCancel})

    section.update({ObjectName.screenHeader:sectionScreenHeader})

    section.update({ObjectName.module:module})

    section.update({ObjectName.subModule:subModule})

    section.update({ObjectName.screen:screen})

    section.update({ObjectName.addPopupHeader:sectionAddPopupHeader})

    section.update({ObjectName.totalCount:sectionTotalCount})

    section.update({ObjectName.defaultStatussectionel:sectionDefaultStatussectionel})

    section.update({ObjectName.defaultStatusToggle:sectionDefaultStatusToggle})

    return section



