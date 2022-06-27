########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 21st June 2022, ID - #55 ||
########################################################################################################################################################################################################################################################################################################################################################


from Setting import ObjectName

pin = "//a[@class='text-center nav-link']"

masterIcon="//a[@data-rb-event-key='MenuId_1']"

baseMasterIcon="//span[text()='Base Master']"

licenseAuthorityIcon="//a[@href='#/licenseAuthority'][@nformcode='37']"

licenseAuthorityAdd="//button[@data-tip='Add']"

licenseAuthorityRefresh="//button[@data-tip='Refresh']"

licenseAuthorityDownloadPDF="//button[@data-tip='Download PDF']"

licenseAuthorityDownloadExcel="//button[@data-tip='Download Excel']"

licenseAuthorityName="//input[@id='sauthorityname'][@name='sauthorityname']"

licenseAuthorityShortName="//*[@id='sauthorityshortname'][@name='sauthorityshortname']"

licenseAuthorityCountry="//*[@id='ncountrycode']"

licenseAuthorityCountryShortName="//*[@id='scountryshortname'][@name='scountryshortname']"

licenseAuthorityAddSubmit="//button[text()='Save']"

licenseAuthorityAddCancel="//button[text()='Cancel']"

licenseAuthorityEditSubmit="//button[text()='Save']"

licenseAuthorityEditCancel="//button[text()='Cancel']"

licenseAuthorityNameList="/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td[1]"

licenseAuthorityDescriptionList="//tbody[@role='presentation']/tr/td[2]"

licenseAuthorityDefaultStatusList="//tbody[@role='presentation']/tr/td[3]"

licenseAuthorityEditList="//tbody[@role='presentation']/tr/td[4]/a/span[1]"

licenseAuthorityDeleteList="//tbody[@role='presentation']/tr/td[4]/a/span[2]"

licenseAuthorityNameFilter="(//span[@class='k-icon k-i-more-vertical'])[1]"

licenseAuthorityDefaultStatusLabel="//label[@for='ndefaultstatus']"

licenseAuthorityDefaultStatusToggle="//input[@name='ndefaultstatus' and @type='checkbox']"

licenseAuthorityTotalCount="//div[@class='k-pager-info k-label']"

licenseAuthorityScreenHeader="//*[@class='navbar-brand']/h2"

licenseAuthorityAddPopupHeader="//div[@class='header-primary flex-grow-1 modal-title h4' and @id='add-user']"

module="Master"

subModule="Base Master"

screen="Container Type"

def elementlicenseAuthority():

    licenseAuthority={}

    licenseAuthority.update({ObjectName.moduleIcon:masterIcon})

    licenseAuthority.update({ObjectName.subModuleIcon:baseMasterIcon})

    licenseAuthority.update({ObjectName.screenIcon:licenseAuthorityIcon})

    licenseAuthority.update({ObjectName.add:licenseAuthorityAdd})

    licenseAuthority.update({ObjectName.name: licenseAuthorityName})

    licenseAuthority.update({ObjectName.description:licenseAuthorityDescription})

    licenseAuthority.update({ObjectName.addSubmit:licenseAuthorityAddSubmit})

    licenseAuthority.update({ObjectName.addCancel:licenseAuthorityAddCancel})

    licenseAuthority.update({ObjectName.screenHeader:licenseAuthorityScreenHeader})

    licenseAuthority.update({ObjectName.module:module})

    licenseAuthority.update({ObjectName.subModule:subModule})

    licenseAuthority.update({ObjectName.screen:screen})

    licenseAuthority.update({ObjectName.addPopupHeader:licenseAuthorityAddPopupHeader})

    licenseAuthority.update({ObjectName.totalCount:licenseAuthorityTotalCount})

    licenseAuthority.update({ObjectName.defaultStatusLabel:licenseAuthorityDefaultStatusLabel})

    licenseAuthority.update({ObjectName.defaultStatusToggle:licenseAuthorityDefaultStatusToggle})

    return licenseAuthority



