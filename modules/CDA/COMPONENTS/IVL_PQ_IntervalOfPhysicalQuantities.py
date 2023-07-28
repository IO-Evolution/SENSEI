from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
from STRUCTURE_UTILS.Component import Component as Component

from INT_IntegerNumber import INT_IntegerNumber

class IVL_PQ_IntervalOfPhysicalQuantities(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.low = Element.Component(INT_IntegerNumber, "low", data)
        self.high = Element.Component(INT_IntegerNumber, "high", data)
        self.center = Element.Component(INT_IntegerNumber, "center", data)

    @classmethod
    def as_dict(cls):
        return {
            "low": INT_IntegerNumber.as_dict(),
            "high": INT_IntegerNumber.as_dict(),
            "center": INT_IntegerNumber.as_dict()
        }