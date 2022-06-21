########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 21st June 2022, ID - #61 ||
########################################################################################################################################################################################################################################################################################################################################################


from Setting import ObjectName

pin = "//a[@class='text-center nav-link']"

masterIcon="//a[@data-rb-event-key='MenuId_1']"

competenceManagementIcon="//span[text()='Competence Management']"

techniqueIcon="//a[@href='#/technique']"

techniqueAdd="//button[@data-tip='Add']"

techniqueRefresh="//button[@data-tip='Refresh']"

techniqueDownloadPDF="//button[@data-tip='Download PDF']"

techniqueDownloadExcel="//button[@data-tip='Download Excel']"

techniqueName="//input[@id='stechniquename'][@name='stechniquename']"

techniqueDescription="//textarea[@id='sdescription'][@name='sdescription']"

techniqueAddSubmit="//button[text()='Save']"

techniqueAddCancel="//button[text()='Cancel']"

techniqueEditSubmit="//button[text()='Save']"

techniqueEditCancel="//button[text()='Cancel']"

techniqueNameList="/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td[1]"

techniqueDescriptionList="//tbody[@role='presentation']/tr/td[2]"

techniqueDefaultStatusList="//tbody[@role='presentation']/tr/td[3]"

techniqueEditList="//tbody[@role='presentation']/tr/td[4]/a/span[1]"

techniqueDeleteList="//tbody[@role='presentation']/tr/td[4]/a/span[2]"

techniqueNameFilter="(//span[@class='k-icon k-i-more-vertical'])[1]"

techniqueDefaultStatusLabel="//label[@for='ndefaultstatus']"

techniqueDefaultStatusToggle="//input[@name='ndefaultstatus' and @type='checkbox']"

techniqueTotalCount="//div[@class='k-pager-info k-label']"

techniqueScreenHeader="//*[@class='navbar-brand']/h2"

techniqueAddPopupHeader="//div[@class='header-primary flex-grow-1 modal-title h4' and @id='add-user']"

module="Master"

subModule="Base Master"

screen="technique"

def elementTechnique():

    technique={}

    technique.update({ObjectName.moduleIcon:masterIcon})

    technique.update({ObjectName.subModuleIcon:competenceManagementIcon})

    technique.update({ObjectName.screenIcon:techniqueIcon})

    technique.update({ObjectName.add:techniqueAdd})

    technique.update({ObjectName.name: techniqueName})

    technique.update({ObjectName.description:techniqueDescription})

    technique.update({ObjectName.addSubmit:techniqueAddSubmit})

    technique.update({ObjectName.addCancel:techniqueAddCancel})

    technique.update({ObjectName.screenHeader:techniqueScreenHeader})

    technique.update({ObjectName.module:module})

    technique.update({ObjectName.subModule:subModule})

    technique.update({ObjectName.screen:screen})

    technique.update({ObjectName.addPopupHeader:techniqueAddPopupHeader})

    technique.update({ObjectName.totalCount:techniqueTotalCount})

    technique.update({ObjectName.defaultStatusLabel:techniqueDefaultStatusLabel})

    technique.update({ObjectName.defaultStatusToggle:techniqueDefaultStatusToggle})

    return technique



