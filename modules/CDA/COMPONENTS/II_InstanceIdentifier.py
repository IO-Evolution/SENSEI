from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
import STRUCTURE_UTILS.Component as Component

class II_InstanceIdentifier(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name
        self.root = Element.Attribute("root", data, required=True)
        self.extension = Element.Attribute("extension", data)

    @classmethod
    def as_dict(cls):
        return {
            "root": "",
            "extension": ""
        }
