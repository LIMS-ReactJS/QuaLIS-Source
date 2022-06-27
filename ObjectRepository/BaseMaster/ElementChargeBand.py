########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 27th June 2022, ID - #70 ||
########################################################################################################################################################################################################################################################################################################################################################


from Setting import ObjectName

pin = "//a[@class='text-center nav-link']"

masterIcon="//a[@data-rb-event-key='MenuId_1']"

baseMasterIcon="//span[text()='Base Master']"

chargeBandIcon="//a[@href='#/chargeBand'][@nformcode='44']"

chargeBandAdd="//button[@data-tip='Add']"

chargeBandRefresh="//button[@data-tip='Refresh']"

chargeBandDownloadPDF="//button[@data-tip='Download PDF']"

chargeBandDownloadExcel="//button[@data-tip='Download Excel']"

chargeBandName="//input[@id='schargebandname'][@name='schargebandname']"

chargeBandDescription="//*[@id='sdescription'][@name='sdescription']"

chargeBandPrice="//*[@id='nprice']"

chargeBandAddSubmit="//button[text()='Save']"

chargeBandAddCancel="//button[text()='Cancel']"

chargeBandEditSubmit="//button[text()='Save']"

chargeBandEditCancel="//button[text()='Cancel']"

chargeBandNameList="/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td[1]"

chargeBandDescriptionList="//tbody[@role='presentation']/tr/td[2]"

chargeBandDefaultStatusList="//tbody[@role='presentation']/tr/td[3]"

chargeBandEditList="//tbody[@role='presentation']/tr/td[4]/a/span[1]"

chargeBandDeleteList="//tbody[@role='presentation']/tr/td[4]/a/span[2]"

chargeBandNameFilter="(//span[@class='k-icon k-i-more-vertical'])[1]"

chargeBandDefaultStatusLabel="//label[@for='ndefaultstatus']"

chargeBandDefaultStatusToggle="//input[@name='ndefaultstatus' and @type='checkbox']"

chargeBandTotalCount="//div[@class='k-pager-info k-label']"

chargeBandScreenHeader="//*[@class='navbar-brand']/h2"

chargeBandAddPopupHeader="//div[@class='header-primary flex-grow-1 modal-title h4' and @id='add-user']"

module="Master"

subModule="Base Master"

screen="Charge Band"

def elementchargeBand():

    chargeBand={}

    chargeBand.update({ObjectName.moduleIcon:masterIcon})

    chargeBand.update({ObjectName.subModuleIcon:baseMasterIcon})

    chargeBand.update({ObjectName.screenIcon:chargeBandIcon})

    chargeBand.update({ObjectName.add:chargeBandAdd})

    chargeBand.update({ObjectName.name: chargeBandName})

    chargeBand.update({ObjectName.description:chargeBandDescription})

    chargeBand.update({ObjectName.addSubmit:chargeBandAddSubmit})

    chargeBand.update({ObjectName.addCancel:chargeBandAddCancel})

    chargeBand.update({ObjectName.screenHeader:chargeBandScreenHeader})

    chargeBand.update({ObjectName.module:module})

    chargeBand.update({ObjectName.subModule:subModule})

    chargeBand.update({ObjectName.screen:screen})

    chargeBand.update({ObjectName.addPopupHeader:chargeBandAddPopupHeader})

    chargeBand.update({ObjectName.totalCount:chargeBandTotalCount})

    chargeBand.update({ObjectName.defaultStatusLabel:chargeBandDefaultStatusLabel})

    chargeBand.update({ObjectName.defaultStatusToggle:chargeBandDefaultStatusToggle})

    return chargeBand



