from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
from STRUCTURE_UTILS.Component import Component as Component

from ST_String import ST_String
from IVL_TS_IntervalOfTime import IVL_TS_IntervalOfTime

class PN_PersonName(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.given = Element.Component(ST_String, "given", data)
        self.family = Element.Component(ST_String, "family", data)
        self.validTime = Element.Component(IVL_TS_IntervalOfTime, "validTime", data)

    @classmethod
    def as_dict(cls):
        return {
            "family": ST_String.as_dict(),
            "given": ST_String.as_dict(),
            "validTime": IVL_TS_IntervalOfTime.as_dict()
        }