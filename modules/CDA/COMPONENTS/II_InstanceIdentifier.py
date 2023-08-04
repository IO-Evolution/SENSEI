from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
from STRUCTURE_UTILS.Component import Component

class II_InstanceIdentifier(Component):
    """II_InstanceIdentifier"""    
    def __init__(self, name: str, data: dict):
        if not data or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name      = name
        self.root      = Element.Attribute("root", data, required=True)
        self.extension = Element.Attribute("extension", data)

    @classmethod
    def as_dict(cls):
        """as_dict"""        
        return {
            "root"     : "",
            "extension": ""
        }
