from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
import STRUCTURE_UTILS.Component as Component

from COMPONENTS.IVL_TS_IntervalOfTime import IVL_TS_IntervalOfTime

class TEL_TelecomincationAddress(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.value = Element.Attribute("value", data, required=True)
        self.use = Element.Attribute("use", data)

        """
            value:
            telephone (tel:)
            fax (fax:)
            email (mailto:)

            use:
            H: home
            WP: Work
            MC: mobile phone
        """

        self.useablePeriod = Element.Component(IVL_TS_IntervalOfTime, "useablePeriod", data, as_list=False)

    @classmethod
    def as_dict(cls):
        return {
            "value": "",
            "use": "",
            "useablePeriod": IVL_TS_IntervalOfTime.as_dict()
        }