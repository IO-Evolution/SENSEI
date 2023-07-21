from exceptions import InvalidGivenValue
from enum import Enum
import elements as Element


class Component:
    name: str
    value: str


class BL_Boolean(Component):
    def __init__(self, name: str, data):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name
        self.value = Element.Attribute("value", data, required=True)

    @classmethod
    def as_dict(cls):
        return {
            "value": ""
        }


class II_InstanceIdentifier(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name
        self.root = Element.Attribute("root", data, required=True)
        self.extension = Element.Attribute("extension", data)

    @classmethod
    def as_dict(cls):
        return {
            "root": "",
            "extension": ""
        }


class ED_EncapsulatedData(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.mediaType = Element.Attribute("mediaType", data)
        self.representation = Element.Attribute("representation", data)

        self.reference = Element.Component(TEL_TelecomincationAddress, "reference", data)
        self.thumbnail = Element.Component(ED_EncapsulatedData, "thumbnail", data)

        if self.reference is None and self.thumbnail is None:
            try:
                self.text = data["text"]
            except:
                raise InvalidGivenValue("Text Needed")
    
    @classmethod
    def as_dict(cls):
        return {
            "mediaType": "",
            "representation": "",
            "reference": TEL_TelecomincationAddress.as_dict(),
            "thumbnail": ED_EncapsulatedData.as_dict(),
            "text": ""
        }


class ST_String(Component):
    def __init__(self, name: str, data: str):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name
        try:
            self.text = data["text"]
        except:
            raise InvalidGivenValue("Text Needed")

    @classmethod
    def as_dict(cls):
        return {
            "text": "",
        }

class CD_ConceptDescriptor(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.code = Element.Attribute("code", data, required=True)
        self.codeSystem = Element.Attribute("codeSystem", data, required=True)
        self.codeSystemVersion = Element.Attribute("codeSystemVersion", data)
        self.displayName = Element.Attribute("displayName", data)
        self.originalText = Element.Component(ST_String, "originalText", data)
        self.translaction = Element.Component(CD_ConceptDescriptor, "translaction", data)
        self.qualifier = Element.Attribute("qualifier", data)

    @classmethod
    def as_dict(cls):
        return {
            "code": "",
            "codeSystem": "",
            "codeSysteVersion": "",
            "displayName": "",
            "originalText": ST_String.as_dict(),
            "translaction": "RECURSIVE",
            "qualifier": ""
        }


class CE_CodedWithEquivalents(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.code = Element.Attribute("code", data, required=True)
        self.codeSystem = Element.Attribute("codeSystem", data, required=True)
        self.codeSystemVersion = Element.Attribute("codeSystemVersion", data)
        self.displayName = Element.Attribute("displayName", data)
        self.originalText = Element.Component(ST_String, "originalText", data)
        self.translaction = Element.Component(CD_ConceptDescriptor, "translaction", data)

    @classmethod
    def as_dict(cls):
        return {
            "code": "",
            "codeSystem": "",
            "codeSysteVersion": "",
            "displayName": "",
            "originalText": ST_String.as_dict(),
            "translaction": CD_ConceptDescriptor.as_dict()
        }


class CV_CodedValue(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.code = Element.Attribute("code", data, required=True)
        self.codeSystem = Element.Attribute("codeSystem", data, required=True)
        self.codeSystemVersion = Element.Attribute("codeSystemVersion", data)
        self.displayName = Element.Attribute("displayName", data)
        self.originalText = Element.Component(ST_String, "originalText", data)

    @classmethod
    def as_dict(cls):
        return {
            "code": "",
            "codeSystem": "",
            "codeSysteVersion": "",
            "displayName": "",
            "originalText": ST_String.as_dict()
        }


class CS_CodedSimpleValue(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.code = Element.Attribute("code", data, required=True)

    @classmethod
    def as_dict(cls):
        return {
            "code": ""
        }


class TEL_TelecomincationAddress(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.value = Element.Attribute("value", data, required=True)
        self.use = Element.Attribute("use", data)

        """
            value:
            telephone (tel:)
            fax (fax:)
            email (mailto:)

            use:
            H: home
            WP: Work
            MC: mobile phone
        """

        self.useablePeriod = Element.Component(IVL_TS_IntervalOfTime, "useablePeriod", data, as_list=False)

    @classmethod
    def as_dict(cls):
        return {
            "value": "",
            "use": "",
            "useablePeriod": IVL_TS_IntervalOfTime.as_dict()
        }

class AD_PostalAddress(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.use = Element.Attribute("use", data)

        self.streetAddressLine = Element.Component(ST_String, "streetAddressLine", data, as_list=False)
        self.city = Element.Component(ST_String, "city", data, as_list=False)
        self.postalCode = Element.Component(ST_String, "postalCode", data, as_list=False)
        self.country = Element.Component(ST_String, "country", data, as_list=False)

        """
        https://wiki.hl7.de/index.php?title=HL7_CDA_Core_Principles#Postal_Address_.28AD.29
        """

    @classmethod
    def as_dict(cls):
        return {
            "use": "",
            "steedAddressLine": ST_String.as_dict(),
            "city": ST_String.as_dict(),
            "postalCode": ST_String.as_dict(),
            "country": ST_String.as_dict(),
        }


class PN_PersonName(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.given = Element.Component(ST_String, "given", data)
        self.family = Element.Component(ST_String, "family", data)
        self.validTime = Element.Component(IVL_TS_IntervalOfTime, "validTime", data)

    @classmethod
    def as_dict(cls):
        return {
            "family": ST_String.as_dict(),
            "given": ST_String.as_dict(),
            "validTime": IVL_TS_IntervalOfTime.as_dict()
        }


class ON_OrganisationName(Component):
    def __init__(self, name: str, data: str):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name
        try:
            self.text = data["text"]
        except:
            raise InvalidGivenValue("Text Needed")

        # self.validTime = Element.Component("validTime", IVL_TS_IntervalOfTime, data)
        """ ????
            <name>The old hospital
                <validTime> 
                    <high value="20111231235959"/>
                </validTime>
            </name>
        """

    @classmethod
    def as_dict(cls):
        return {
            "text": ""
        }

class INT_IntegerNumber(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.value = Element.Attribute("value", data, required=True)

    @classmethod
    def as_dict(cls):
        return {
            "value": ""
        }


class PQ_PhysicalQuantities(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.value = Element.Attribute("value", data, required=True)
        self.unit = Element.Attribute("unit", data, required=True)

    @classmethod
    def as_dict(cls):
        return {
            "value": "",
            "unit": ""
        }


class TS_PointInTime(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.value = Element.Attribute("value", data, required=True)

    @classmethod
    def as_dict(cls):
        return {
            "value": ""
        }

# class IVL_Intervals(Component):
#     def __init__(self, name: str, data: dict):
# if data == {} or data is None:
#  raise InvalidGivenValue("Empty Data Set")
#
# self.name = name


class IVL_TS_IntervalOfTime(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.low = Element.Component(INT_IntegerNumber, "low", data)
        self.high = Element.Component(INT_IntegerNumber, "high", data)
        self.center = Element.Component(INT_IntegerNumber, "center", data)
        self.width = Element.Component(PQ_PhysicalQuantities, "width", data)

    @classmethod
    def as_dict(cls):
        return {
            "low": INT_IntegerNumber.as_dict(),
            "high": INT_IntegerNumber.as_dict(),
            "center": INT_IntegerNumber.as_dict(),
            "width": PQ_PhysicalQuantities.as_dict()
        }


class IVL_PQ_IntervalOfPhysicalQuantities(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.low = Element.Component(INT_IntegerNumber, "low", data)
        self.high = Element.Component(INT_IntegerNumber, "high", data)
        self.center = Element.Component(INT_IntegerNumber, "center", data)

    @classmethod
    def as_dict(cls):
        return {
            "low": INT_IntegerNumber.as_dict(),
            "high": INT_IntegerNumber.as_dict(),
            "center": INT_IntegerNumber.as_dict()
        }


class RTO_QTY_QTY_RatioOfQuantities(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.numerator = Element.Component(PQ_PhysicalQuantities, "numerator", data)
        if "unit" in data["denominator"]:
            self.denominator = Element.Component(PQ_PhysicalQuantities, "denominator", data)
        else:
            self.denominator = Element.Component(INT_IntegerNumber, "denominator", data)

    @classmethod
    def as_dict(cls):
        return {
            "numerator": PQ_PhysicalQuantities.as_dict(),
            "denominator_int": INT_IntegerNumber.as_dict(),
            "denominator_pq": PQ_PhysicalQuantities.as_dict()
        }
    
    
# ==================================================================


class ClinicalDocument(Component):
    def __init__(self, name: str, data: dict):
        self.name = name

        self.realmCode = Element.Component(CS_CodedSimpleValue, "realmCode", data)
        self.typeId = Element.Component(InfrastructureRootTypeId, "typeId", data, required=True, as_list=False)
        self.templateId = Element.Component(II_InstanceIdentifier, "templateId", data)
        self.id = Element.Component(II_InstanceIdentifier, "id", data, required=True, as_list=False)
        self.code = Element.Component(CE_CodedWithEquivalents, "code", data, required=True, as_list=False)
        self.title = Element.Component(ST_String, "title", data, as_list=False)
        self.effectiveTime = Element.Component(TS_PointInTime, "effectiveTime", data, required=True, as_list=False)
        self.confidentialityCode = Element.Component(CE_CodedWithEquivalents, "confidentialityCode", data, required=True, as_list=False)
        self.languageCode = Element.Component(CS_CodedSimpleValue, "languageCode", data, as_list=False)
        self.setId = Element.Component(II_InstanceIdentifier, "setId", data, as_list=False)
        self.versionNumber = Element.Component(INT_IntegerNumber, "versionNumber", data, as_list=False)
        self.copyTime = Element.Component(TS_PointInTime, "copyTime", data, as_list=False)
        self.recordTarget = Element.Component(RecordTarget, "recordTarget", data, required=True)
        # self.author = Element.Component(Author, "author", data, required=True)
        # self.dataEnterer = Element.Component(DataEnterer, "dataEnterer", data, as_list=False)
        # self.informant = Element.Component(Informant, "informant", data)
        # self.custodian = Element.Component(Custodian, "custodian", data, required=True, as_list=False)
        # self.informationRecipient = Element.Component(InformationRecipient, "informationRecipient", data)
        # self.legalAuthenticator = Element.Component(LegalAuthenticator, "legalAuthenticator", data, as_list=False)
        # self.authenticator = Element.Component(Authenticator, "authenticator", data)
        # self.participant = Element.Component(Participant, "participant", data)
        # self.inFulfillmentOf = Element.Component(InFulfillmentOf, "inFulfillmentOf", data)
        # self.documentationOf = Element.Component(DocumentationOf, "documentationOf", data)
        # self.relatedDocument = Element.Component(RelatedDocument, "relatedDocument", data)
        # self.authorization = Element.Component(Authorization, "authorization", data)
        # self.componentOf = Element.Component(Component1, "componentOf", data, as_list=False)
        # self.component = Element.Component(Component2, "component", data, required=True, as_list=False)
        # self.classCode = Element.Component(ActClinicalDocument, "classCode", data, as_list=False)
        # self.moodCode = Element.Component(ActMood, "moodCode", data, as_list=False)

    @classmethod
    def as_dict(cls):
        return {
            "realmCode": CS_CodedSimpleValue.as_dict(),
            "typeId": InfrastructureRootTypeId.as_dict(),
            "templateId": II_InstanceIdentifier.as_dict(),
            "id": II_InstanceIdentifier.as_dict(),
            "code": CE_CodedWithEquivalents.as_dict(),
            "title": ST_String.as_dict(),
            "effectiveTime": TS_PointInTime.as_dict(),
            "confidentialityCode": CE_CodedWithEquivalents.as_dict(),
            "languageCode": CS_CodedSimpleValue.as_dict(),
            "setId": II_InstanceIdentifier.as_dict(),
            "versionNumber": INT_IntegerNumber.as_dict(),
            "copyTime": TS_PointInTime.as_dict(),
            "recordTarget": RecordTarget.as_dict()
        }
    
class InfrastructureRootTypeId(II_InstanceIdentifier):
    def __init__(self, name: str, data: dict):
        data["root"] = "2.16.840.1.113883.1.3"
        II_InstanceIdentifier.__init__(self, name, data)

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

class PatientRole(Component):
    def __init__(self, name: str, data: dict):
        self.name = name

        self.realmCode = Element.Component(CS_CodedSimpleValue, "realmCode", data)
        self.typeId = Element.Component(InfrastructureRootTypeId, "typeId", data, as_list=False)
        self.templateId = Element.Component(II_InstanceIdentifier, "templateId", data)
        self.id = Element.Component(II_InstanceIdentifier, "id", data, required=True)
        self.addr = Element.Component(AD_PostalAddress, "addr", data)
        self.telecom = Element.Component(TEL_TelecomincationAddress, "telecom", data)
        # self.patient = Element.Component(Patient, "patinet", as_list=False)
        # self.providerOrganization = Element.Component(Organization, "providerOrganization", data, as_list=False)
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
