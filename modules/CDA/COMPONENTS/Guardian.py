from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
import STRUCTURE_UTILS.Component as Component

class Guardian(Component):
    def __init__(self, name: str, data: dict):
        self.realmCode = Element.Component()
        self.typeId = Element.Component()
        self.templateId = Element.Component()
        self.id = Element.Component()
        self.code = Element.Component()
        self.addr = Element.Component()
        self.telecom = Element.Component()
        self.guardianPerson = Element.Component()
        self.guardianOrganization = Element.Component()
        self.classCode = Element.Attribute()

    @classmethod
    def as_dict(cls):
        return {
            "realmCode": CS_CodedSimpleValue.as_dict(),
            "typeId": InfrastructureRootTypeId.as_dict(),
            "templateId": II_InstanceIdentifier.as_dict(),
            "id": II_InstanceIdentifier.as_dict(),
            "code": CE_CodedWithEquivalents.as_dict(),
            "addr": AD_PostalAddress.as_dict(),
            "telecom": TEL_TelecomincationAddress.as_dict(),
            "guardianPerson": Person.as_dict(),
            "guardianOrganization": Organization.as_dict(),
            "classCode": ""
        }