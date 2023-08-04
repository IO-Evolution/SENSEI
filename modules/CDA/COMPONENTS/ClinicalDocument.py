# from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
from STRUCTURE_UTILS.Component import Component

from CS_CodedSimpleValue import CS_CodedSimpleValue
from InfrastructureRootTypeId import InfrastructureRootTypeId
from II_InstanceIdentifier import II_InstanceIdentifier
from CE_CodedWithEquivalents import CE_CodedWithEquivalents
from ST_String import ST_String
from TS_PointInTime import TS_PointInTime
from INT_IntegerNumber import INT_IntegerNumber
from RecordTarget import RecordTarget
from Author import Author
from DataEnterer import DataEnterer
from Custodian import Custodian
from InformationRecipient import InformationRecipient
from LegalAuthenticator import LegalAuthenticator
from Authenticator import Authenticator
from InFulfillmentOf import InFulfillmentOf
from DocumentationOf import DocumentationOf
from RelatedDocument import RelatedDocument
from Authorization import Authorization
from Component1 import Component1
from Component2 import Component2

class ClinicalDocument(Component):
    """ClinicalDocument"""
    def __init__(self, name: str, data: dict):
        self.name                 = name
        # HEADER
        self.realmCode            = Element.Component(CS_CodedSimpleValue, "realmCode", data)
        self.typeId               = Element.Component(InfrastructureRootTypeId, "typeId", data, required=True, as_list=False)
        self.templateId           = Element.Component(II_InstanceIdentifier, "templateId", data)
        self.id                   = Element.Component(II_InstanceIdentifier, "id", data, required=True, as_list=False)
        self.code                 = Element.Component(CE_CodedWithEquivalents, "code", data, required=True, as_list=False)
        self.title                = Element.Component(ST_String, "title", data, as_list=False)
        self.effectiveTime        = Element.Component(TS_PointInTime, "effectiveTime", data, required=True, as_list=False)
        self.confidentialityCode  = Element.Component(CE_CodedWithEquivalents, "confidentialityCode", data, required=True, as_list=False)
        self.languageCode         = Element.Component(CS_CodedSimpleValue, "languageCode", data, as_list=False)
        self.setId                = Element.Component(II_InstanceIdentifier, "setId", data, as_list=False)
        self.versionNumber        = Element.Component(INT_IntegerNumber, "versionNumber", data, as_list=False)
        self.copyTime             = Element.Component(TS_PointInTime, "copyTime", data, as_list=False)
        self.recordTarget         = Element.Component(RecordTarget, "recordTarget", data, required=True)
        self.author               = Element.Component(Author, "author", data, required=True)
        self.dataEnterer          = Element.Component(DataEnterer, "dataEnterer", data, as_list=False)
        #self.informant           = Element.Component(Informant, "informant", data)
        self.custodian            = Element.Component(Custodian, "custodian", data, required=True, as_list=False)
        self.informationRecipient = Element.Component(InformationRecipient, "informationRecipient", data)
        self.legalAuthenticator   = Element.Component(LegalAuthenticator, "legalAuthenticator", data, as_list=False)
        self.authenticator        = Element.Component(Authenticator, "authenticator", data)
        #self.participant         = Element.Component(Participant, "participant", data)
        self.inFulfillmentOf      = Element.Component(InFulfillmentOf, "inFulfillmentOf", data)
        self.documentationOf      = Element.Component(DocumentationOf, "documentationOf", data)
        self.relatedDocument      = Element.Component(RelatedDocument, "relatedDocument", data)
        self.authorization        = Element.Component(Authorization, "authorization", data)
        self.componentOf          = Element.Component(Component1, "componentOf", data, as_list=False)
        # BODY
        self.component            = Element.Component(Component2, "component", data, required=True, as_list=False)
        #self.classCode           = Element.Component(ActClinicalDocument, "classCode", data, as_list=False)
        #self.moodCode            = Element.Component(ActMood, "moodCode", data, as_list=False)

    @classmethod
    def as_dict(cls):
        """as_dict"""        
        return {
            "realmCode"          : CS_CodedSimpleValue.as_dict(),
            "typeId"             : InfrastructureRootTypeId.as_dict(),
            "templateId"         : II_InstanceIdentifier.as_dict(),
            "id"                 : II_InstanceIdentifier.as_dict(),
            "code"               : CE_CodedWithEquivalents.as_dict(),
            "title"              : ST_String.as_dict(),
            "effectiveTime"      : TS_PointInTime.as_dict(),
            "confidentialityCode": CE_CodedWithEquivalents.as_dict(),
            "languageCode"       : CS_CodedSimpleValue.as_dict(),
            "setId"              : II_InstanceIdentifier.as_dict(),
            "versionNumber"      : INT_IntegerNumber.as_dict(),
            "copyTime"           : TS_PointInTime.as_dict(),
            "recordTarget"       : RecordTarget.as_dict()
        }
