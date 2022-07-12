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

from Setting import FieldName, InterfaceType, ActiveStatus, YesNo, ParameterType


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

def technique():
    name="Chemical Technique"
    description="Chemical technique is used to test the chemical process"
    technique={}
    technique.update({FieldName.techniqueName:name})
    technique.update({FieldName.techniqueDescription:description})
    return technique

def instrumentCategory():
    name="MED INST CAT"
    description="Medical Instrument Category"
    techniqueName=technique().get(FieldName.techniqueName)
    instrumentCategory={}
    instrumentCategory.update({FieldName.instrumentCategoryName:name})
    instrumentCategory.update({FieldName.instrumentCategoryDescription:description})
    instrumentCategory.update({FieldName.instrumentCategoryTechnique:techniqueName})
    instrumentCategory.update({FieldName.instrumentCategoryInterface:InterfaceType.logiLab})
    return instrumentCategory

def supplier():
    name="Medical Supplier"
    supplier={}
    supplier.update({FieldName.supplierName:name})
    return supplier


def instrument():
    ID="INST 2022"
    name="Medical Instrument"
    supplierName=supplier().get(FieldName.supplierName)
    serialNumber="IC2022"
    manufacturerDate="10-JULY-2022"
    PODate="11-JULY-2022"
    receivedDate="12-JULY-2022"
    installationDate="13-JULY-2022"
    expiryDate="14-JULY-2022"
    instrument={}
    instrument.update({FieldName.instrumentID:ID})
    instrument.update({FieldName.instrumentName:name})
    instrument.update({FieldName.instrumentSupplier:supplierName})
    instrument.update({FieldName.instrumentCategoryName:instrumentCategory().get(FieldName.instrumentCategoryName)})
    instrument.update({FieldName.instrumentSerialNumber:serialNumber})
    instrument.update({FieldName.instrumentManufacturerDate:manufacturerDate})
    instrument.update({FieldName.instrumentPODate:PODate})
    instrument.update({FieldName.instrumentInstallationDate:installationDate})
    instrument.update({FieldName.instrumentReceivedDate:receivedDate})
    instrument.update({FieldName.instrumentExpireDate:expiryDate})
    return instrument

def courier():
    name="Agaram Courier"
    contactPerson="Murali.R"
    addressOne="Nungambakkam"
    addressTwo="Chennai"
    addressThree="TamilNadu, India"
    countryName=country().get(FieldName.countryName)
    phoneNumber="9876543210"
    mobileNumber="9876543210"
    faxNumber="982022"
    email="murali.r@agaramtech.com"
    courier={}
    courier.update({FieldName.courierName:name})
    courier.update({FieldName.courierContactPerson:contactPerson})
    courier.update({FieldName.courierAddressOne:addressOne})
    courier.update({FieldName.courierAddressTwo:addressTwo})
    courier.update({FieldName.courierAddressThree:addressThree})
    courier.update({FieldName.courierCountry:countryName})
    courier.update({FieldName.courierPhoneNumber:phoneNumber})
    courier.update({FieldName.courierMobileNumber:mobileNumber})
    courier.update({FieldName.courierFaxNumber:faxNumber})
    courier.update({FieldName.courierEmail:email})
    return courier

def client():
    name="AGARAM TECH"
    addressOne="Nungambakkam"
    addressTwo="Chennai"
    addressThree="Tamil Nadu, India"
    phoneNumber="9988776655"
    mobileNumber="9876543210"
    faxNumber="LIMS2022"
    mail="murali.r@agaramtech.com"
    countryName=country().get(FieldName.countryName)
    active=ActiveStatus.active
    client={}
    client.update({FieldName.clientName:name})
    client.update({FieldName.clientAddressOne:addressOne})
    client.update({FieldName.clientAddressTwo:addressTwo})
    client.update({FieldName.clientAddressThree:addressThree})
    client.update({FieldName.clientPhoneNumber:phoneNumber})
    client.update({FieldName.clientMobileNumber:mobileNumber})
    client.update({FieldName.clientFaxNumber:faxNumber})
    client.update({FieldName.clientEmail:mail})
    client.update({FieldName.clientCountry:countryName})
    client.update({FieldName.clientIsActive:active})
    return client

def MAHolder():
    name="AGARAM MA Holder001"
    addressOne="Nungambakkam"
    addressTwo="Chennai"
    addressThree="Tamil Nadu, India"
    countryName=country().get(FieldName.countryName)
    active=ActiveStatus.active
    MAHolder={}
    MAHolder.update({FieldName.MAHolderName:name})
    MAHolder.update({FieldName.MAHolderAddressOne:addressOne})
    MAHolder.update({FieldName.MAHolderAddressTwo:addressTwo})
    MAHolder.update({FieldName.MAHolderAddressThree:addressThree})
    MAHolder.update({FieldName.MAHolderCountry:countryName})
    MAHolder.update({FieldName.MAHolderActive:active})
    return MAHolder

def methodCategory():
    name="PH Method Cat"
    description="Potential of Hydrogen Method cat"
    methodCategory = {}
    methodCategory.update({FieldName.methodCategoryName: name})
    methodCategory.update({FieldName.methodCategoryDescription: description})
    return methodCategory


def method():
    name="PH Test"
    description="Potential of Hydrogen Test"
    methodCategoryName=methodCategory().get(FieldName.name)
    method={}
    method.update({FieldName.methodName: name})
    method.update({FieldName.methodCategoryName: methodCategoryName})
    method.update({FieldName.methodDescription: description})
    return method

def testMaster():
    testCategoryName=testCategory().get(FieldName.testCategoryName)
    name="PH Test"
    abbreviation="Potential of Hydrogen Test"
    description="PH is known as the negative logarithm of H+ ion concentration"
    cost=100
    labName=lab().get(FieldName.name)
    methodName=method().get(FieldName.methodName)
    instrumentCategoryName=instrumentCategory().get(FieldName.instrumentCategoryName)
    accredited=YesNo.yes
    active=YesNo.yes
    parameterName="PH Value"
    ParameterAbbreviation="PH Value"
    parameterType=ParameterType.numeric
    parameterUnit=unit().get(FieldName.name)
    testMaster={}
    testMaster.update({FieldName.testCategoryName:testCategoryName})
    testMaster.update({FieldName.testMasterTestName:name})
    testMaster.update({FieldName.testMasterTestAbbreviation:abbreviation})
    testMaster.update({FieldName.testMasterTestDescription:description})
    return testMaster



