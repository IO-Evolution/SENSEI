from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
from STRUCTURE_UTILS.Component import Component

from II_InstanceIdentifier import II_InstanceIdentifier

class InfrastructureRootTypeId(II_InstanceIdentifier):
    """InfrastructureRootTypeId"""    
    def __init__(self, name: str, data: dict):
        data["root"] = "2.16.840.1.113883.1.3"
        II_InstanceIdentifier.__init__(self, name, data)
        