from STRUCTURE_UTILS.exceptions import InvalidGivenValue
import STRUCTURE_UTILS.elements as Element
import STRUCTURE_UTILS.Component as Component

class InfrastructureRootTypeId(II_InstanceIdentifier):
    def __init__(self, name: str, data: dict):
        data["root"] = "2.16.840.1.113883.1.3"
        II_InstanceIdentifier.__init__(self, name, data)