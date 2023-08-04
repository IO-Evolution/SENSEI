from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
from STRUCTURE_UTILS.Component import Component

class ON_OrganisationName(Component):
    """ON_OrganisationName"""    
    def __init__(self, name: str, data: str):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name
        try:
            self.text = data["text"]
        except:
            raise InvalidGivenValue("Text Needed")

        # self.validTime = Element.Component("validTime", IVL_TS_IntervalOfTime, data)
        """ ????
            <name>The old hospital
                <validTime> 
                    <high value="20111231235959"/>
                </validTime>
            </name>
        """

    @classmethod
    def as_dict(cls):
        """as_dict"""        
        return {
            "text": ""
        }
    