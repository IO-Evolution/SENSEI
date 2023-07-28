from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
import STRUCTURE_UTILS.Component as Component

from COMPONENTS.PQ_PhysicalQuantities import PQ_PhysicalQuantities
from COMPONENTS.INT_IntegerNumber import INT_IntegerNumber

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