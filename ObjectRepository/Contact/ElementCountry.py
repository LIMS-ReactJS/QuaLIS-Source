########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 24th June 2022, ID - #65 ||
########################################################################################################################################################################################################################################################################################################################################################

from Setting import ObjectName

pin = "//a[@class='text-center nav-link']"

masterIcon="//a[@data-rb-event-key='MenuId_1']"

contactsIcon="//*[text()='Contacts']"

countryIcon="//a[@href='#/country'][@nformcode='5']"

countryAdd="//button[@data-tip='Add']"

countryRefresh="//button[@data-tip='Refresh']"

countryDownloadPDF="//button[@data-tip='Download PDF']"

countryDownloadExcel="//button[@data-tip='Download Excel']"

countryName="//input[@id='scountryname'][@name='scountryname']"

countryShortName="//input[@id='scountryshortname'][@name='scountryshortname']"\

countryTwoChar="//input[@id='stwocharcountry'][@name='stwocharcountry']"

countryThreeChar="//input[@id='sthreecharcountry'][@name='sthreecharcountry']"

countryAddSubmit="//button[text()='Save']"

countryAddCancel="//button[text()='Cancel']"

countryEditSubmit="//button[text()='Save']"

countryEditCancel="//button[text()='Cancel']"

countryNameList="/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td[1]"

countryDescriptionList="//tbody[@role='presentation']/tr/td[2]"

countryEditList="//tbody[@role='presentation']/tr/td[4]/a/span[1]"

countryDeleteList="//tbody[@role='presentation']/tr/td[4]/a/span[2]"

countryNameFilter="(//span[@class='k-icon k-i-more-vertical'])[1]"

countryDefaultStatusLabel="//label[@for='ndefaultstatus']"

countryDefaultStatusToggle="//input[@name='ndefaultstatus' and @type='checkbox']"

countryTotalCount="//div[@class='k-pager-info k-label']"

countryScreenHeader="//*[@class='navbar-brand']/h2"

countryAddPopupHeader="//div[@class='header-primary flex-grow-1 modal-title h4' and @id='add-user']"

module="Master"

subModule="Contacts"

screen="Country"

def elementcountry():

    country={}

    country.update({ObjectName.moduleIcon:masterIcon})

    country.update({ObjectName.subModuleIcon:baseMasterIcon})

    country.update({ObjectName.screenIcon:countryIcon})

    country.update({ObjectName.add:countryAdd})

    country.update({ObjectName.name: countryName})

    country.update({ObjectName.description:countryDescription})

    country.update({ObjectName.addSubmit:countryAddSubmit})

    country.update({ObjectName.addCancel:countryAddCancel})

    country.update({ObjectName.screenHeader:countryScreenHeader})

    country.update({ObjectName.module:module})

    country.update({ObjectName.subModule:subModule})

    country.update({ObjectName.screen:screen})

    country.update({ObjectName.addPopupHeader:countryAddPopupHeader})

    country.update({ObjectName.totalCount:countryTotalCount})

    country.update({ObjectName.defaultStatusLabel:countryDefaultStatusLabel})

    country.update({ObjectName.defaultStatusToggle:countryDefaultStatusToggle})

    return country



