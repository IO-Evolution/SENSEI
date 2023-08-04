from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
from STRUCTURE_UTILS.Component import Component

from INT_IntegerNumber import INT_IntegerNumber
from PQ_PhysicalQuantities import PQ_PhysicalQuantities

class IVL_TS_IntervalOfTime(Component):
    def __init__(self, name: str, data: dict):
        """__init__"""        
        if not data or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name   = name
        self.low    = Element.Component(INT_IntegerNumber, "low", data)
        self.high   = Element.Component(INT_IntegerNumber, "high", data)
        self.center = Element.Component(INT_IntegerNumber, "center", data)
        self.width  = Element.Component(PQ_PhysicalQuantities, "width", data)

    @classmethod
    def as_dict(cls):
        """as_dict"""        
        return {
            "low"   : INT_IntegerNumber.as_dict(),
            "high"  : INT_IntegerNumber.as_dict(),
            "center": INT_IntegerNumber.as_dict(),
            "width" : PQ_PhysicalQuantities.as_dict()
        }
    