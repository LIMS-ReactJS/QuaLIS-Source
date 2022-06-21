########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 20th June 2022, ID - #46 ||
########################################################################################################################################################################################################################################################################################################################################################

from Setting import ObjectName

pin = "//a[@class='text-center nav-link']"

masterIcon="//a[@data-rb-event-key='MenuId_1']"

productManagementIcon="//span[text()='Product']"

productCategoryIcon="//a[@href='#/productCategory']"

productCategoryAdd="//button[@data-tip='Add']"

productCategoryRefresh="//button[@data-tip='Refresh']"

productCategoryDownloadPDF="//button[@data-tip='Download PDF']"

productCategoryDownloadExcel="//button[@data-tip='Download Excel']"

productCategoryName="//input[@id='sproductcatname'][@name='sproductcatname']"

productCategoryDescription="//textarea[@id='sdescription'][@name='sdescription']"

productCategoryAddSubmit="//button[text()='Save']"

productCategoryAddCancel="//button[text()='Cancel']"

productCategoryEditSubmit="//button[text()='Save']"

productCategoryEditCancel="//button[text()='Cancel']"

productCategoryNameList="/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[3]/div/div[1]/table/tbody/tr/td[1]"

productCategoryDescriptionList="//tbody[@role='presentation']/tr/td[2]"

productCategoryDefaultStatusList="//tbody[@role='presentation']/tr/td[3]"

productCategoryEditList="//tbody[@role='presentation']/tr/td[4]/a/span[1]"

productCategoryDeleteList="//tbody[@role='presentation']/tr/td[4]/a/span[2]"

productCategoryNameFilter="(//span[@class='k-icon k-i-more-vertical'])[1]"

productCategoryDefaultStatusLabel="//*[@for='ndefaultstatus']"

productCategoryDefaultStatusToggle="//input[@name='ndefaultstatus' and @type='checkbox']"

productCategoryTotalCount="//div[@class='k-pager-info k-productCategoryel']"

productCategoryScreenHeader="//*[@class='navbar-brand']/h2"

productCategoryAddPopupHeader="//div[@class='header-primary flex-grow-1 modal-title h4' and @id='add-user']"

module="Master"

subModule="Product Management"

screen="Product Category"

def elementProductCategory():

    productCategory={}

    productCategory.update({ObjectName.moduleIcon:masterIcon})

    productCategory.update({ObjectName.subModuleIcon:productManagementIcon})

    productCategory.update({ObjectName.screenIcon:productCategoryIcon})

    productCategory.update({ObjectName.add:productCategoryAdd})

    productCategory.update({ObjectName.name: productCategoryName})

    productCategory.update({ObjectName.description:productCategoryDescription})

    productCategory.update({ObjectName.addSubmit:productCategoryAddSubmit})

    productCategory.update({ObjectName.addCancel:productCategoryAddCancel})

    productCategory.update({ObjectName.screenHeader:productCategoryScreenHeader})

    productCategory.update({ObjectName.module:module})

    productCategory.update({ObjectName.subModule:subModule})

    productCategory.update({ObjectName.screen:screen})

    productCategory.update({ObjectName.addPopupHeader:productCategoryAddPopupHeader})

    productCategory.update({ObjectName.totalCount:productCategoryTotalCount})

    productCategory.update({ObjectName.defaultStatusLabel:productCategoryDefaultStatusLabel})

    productCategory.update({ObjectName.defaultStatusToggle:productCategoryDefaultStatusToggle})

    return productCategory



