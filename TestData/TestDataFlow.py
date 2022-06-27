########################################################################################################################################################################################################################################################################################################################################################
# 1. unit() - || Author: ATE186, Date: 20th June 2022, ID - #37 ||
# 2. storageCondition() - || Author: ATE186, Date: 21st June 2022 ID - #37 ||
# 3. productCategory() - || Author: ATE186, Date: 21st June 2022 ID - #37 ||
# 4. testCategory() - || Author: ATE186, Date: 21st June 2022 ID - #37 ||
# 5. lab() - || Author: ATE186, Date: 21st June 2022 ID - #37 ||
# 6. division() - || Author: ATE186, Date: 21st June 2022 ID - #37 ||
# 7. designation() - || Author: ATE186, Date: 21st June 2022 ID - #37 ||
# 8. source() - || Author: ATE186, Date: 21st June 2022 ID - #37 ||
########################################################################################################################################################################################################################################################################################################################################################

from Setting import FieldName

def unit():
    name="CM1"
    description="Centi Meter"
    unit={}
    unit.update({FieldName.name:name})
    unit.update({FieldName.description:description})
    return unit

def storageCondition():
    name="100 C"
    description="100 Degree Celcius"
    storageCondition={}
    storageCondition.update({FieldName.name:name})
    storageCondition.update({FieldName.description:description})
    return storageCondition

def productCategory():
    name="Fuel"
    description="It is about Fuel"
    productCategory={}
    productCategory.update({FieldName.name:name})
    productCategory.update({FieldName.description:description})
    return productCategory

def testCategory():
    name="Fuel"
    description="It is about Fuel"
    testCategory={}
    testCategory.update({FieldName.name:name})
    testCategory.update({FieldName.description:description})
    return testCategory

def lab():
    name="Chemical Lab"
    description="It is about Chemical Lab"
    lab={}
    lab.update({FieldName.name:name})
    lab.update({FieldName.description:description})
    return lab

def division():
    name="Chemical Division"
    description="It is about Chemical Division"
    division={}
    division.update({FieldName.name:name})
    division.update({FieldName.description:description})
    return division

def designation():
    name="Chemical Designation"
    description="It is about Chemical Designation"
    designation={}
    designation.update({FieldName.name:name})
    designation.update({FieldName.description:description})
    return designation

def source():
    name="Chemical Source"
    description="It is about Chemical Source"
    source={}
    source.update({FieldName.name:name})
    source.update({FieldName.description:description})
    return source

userRoleReviewer = "Reviewer"
userRoleApprover = "Approver"
userRoleAnalyst = "Analyst"

def country():
    name="India"
    shortName="IND"
    twoCharName="IN"
    threeCharName="IND"
    country={}
    country.update({FieldName.countryName:name})
    country.update({FieldName.countryShortName:shortName})
    country.update({FieldName.countryTwoChar:twoCharName})
    country.update({FieldName.countryThreeChar:threeCharName})
    return country

def user():
    loginID="murali"
    firstName="Murali"
    lastName="Rajendran"
    initial="R"
    addressOne="Priyan Plaza"
    addressTwo="Nungambakkam, Chennai"
    addressThree="Tamil Nadu, India"
    qualification="B.Tech"
    jobDescription="Chemical Testing"
    mobileNumber="9988776655"
    phoneNumber="0449988776655"
    email="murali.r@agaramtech.com"
    site="UK_NIBSC"
    user={}
    user.update({FieldName.usersLoginID:loginID})
    user.update({FieldName.usersFirstName:firstName})
    user.update({FieldName.usersLastName:lastName})
    user.update({FieldName.usersInitial:initial})
    user.update({FieldName.usersAddressOne:addressOne})
    user.update({FieldName.usersAddressTwo:addressTwo})
    user.update({FieldName.usersQualification:qualification})
    user.update({FieldName.usersJobDescription:jobDescription})
    user.update({FieldName.usersPhoneNumber:phoneNumber})
    user.update({FieldName.usersMobileNumber:mobileNumber})
    user.update({FieldName.usersEmail:email})
    user.update({FieldName.usersDivision:division().get(FieldName.name)})
    user.update({FieldName.usersCountry:country().get(FieldName.countryName)})
    user.update({FieldName.usersUserRole:userRoleAnalyst})
    user.update({FieldName.usersDesignation:designation().get(FieldName.name)})
    return user

def liceseAuthority():
    name="LA001"
    shortName="LA"
    countryName=country().get(FieldName.countryName)
    countryShortName=country().get(FieldName.countryShortName)
    licenseAuthority={}
    licenseAuthority.update({FieldName.licenseAuthorityName:name})
    licenseAuthority.update({FieldName.licenseAuthorityShortName:shortName})
    licenseAuthority.update({FieldName.licenseAuthorityCountry:countryName})
    licenseAuthority.update({FieldName.licenseAuthorityCountryShortName:countryShortName})
    return licenseAuthority

def chargeBand():
    name="CB001"
    description="Charge Band about 0001"
    price="100"
    chargeBand={}
    chargeBand.update({FieldName.chargeBandName:name})
    chargeBand.update({FieldName.chargeBandDescription:description})
    chargeBand.update({FieldName.chargeBandPrice:price})
    return chargeBand
