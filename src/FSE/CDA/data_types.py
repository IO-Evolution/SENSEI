import elements as el
from exceptions import InvalidGivenValue, InvalidGivenSubelementData


class Component:
    name: str
    value: str


class BL_Boolean(Component):
    def __init__(self, name: str, data):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name
        self.value = el.Attribute("value", data, required=True)


class II_InstanceIdentifier(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name
        self.root = el.Attribute("root", data, required=True)
        self.extension = el.Attribute("extension", data)


class ED_EncapsulatedData(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.mediaType = el.Attribute("mediaType", data)
        self.representation = el.Attribute("representation", data)

        self.reference = el.Component(TEL_TelecomincationAddress, "reference", data)
        self.thumbnail = el.Component(ED_EncapsulatedData, "thumbnail", data)

        if self.reference is None and self.thumbnail is None:
            try:
                self.text = data["text"]
            except:
                raise InvalidGivenValue("Text Needed")


class ST_String(Component):
    def __init__(self, name: str, data: str):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name
        try:
            self.text = data["text"]
        except:
            raise InvalidGivenValue("Text Needed")


class CD_ConceptDescriptor(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.code = el.Attribute("code", data, required=True)
        self.codeSystem = el.Attribute("codeSystem", data, required=True)
        self.codeSystemVersion = el.Attribute("codeSystemVersion", data)
        self.displayName = el.Attribute("displayName", data)
        self.originalText = el.Component(ST_String, "originalText", data)
        self.translaction = el.Component(CD_ConceptDescriptor, "translaction", data)
        self.qualifier = el.Attribute("qualifier", data)


class CE_CodedWithEquivalents(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.code = el.Attribute("code", data, required=True)
        self.codeSystem = el.Attribute("codeSystem", data, required=True)
        self.codeSystemVersion = el.Attribute("codeSystemVersion", data)
        self.displayName = el.Attribute("displayName", data)
        self.originalText = el.Component(ST_String, "originalText", data)
        self.translaction = el.Component(CD_ConceptDescriptor, "translaction", data)


class CV_CodedValue(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.code = el.Attribute("code", data, required=True)
        self.codeSystem = el.Attribute("codeSystem", data, required=True)
        self.codeSystemVersion = el.Attribute("codeSystemVersion", data)
        self.displayName = el.Attribute("displayName", data)
        self.originalText = el.Component(ST_String, "originalText", data)


class CS_CodedSimpleValue(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.code = el.Attribute("code", data, required=True)


class TEL_TelecomincationAddress(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.value = el.Attribute("value", data, required=True)
        self.use = el.Attribute("use", data)

        """
            value:
            telephone (tel:)
            fax (fax:)
            email (mailto:)

            use:
            H: home
            WP: Work
            MC: mobile phone
        """

        self.useablePeriod = el.Component("useablePeriod", IVL_TS_IntervalOfTime, data)


class AD_PostalAddress(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.use = el.Attribute("use", data)

        self.streetAddressLine = el.Component("streetAddressLine", ST_String, data)
        self.city = el.Component("streetAddressLine", ST_String, data)
        self.postalCode = el.Component("streetAddressLine", ST_String, data)
        self.country = el.Component("streetAddressLine", ST_String, data)

        """
        https://wiki.hl7.de/index.php?title=HL7_CDA_Core_Principles#Postal_Address_.28AD.29
        """


class PN_PersonName(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.given = el.Component("given", ST_String, data)
        self.family = el.Component("family", ST_String, data)
        self.validTime = el.Component("validTime", IVL_TS_IntervalOfTime, data)


class ON_OrganisationName(Component):
    def __init__(self, name: str, data: str):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name
        try:
            self.text = data["text"]
        except:
            raise InvalidGivenValue("Text Needed")

        # self.validTime = el.Component("validTime", IVL_TS_IntervalOfTime, data)
        """ ????
            <name>The old hospital
                <validTime> 
                    <high value="20111231235959"/>
                </validTime>
            </name>
        """


class INT_IntegerNumber(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.value = el.Attribute("value", data, required=True)


class PQ_PhysicalQuantities(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.value = el.Attribute("value", data, required=True)
        self.unit = el.Attribute("unit", data, required=True)


class TS_PointInTime(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.value = el.Attribute("value", data, required=True)

# class IVL_Intervals(Component):
#     def __init__(self, name: str, data: dict):
# if data == {} or data is None:
#  raise InvalidGivenValue("Empty Data Set")
#
# self.name = name


class IVL_TS_IntervalOfTime(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.low = el.Component("low", INT_IntegerNumber, data)
        self.high = el.Component("high", INT_IntegerNumber, data)
        self.center = el.Component("center", INT_IntegerNumber, data)
        self.width = el.Component("width", PQ_PhysicalQuantities, data)


class IVL_PQ_IntervalOfPhysicalQuantities(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.low = el.Component("low", INT_IntegerNumber, data)
        self.high = el.Component("high", INT_IntegerNumber, data)
        self.center = el.Component("center", INT_IntegerNumber, data)


class RTO_QTY_QTY_RatioOfQuantities(Component):
    def __init__(self, name: str, data: dict):
        if data == {} or data is None:
            raise InvalidGivenValue("Empty Data Set")

        self.name = name

        self.numerator = el.Component("numerator", PQ_PhysicalQuantities, data)
        if "unit" in data["denominator"]:
            self.denominator = el.Component("denominator", PQ_PhysicalQuantities, data)
        else:
            self.denominator = el.Component("denominator", INT_IntegerNumber, data)
