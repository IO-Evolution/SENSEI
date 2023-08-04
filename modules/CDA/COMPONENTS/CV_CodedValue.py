from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
from STRUCTURE_UTILS.Component import Component

from ST_String import ST_String

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