########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 20th June 2022, ID - #54 ||
########################################################################################################################################################################################################################################################################################################################################################

from Setting import ObjectName

pin = "//a[@class='text-center nav-link']"

masterIcon="//a[@data-rb-event-key='MenuId_1']"

baseMasterIcon="//span[text()='Base Master']"

storageLocationIcon="//a[@href='#/storageLocation']"

storageLocationAdd="//button[@data-tip='Add']"

storageLocationRefresh="//button[@data-tip='Refresh']"

storageLocationDownloadPDF="//button[@data-tip='Download PDF']"

storageLocationDownloadExcel="//button[@data-tip='Download Excel']"

storageLocationName="//input[@id='sstoragelocationname'][@name='sstoragelocationname']"

storageLocationDescription="//textarea[@id='sdescription'][@name='sdescription']"

storageLocationAddSubmit="//button[text()='Save']"

storageLocationAddCancel="//button[text()='Cancel']"

storageLocationEditSubmit="//button[text()='Save']"

storageLocationEditCancel="//button[text()='Cancel']"

storageLocationNameList="/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td[1]"

storageLocationDescriptionList="//tbody[@role='presentation']/tr/td[2]"

storageLocationDefaultStatusList="//tbody[@role='presentation']/tr/td[3]"

storageLocationEditList="//tbody[@role='presentation']/tr/td[4]/a/span[1]"

storageLocationDeleteList="//tbody[@role='presentation']/tr/td[4]/a/span[2]"

storageLocationNameFilter="(//span[@class='k-icon k-i-more-vertical'])[1]"

storageLocationDefaultStatusLabel="//label[@for='ndefaultstatus']"

storageLocationDefaultStatusToggle="//input[@name='ndefaultstatus' and @type='checkbox']"

storageLocationTotalCount="//div[@class='k-pager-info k-label']"

storageLocationScreenHeader="//*[@class='navbar-brand']/h2"

storageLocationAddPopupHeader="//div[@class='header-primary flex-grow-1 modal-title h4' and @id='add-user']"

module="Master"

subModule="Base Master"

screen="Storage Location"

def elementStorageLocation():

    storageLocation={}

    storageLocation.update({ObjectName.moduleIcon:masterIcon})

    storageLocation.update({ObjectName.subModuleIcon:baseMasterIcon})

    storageLocation.update({ObjectName.screenIcon:storageLocationIcon})

    storageLocation.update({ObjectName.add:storageLocationAdd})

    storageLocation.update({ObjectName.name: storageLocationName})

    storageLocation.update({ObjectName.description:storageLocationDescription})

    storageLocation.update({ObjectName.addSubmit:storageLocationAddSubmit})

    storageLocation.update({ObjectName.addCancel:storageLocationAddCancel})

    storageLocation.update({ObjectName.screenHeader:storageLocationScreenHeader})

    storageLocation.update({ObjectName.module:module})

    storageLocation.update({ObjectName.subModule:subModule})

    storageLocation.update({ObjectName.screen:screen})

    storageLocation.update({ObjectName.addPopupHeader:storageLocationAddPopupHeader})

    storageLocation.update({ObjectName.totalCount:storageLocationTotalCount})

    storageLocation.update({ObjectName.defaultStatusLabel:storageLocationDefaultStatusLabel})

    storageLocation.update({ObjectName.defaultStatusToggle:storageLocationDefaultStatusToggle})

    return storageLocation



