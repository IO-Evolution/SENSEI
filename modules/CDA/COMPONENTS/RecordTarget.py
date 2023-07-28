from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
from STRUCTURE_UTILS.Component import Component as Component

class RecordTarget(Component):
    def __init__(self, name: str, data: dict):
        self.name = name

        self.realmCode = Element.Component(CS_CodedSimpleValue, "realmCode", data)
        self.typeId = Element.Component(InfrastructureRootTypeId, "typeId", data, as_list=False)
        self.templateId = Element.Component(II_InstanceIdentifier, "templateId", data)
        self.patientRole = Element.Component(PatientRole, "patientRole", data, required=True, as_list=False)

        self.typeCode = Element.Attribute("typeCode", data, fixed="RCT")
        self.contextControlCode = Element.Attribute("contextControlCOde", data, fixed="OP")

    @classmethod
    def as_dict(cls):
        return {
            "relamCode": CS_CodedSimpleValue.as_dict(),
            "typeId": InfrastructureRootTypeId.as_dict(),
            "templateId": II_InstanceIdentifier.as_dict(),
            "patientRole": PatientRole.as_dict(),
            "typeCode": "",
            "contectControlCode": ""
        }