from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
import STRUCTURE_UTILS.Component as Component

class Patient(Component):
    def __init__(self, name: str, data: dict):
        self.realmCode = Element.Component(CS_CodedSimpleValue, "realmCode", data)
        self.typeId = Element.Component(InfrastructureRootTypeId, "typeId", data, as_list=False)
        self.templateId = Element.Component(II_InstanceIdentifier, "templateId", data)
        self.id = Element.Component(II_InstanceIdentifier, "id", data, as_list=False)
        self.name_ = Element.Component(PN_PersonName, "name", data)
        self.administrativeGenderCode = Element.Component(CE_CodedWithEquivalents, "administrativeGenderCode", data, as_list=False)
        self.birthTime = Element.Component(TS_PointInTime, "birthTime", data, as_list=False)
        self.maritalStatusCode = Element.Component(CE_CodedWithEquivalents, "maritalStatusCode", data, as_list=True)
        self.religiousAfflitionCode = Element.Component(CE_CodedWithEquivalents, "religiousAfflitionCode", data, as_list=True)
        self.raceCode = Element.Component(CE_CodedWithEquivalents, "raceCode", data, as_list=True)
        self.ethnicGroupCode = Element.Component(CE_CodedWithEquivalents, "ethnicGroupCode", data, as_list=True)
        self.guardian = Element.Component(Guardian, "guardian", data)
        self.birthplace = Element.Component(BirthPlace, "birthplace", data, as_list=False)
        self.languageCommunication = Element.Component(LanguageCommunication, "languageCommunication", data)
        self.classCode = Element.Attribute("classCode", data, fixed="PSN")
        self.determinerCode = Element.Attribute("determinerCode", data, fixed="INSTANCE")

    @classmethod
    def as_dict(cls):
        return {
            "realmCode": CS_CodedSimpleValue.as_dict(),
            "typeId": InfrastructureRootTypeId.as_dict(),
            "templateId": II_InstanceIdentifier.as_dict(),
            "id": II_InstanceIdentifier.as_dict(),
            "name": PN_PersonName.as_dict(),
            "administrativeGenderCode": CE_CodedWithEquivalents.as_dict(),
            "birthTime": TS_PointInTime.as_dict(),
            "maritalStatusCode": CE_CodedWithEquivalents.as_dict(),
            "religiousAfflitionCode": CE_CodedWithEquivalents.as_dict(),
            "raceCode": CE_CodedWithEquivalents.as_dict(),
            "ethnicGroupCode": CE_CodedWithEquivalents.as_dict(),
            "guardian": Guardian.as_dict(),
            "birthplace": BirthPlace.as_dict(),
            "languageCommunication": LanguageCommunication.as_dict(),
            "classCode": "",
            "determinerCode": ""
        }