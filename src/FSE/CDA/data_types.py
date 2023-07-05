import elements as el

class Component:
    name: str
    value: str

class BL_Boolean(Component):
    def __init__(self, name: str, data):
        self.name = name
        self.value = el.Attribute("value", data)

class II_InstanceIdentifier(Component):
    def __init__(self, name: str, data: dict):
        self.name = name
        self.root = el.Attribute("root", data)
        self.extension = el.Attribute("extension", data)

class ED_EncapsulatedData(Component):
    def __init__(self, name: str, data: dict):
        self.name = name

class CD_ConceptDescriptor(Component):
    def __init__(self, name: str, data: dict):
        self.name = name

class CE_CodedWithEquivalents(Component):
    def __init__(self, name: str, data: dict):
        self.name = name

class CV_CodedValue(Component):
    def __init__(self, name: str, data: dict):
        self.name = name

class CS_CodedSimpleValue(Component):
    def __init__(self, name: str, data: dict):
        self.name = name

class TEL_TelecomincationAddress(Component):
    def __init__(self, name: str, data: dict):
        self.name = name

class AD_PostalAddress(Component):
    def __init__(self, name: str, data: dict):
        self.name = name

class PN_PersonName(Component):
    def __init__(self, name: str, data: dict):
        self.name = name

class ON_OrganisationName(Component):
    def __init__(self, name: str, data: dict):
        self.name = name

class INT_IntegerNumber(Component):
    def __init__(self, name: str, data: dict):
        self.name = name

class PQ_PhysicalQuantities(Component):
    def __init__(self, name: str, data: dict):
        self.name = name

class TS_PointInTime(Component):
    def __init__(self, name: str, data: dict):
        self.name = name

class IVL_Intervals(Component):
    def __init__(self, name: str, data: dict):
        self.name = name

class IVL_TS_IntervalOfTime(Component):
    def __init__(self, name: str, data: dict):
        self.name = name

class IVL_PQ_IntervalOfPhysicalQuantities(Component):
    def __init__(self, name: str, data: dict):
        self.name = name

class RTO_QTY_QTY_RatioOfQuantities(Component):
    def __init__(self, name: str, data: dict):
        self.name = name

