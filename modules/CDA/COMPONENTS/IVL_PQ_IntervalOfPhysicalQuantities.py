from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
from STRUCTURE_UTILS.Component import Component

from INT_IntegerNumber import INT_IntegerNumber

class IVL_PQ_IntervalOfPhysicalQuantities(Component):
    """IVL_PQ_IntervalOfPhysicalQuantities"""    
    def __init__(self, name: str, data: dict):        
        if not data or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name   = name
        self.low    = Element.Component(INT_IntegerNumber, "low", data)
        self.high   = Element.Component(INT_IntegerNumber, "high", data)
        self.center = Element.Component(INT_IntegerNumber, "center", data)

    @classmethod
    def as_dict(cls):
        """as_dict"""        
        return {
            "low"   : INT_IntegerNumber.as_dict(),
            "high"  : INT_IntegerNumber.as_dict(),
            "center": INT_IntegerNumber.as_dict()
        }
    