from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
from STRUCTURE_UTILS.Component import Component

class ExternalObservation(Component):
    def __init__(self, name: str, data: dict):
        pass

    @classmethod
    def as_dict(cls):
        return {}