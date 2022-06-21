########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 21st June 2022, ID - #56 ||
########################################################################################################################################################################################################################################################################################################################################################

from Setting import ObjectName

pin = "//a[@class='text-center nav-link']"

masterIcon="//a[@data-rb-event-key='MenuId_1']"

userManagementIcon="//span[text()='User Management']"

userRoleIcon="//a[@href='#/userRole']"

userRoleAdd="//button[@data-tip='Add']"

userRoleRefresh="//button[@data-tip='Refresh']"

userRoleDownloadPDF="//button[@data-tip='Download PDF']"

userRoleDownloadExcel="//button[@data-tip='Download Excel']"

userRoleName="//input[@id='slabname'][@name='slabname']"

userRoleDescription="//textarea[@id='sdescription'][@name='sdescription']"

userRoleAddSubmit="//button[text()='Save']"

userRoleAddCancel="//button[text()='Cancel']"

userRoleEditSubmit="//button[text()='Save']"

userRoleEditCancel="//button[text()='Cancel']"

userRoleNameList="/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td[1]"

userRoleDescriptionList="//tbody[@role='presentation']/tr/td[2]"

userRoleDefaultStatusList="//tbody[@role='presentation']/tr/td[3]"

userRoleEditList="//tbody[@role='presentation']/tr/td[4]/a/span[1]"

userRoleDeleteList="//tbody[@role='presentation']/tr/td[4]/a/span[2]"

userRoleNameFilter="(//span[@class='k-icon k-i-more-vertical'])[1]"

userRoleDefaultStatususerRoleel="//userRoleel[@for='ndefaultstatus']"

userRoleDefaultStatusToggle="//input[@name='ndefaultstatus' and @type='checkbox']"

userRoleTotalCount="//div[@class='k-pager-info k-userRoleel']"

userRoleScreenHeader="//*[@class='navbar-brand']/h2"

userRoleAddPopupHeader="//div[@class='header-primary flex-grow-1 modal-title h4' and @id='add-user']"

module="Master"

subModule="Organisation"

screen="userRole"

def elementuserRole():

    userRole={}

    userRole.update({ObjectName.moduleIcon:masterIcon})

    userRole.update({ObjectName.subModuleIcon:organisationManagemenIcon})

    userRole.update({ObjectName.screenIcon:userRoleIcon})

    userRole.update({ObjectName.add:userRoleAdd})

    userRole.update({ObjectName.name: userRoleName})

    userRole.update({ObjectName.description:userRoleDescription})

    userRole.update({ObjectName.addSubmit:userRoleAddSubmit})

    userRole.update({ObjectName.addCancel:userRoleAddCancel})

    userRole.update({ObjectName.screenHeader:userRoleScreenHeader})

    userRole.update({ObjectName.module:module})

    userRole.update({ObjectName.subModule:subModule})

    userRole.update({ObjectName.screen:screen})

    userRole.update({ObjectName.addPopupHeader:userRoleAddPopupHeader})

    userRole.update({ObjectName.totalCount:userRoleTotalCount})

    userRole.update({ObjectName.defaultStatususerRoleel:userRoleDefaultStatususerRoleel})

    userRole.update({ObjectName.defaultStatusToggle:userRoleDefaultStatusToggle})

    return userRole



