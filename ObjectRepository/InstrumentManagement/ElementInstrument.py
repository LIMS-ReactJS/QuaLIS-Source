########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 27th June 2022, ID - #73 ||
########################################################################################################################################################################################################################################################################################################################################################


from Setting import ObjectName

pin = "//a[@class='text-center nav-link']"

masterIcon="//a[@data-rb-event-key='MenuId_1']"

instrumentManagementIcon="//span[text()='Instrument Management']"

instrumentIcon="//a[@href='#/instrument'][@nformcode='28']"

instrumentCategoryFilterIcon="//*[@data-tip='Click to show filter']"

instrumentCategoryFilterName="//*[@id='ninstrumentcatcode']"

instrumentCategoryFilterSubmit="//*[text()='Submit']"

instrumentCategoryFilterCancel="//*[text()='Cancel']"

instrumentAdd="//button[@data-tip='Add']"

instrumentRefresh="//button[@data-tip='Refresh']"

instrumentDownloadPDF="//button[@data-tip='Download PDF']"

instrumentDownloadExcel="//button[@data-tip='Download Excel']"

instrumentCategoryName="//*[@id='ninstrumentcatcode']"

instrumentID="//input[@id='sinstrumentid'][@name='sinstrumentid']"

instrumentName="//input[@id='sinstrumentname'][@name='sinstrumentname']"

instrumentSupplier="//*[@id='nsuppliercode']"

instrumentSerialNumber="//*[@id='sserialno']"

instrumentManufacturerDate="//input[@name='dmanufacdate']"

instrumentPODate="//input[@name='dpodate']"

instrumentReceivedDate="//*[@name='dreceiveddate']"

instrumentInstallationDate="//*[@name='dinstallationdate']"

instrumentExpireDate="//*[@name='dexpirydate']"

instrumentAddSubmit="//button[text()='Save']"

instrumentAddCancel="//button[text()='Cancel']"

instrumentEditSubmit="//button[text()='Save']"

instrumentEditCancel="//button[text()='Cancel']"

instrumentNameList="/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td[1]"

instrumentDescriptionList="//tbody[@role='presentation']/tr/td[2]"

instrumentDefaultStatusList="//tbody[@role='presentation']/tr/td[3]"

instrumentEditList="//tbody[@role='presentation']/tr/td[4]/a/span[1]"

instrumentDeleteList="//tbody[@role='presentation']/tr/td[4]/a/span[2]"

instrumentNameFilter="(//span[@class='k-icon k-i-more-vertical'])[1]"

instrumentDefaultStatusLabel="//label[@for='ndefaultstatus']"

instrumentDefaultStatusToggle="//input[@name='ndefaultstatus' and @type='checkbox']"

instrumentTotalCount="//div[@class='k-pager-info k-label']"

instrumentScreenHeader="//*[@class='navbar-brand']/h2"

instrumentAddPopupHeader="//div[@class='header-primary flex-grow-1 modal-title h4' and @id='add-user']"

module="Master"

subModule="Instrument Management"

screen="Instrument"

def elementinstrument():

    instrument={}

    instrument.update({ObjectName.moduleIcon:masterIcon})

    instrument.update({ObjectName.subModuleIcon:instrumentManagementIcon})

    instrument.update({ObjectName.screenIcon:instrumentIcon})

    instrument.update({ObjectName.add:instrumentAdd})

    instrument.update({ObjectName.name: instrumentName})

    instrument.update({ObjectName.addSubmit:instrumentAddSubmit})

    instrument.update({ObjectName.addCancel:instrumentAddCancel})

    instrument.update({ObjectName.screenHeader:instrumentScreenHeader})

    instrument.update({ObjectName.module:module})

    instrument.update({ObjectName.subModule:subModule})

    instrument.update({ObjectName.screen:screen})

    instrument.update({ObjectName.addPopupHeader:instrumentAddPopupHeader})

    instrument.update({ObjectName.totalCount:instrumentTotalCount})

    instrument.update({ObjectName.defaultStatusLabel:instrumentDefaultStatusLabel})

    instrument.update({ObjectName.defaultStatusToggle:instrumentDefaultStatusToggle})

    return instrument



