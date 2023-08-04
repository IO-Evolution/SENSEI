from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
from STRUCTURE_UTILS.Component import Component

from CS_CodedSimpleValue import CS_CodedSimpleValue
from InfrastructureRootTypeId import InfrastructureRootTypeId
from II_InstanceIdentifier import II_InstanceIdentifier
from CE_CodedWithEquivalents import CE_CodedWithEquivalents
from AD_PostalAddress import AD_PostalAddress
from TEL_TelecomincationAddress import TEL_TelecomincationAddress
from Person import Person
from Organization import Organization

class Guardian(Component):
    """Guardian"""    
    def __init__(self, name: str, data: dict):
        self.realmCode            = Element.Component()
        self.typeId               = Element.Component()
        self.templateId           = Element.Component()
        self.id                   = Element.Component()
        self.code                 = Element.Component()
        self.addr                 = Element.Component()
        self.telecom              = Element.Component()
        self.guardianPerson       = Element.Component()
        self.guardianOrganization = Element.Component()
        self.classCode            = Element.Attribute()

    @classmethod
    def as_dict(cls):
        """as_dict"""        
        return {
            "realmCode"           : CS_CodedSimpleValue.as_dict(),
            "typeId"              : InfrastructureRootTypeId.as_dict(),
            "templateId"          : II_InstanceIdentifier.as_dict(),
            "id"                  : II_InstanceIdentifier.as_dict(),
            "code"                : CE_CodedWithEquivalents.as_dict(),
            "addr"                : AD_PostalAddress.as_dict(),
            "telecom"             : TEL_TelecomincationAddress.as_dict(),
            "guardianPerson"      : Person.as_dict(),
            "guardianOrganization": Organization.as_dict(),
            "classCode"           : ""
        }
    