########################################################################################################################################################################################################################################################################################################################################################
# Author: ATE186, Date: 27st June 2022, ID - #69 ||
########################################################################################################################################################################################################################################################################################################################################################
from ObjectRepository.BaseMaster import ElementLicenseAuthority
from Setting import FieldName
from Utilities import Utility


def licenseAuthorityAdd(driver,licenseAuthority):
    Utility.click(driver,ElementLicenseAuthority.masterIcon)
    Utility.click(driver,ElementLicenseAuthority.baseMasterIcon)
    Utility.click(driver,ElementLicenseAuthority.licenseAuthorityIcon)
    Utility.click(driver,ElementLicenseAuthority.licenseAuthorityAdd)
    Utility.sendKeys(driver,ElementLicenseAuthority.licenseAuthorityName,licenseAuthority.get(FieldName.licenseAuthorityName))
    Utility.sendKeys(driver,ElementLicenseAuthority.licenseAuthorityShortName,licenseAuthority.get(FieldName.licenseAuthorityShortName))
    Utility.selectByText(driver,ElementLicenseAuthority.licenseAuthorityCountry,licenseAuthority.get(FieldName.licenseAuthorityCountry))
    Utility.click(driver,ElementLicenseAuthority.licenseAuthorityAddSubmit)