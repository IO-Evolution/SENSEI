from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
from STRUCTURE_UTILS.Component import Component

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
