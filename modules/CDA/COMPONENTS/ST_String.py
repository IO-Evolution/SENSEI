from STRUCTURE_UTILS.exceptions import InvalidGivenValue
from STRUCTURE_UTILS.Component import Component

class ST_String(Component):
    """ST_String"""    
    def __init__(self, name: str, data: str):
        if not data or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name
        try:
            self.text = data["text"]
        except:
            raise InvalidGivenValue("Text Needed")

    @classmethod
    def as_dict(cls):
        """as_dict"""        
        return {
            "text": "",
        }
