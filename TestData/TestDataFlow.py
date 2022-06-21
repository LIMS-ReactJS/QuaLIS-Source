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