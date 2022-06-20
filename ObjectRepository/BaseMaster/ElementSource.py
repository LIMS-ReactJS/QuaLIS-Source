########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 20th June 2022, ID - #45 ||
########################################################################################################################################################################################################################################################################################################################################################


from Setting import ObjectName

pin = "//a[@class='text-center nav-link']"

masterIcon="//a[@data-rb-event-key='MenuId_1']"

baseMasterIcon="//span[text()='Base Master']"

sourceIcon="//a[@href='#/source']"

sourceAdd="//button[@data-tip='Add']"

sourceRefresh="//button[@data-tip='Refresh']"

sourceDownloadPDF="//button[@data-tip='Download PDF']"

sourceDownloadExcel="//button[@data-tip='Download Excel']"

sourceName="//input[@id='ssourcename'][@name='ssourcename']"

sourceDescription="//textarea[@id='sdescription'][@name='sdescription']"

sourceAddSubmit="//button[text()='Save']"

sourceAddCancel="//button[text()='Cancel']"

sourceEditSubmit="//button[text()='Save']"

sourceEditCancel="//button[text()='Cancel']"

sourceNameList="/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td[1]"

sourceDescriptionList="//tbody[@role='presentation']/tr/td[2]"

sourceDefaultStatusList="//tbody[@role='presentation']/tr/td[3]"

sourceEditList="//tbody[@role='presentation']/tr/td[4]/a/span[1]"

sourceDeleteList="//tbody[@role='presentation']/tr/td[4]/a/span[2]"

sourceNameFilter="(//span[@class='k-icon k-i-more-vertical'])[1]"

sourceDefaultStatusLabel="//label[@for='ndefaultstatus']"

sourceDefaultStatusToggle="//input[@name='ndefaultstatus' and @type='checkbox']"

sourceTotalCount="//div[@class='k-pager-info k-label']"

sourceScreenHeader="//*[@class='navbar-brand']/h2"

sourceAddPopupHeader="//div[@class='header-primary flex-grow-1 modal-title h4' and @id='add-user']"

module="Master"

subModule="Base Master"

screen="source"

def elementSource():

    source={}

    source.update({ObjectName.moduleIcon:masterIcon})

    source.update({ObjectName.subModuleIcon:baseMasterIcon})

    source.update({ObjectName.screenIcon:sourceIcon})

    source.update({ObjectName.add:sourceAdd})

    source.update({ObjectName.name: sourceName})

    source.update({ObjectName.description:sourceDescription})

    source.update({ObjectName.addSubmit:sourceAddSubmit})

    source.update({ObjectName.addCancel:sourceAddCancel})

    source.update({ObjectName.screenHeader:sourceScreenHeader})

    source.update({ObjectName.module:module})

    source.update({ObjectName.subModule:subModule})

    source.update({ObjectName.screen:screen})

    source.update({ObjectName.addPopupHeader:sourceAddPopupHeader})

    source.update({ObjectName.totalCount:sourceTotalCount})

    source.update({ObjectName.defaultStatusLabel:sourceDefaultStatusLabel})

    source.update({ObjectName.defaultStatusToggle:sourceDefaultStatusToggle})

    return source



