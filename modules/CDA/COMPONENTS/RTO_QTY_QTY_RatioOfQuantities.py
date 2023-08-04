from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
from STRUCTURE_UTILS.Component import Component

from PQ_PhysicalQuantities import PQ_PhysicalQuantities
from INT_IntegerNumber import INT_IntegerNumber

class RTO_QTY_QTY_RatioOfQuantities(Component):
    """RTO_QTY_QTY_RatioOfQuantities"""    
    def __init__(self, name: str, data: dict):
        if not data or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.numerator = Element.Component(PQ_PhysicalQuantities, "numerator", data)
        if "unit" in data["denominator"]:
            self.denominator = Element.Component(PQ_PhysicalQuantities, "denominator", data)
        else: 
            self.denominator = Element.Component(INT_IntegerNumber, "denominator", data)

    @classmethod
    def as_dict(cls):
        """as_dict"""        
        return {
            "numerator"      : PQ_PhysicalQuantities.as_dict(),
            "denominator_int": INT_IntegerNumber.as_dict(),
            "denominator_pq" : PQ_PhysicalQuantities.as_dict()
        }
    