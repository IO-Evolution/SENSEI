from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
from STRUCTURE_UTILS.Component import Component

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