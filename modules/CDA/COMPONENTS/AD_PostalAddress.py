from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
import STRUCTURE_UTILS.Component as Component

from COMPONENTS.ST_String import ST_String

class AD_PostalAddress(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.use = Element.Attribute("use", data)

        self.streetAddressLine = Element.Component(ST_String, "streetAddressLine", data, as_list=False)
        self.city = Element.Component(ST_String, "city", data, as_list=False)
        self.postalCode = Element.Component(ST_String, "postalCode", data, as_list=False)
        self.country = Element.Component(ST_String, "country", data, as_list=False)

        """
        https://wiki.hl7.de/index.php?title=HL7_CDA_Core_Principles#Postal_Address_.28AD.29
        """

    @classmethod
    def as_dict(cls):
        return {
            "use": "",
            "steedAddressLine": ST_String.as_dict(),
            "city": ST_String.as_dict(),
            "postalCode": ST_String.as_dict(),
            "country": ST_String.as_dict(),
        }