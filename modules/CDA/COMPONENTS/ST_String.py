from STRUCTURE_UTILS.exceptions import InvalidGivenValue
from STRUCTURE_UTILS import Component


class ST_String(Component):
    def __init__(self, name: str, data: str):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name
        try:
            self.text = data["text"]
        except:
            raise InvalidGivenValue("Text Needed")

    @classmethod
    def as_dict(cls):
        return {
            "text": "",
        }
