from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
import STRUCTURE_UTILS.Component as Component

class PatientRole(Component):
    def __init__(self, name: str, data: dict):
        self.name = name

        self.realmCode = Element.Component(CS_CodedSimpleValue, "realmCode", data)
        self.typeId = Element.Component(InfrastructureRootTypeId, "typeId", data, as_list=False)
        self.templateId = Element.Component(II_InstanceIdentifier, "templateId", data)
        self.id = Element.Component(II_InstanceIdentifier, "id", data, required=True)
        self.addr = Element.Component(AD_PostalAddress, "addr", data)
        self.telecom = Element.Component(TEL_TelecomincationAddress, "telecom", data)
        self.patient = Element.Component(Patient, "patinet", as_list=False)
        self.providerOrganization = Element.Component(Organization, "providerOrganization", data, as_list=False)
        self.classCode = Element.Attribute("classCode", data, fixed="PAT")

    @classmethod
    def as_dict(cls):
        return {
            "realmCode": CS_CodedSimpleValue.as_dict(),
            "typeId": InfrastructureRootTypeId.as_dict(),
            "templateId": II_InstanceIdentifier.as_dict(),
            "id": II_InstanceIdentifier.as_dict(),
            "addr": AD_PostalAddress.as_dict(),
            "telecom": TEL_TelecomincationAddress.as_dict(),
            "classCode": ""
        }