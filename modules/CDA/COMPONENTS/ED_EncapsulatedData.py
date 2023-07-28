from STRUCTURE_UTILS.Component import Component
from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element

from TEL_TelecomincationAddress import TEL_TelecomincationAddress

class ED_EncapsulatedData(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.mediaType = Element.Attribute("mediaType", data)
        self.representation = Element.Attribute("representation", data)

        self.reference = Element.Component(TEL_TelecomincationAddress, "reference", data)
        self.thumbnail = Element.Component(ED_EncapsulatedData, "thumbnail", data)

        if self.reference is None and self.thumbnail is None:
            try:
                self.text = data["text"]
            except:
                raise InvalidGivenValue("Text Needed")
    
    @classmethod
    def as_dict(cls):
        return {
            "mediaType": "",
            "representation": "",
            "reference": TEL_TelecomincationAddress.as_dict(),
            "thumbnail": "REC",
            "text": ""
        }
