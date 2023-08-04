from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
from STRUCTURE_UTILS.Component import Component

class PQ_PhysicalQuantities(Component):
    """PQ_PhysicalQuantities"""    
    def __init__(self, name: str, data: dict):
        if not data or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name  = name
        self.value = Element.Attribute("value", data, required=True)
        self.unit  = Element.Attribute("unit", data, required=True)

    @classmethod
    def as_dict(cls):
        """as_dict"""        
        return {
            "value": "",
            "unit" : ""
        }