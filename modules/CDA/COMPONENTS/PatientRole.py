from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
from STRUCTURE_UTILS.Component import Component

from CS_CodedSimpleValue import CS_CodedSimpleValue
from II_InstanceIdentifier import II_InstanceIdentifier
from AD_PostalAddress import AD_PostalAddress
from TEL_TelecomincationAddress import TEL_TelecomincationAddress
from InfrastructureRootTypeId import InfrastructureRootTypeId
from Patient import Patient
from Organization import Organization

class PatientRole(Component):
    """PatientRole"""    
    def __init__(self, name: str, data: dict):
        self.name                 = name
        self.realmCode            = Element.Component(CS_CodedSimpleValue, "realmCode", data)
        self.typeId               = Element.Component(InfrastructureRootTypeId, "typeId", data, as_list=False)
        self.templateId           = Element.Component(II_InstanceIdentifier, "templateId", data)
        self.id                   = Element.Component(II_InstanceIdentifier, "id", data, required=True)
        self.addr                 = Element.Component(AD_PostalAddress, "addr", data)
        self.telecom              = Element.Component(TEL_TelecomincationAddress, "telecom", data)
        self.patient              = Element.Component(Patient, "patinet", as_list=False)
        self.providerOrganization = Element.Component(Organization, "providerOrganization", data, as_list=False)
        self.classCode            = Element.Attribute("classCode", data, fixed="PAT")

    @classmethod
    def as_dict(cls):
        """as_dict"""        
        return {
            "realmCode" : CS_CodedSimpleValue.as_dict(),
            "typeId"    : InfrastructureRootTypeId.as_dict(),
            "templateId": II_InstanceIdentifier.as_dict(),
            "id"        : II_InstanceIdentifier.as_dict(),
            "addr"      : AD_PostalAddress.as_dict(),
            "telecom"   : TEL_TelecomincationAddress.as_dict(),
            "classCode" : ""
        }
    