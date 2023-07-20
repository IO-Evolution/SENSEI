import unittest

import sys
import os.path

parent_folder = os.getcwd()
sys.path.append(parent_folder + '/src/FSE/CDA')

import cda_types as PrimitiveType  # nopep8
from exceptions import InvalidGivenValue, InvalidGivenSubelementData  # nopep8


class Test_BL_Boolean(unittest.TestCase):

    def test_required_KO_emptySet(self):
        self.assertRaises(InvalidGivenValue, PrimitiveType.BL_Boolean, "boolean", {})

    def test_required_KO_nonEmptySet(self):
        test_case = {
            "non_value": True
        }
        self.assertRaises(InvalidGivenValue, PrimitiveType.BL_Boolean, "boolean", test_case)

    def test_required_OK(self):
        test_case = {
            "value": True
        }
        obj = None
        try:
            obj = PrimitiveType.BL_Boolean("boolean", test_case)
        except Exception as error:
            self.fail("Raised exception")

        self.assertEqual("boolean", obj.name)
        self.assertEqual(test_case["value"], obj.value)


class Test_II_InstanceIdentifier(unittest.TestCase):
    def test_required_KO_emptySet(self):
        self.assertRaises(InvalidGivenValue, PrimitiveType.II_InstanceIdentifier, "id", {})

    def test_required_KO_nonEmptySet_noOptional(self):
        test_case = {
            "non_root": "0.0.0.0"
        }
        self.assertRaises(InvalidGivenValue, PrimitiveType.II_InstanceIdentifier, "id", test_case)

    def test_required_OK(self):
        test_case = {
            "root": "1.2.3.4"
        }
        obj = None
        try:
            obj = PrimitiveType.II_InstanceIdentifier("id", test_case)
        except Exception as error:
            self.fail("Raised exception")

        self.assertEqual("id", obj.name)
        self.assertEqual(test_case["root"], obj.root)
        self.assertIsNone(obj.extension)

    def test_optional_full(self):
        test_case = {
            "root": "1.2.3.4",
            "extension": "123456789"
        }
        obj = None
        try:
            obj = PrimitiveType.II_InstanceIdentifier("id", test_case)
        except Exception as error:
            self.fail("Raised exception")

        self.assertEqual("id", obj.name)
        self.assertEqual(test_case["root"], obj.root)
        self.assertEqual(test_case["extension"], obj.extension)


class Test_ED_EncapsulatedData(unittest.TestCase):
    def test_required_KO_emptySet(self):
        self.assertRaises(InvalidGivenValue, PrimitiveType.ED_EncapsulatedData, "data", {})

    def test_required_KO_text(self):
        test_case = {
            "mediaType": "H",
            "representation": "isdaiosuda908798sd798a7sd897987=="
        }
        self.assertRaises(InvalidGivenValue, PrimitiveType.ED_EncapsulatedData, "data", test_case)

    def test_required_OK_text(self):
        test_case = {
            "mediaType": "H",
            "representation": "isdaiosuda908798sd798a7sd897987==",
            "text": "prova test"
        }
        obj = None
        try:
            obj = PrimitiveType.ED_EncapsulatedData("data", test_case)
        except Exception as error:
            self.fail("Raised exception")

        self.assertEqual("data", obj.name)
        self.assertEqual(test_case["mediaType"], obj.mediaType)
        self.assertEqual(test_case["representation"], obj.representation)
        self.assertEqual(test_case["text"], obj.text)

    def test_required_OK_nonText(self):
        test_case = {
            "mediaType": "H",
            "representation": "isdaiosuda908798sd798a7sd897987==",
            "reference": {
                "value": "referencegood"
            }
        }
        obj = None
        try:
            obj = PrimitiveType.ED_EncapsulatedData("data", test_case)
        except Exception as error:
            self.fail("Raised exception")

        self.assertEqual("data", obj.name)
        self.assertEqual(test_case["mediaType"], obj.mediaType)
        self.assertEqual(test_case["representation"], obj.representation)
        self.assertIsNotNone(obj.reference)

    def test_optional_full_basic(self):
        test_case = {
            "mediaType": "H",
            "representation": "isdaiosuda908798sd798a7sd897987==",
            "reference": {
                "value": "referencegood"
            },
            "thumbnail": {
                "mediaType": "foto",
                "text": "asidjaoijdoiwjiojioj=="
            }
        }
        obj = None
        try:
            obj = PrimitiveType.ED_EncapsulatedData("data", test_case)
        except Exception as error:
            self.fail("Raised exception")

        self.assertEqual("data", obj.name)
        self.assertEqual(test_case["mediaType"], obj.mediaType)
        self.assertEqual(test_case["representation"], obj.representation)
        self.assertEqual(PrimitiveType.TEL_TelecomincationAddress, type(obj.reference))
        self.assertEqual(PrimitiveType.ED_EncapsulatedData, type(obj.thumbnail))

    def test_optional_full_list(self):
        test_case = {
            "mediaType": "H",
            "representation": "isdaiosuda908798sd798a7sd897987==",
            "reference": [
                {
                    "value": "1"
                },
                {
                    "value": "2"
                },
                {
                    "value": "3"
                },
                {
                    "value": "4"
                }
            ],
            "thumbnail": [
                {
                    "mediaType": "foto2",
                    "text": "asidjaoijdoiwjiojioj=="
                },
                {
                    "mediaType": "foto2",
                    "text": "asidjaoijdoiwjiojioj=="
                },
            ]
        }
        obj = None
        try:
            obj = PrimitiveType.ED_EncapsulatedData("data", test_case)
        except Exception as error:
            self.fail("Raised exception")

        self.assertEqual("data", obj.name)
        self.assertEqual(test_case["mediaType"], obj.mediaType)
        self.assertEqual(test_case["representation"], obj.representation)
        self.assertIsNotNone(obj.reference)
        self.assertIsNotNone(obj.thumbnail)
        self.assertEqual(len(test_case["reference"]), len(obj.reference))
        self.assertEqual(len(test_case["thumbnail"]), len(obj.thumbnail))
        self.assertEqual(PrimitiveType.TEL_TelecomincationAddress, type(obj.reference[0]))
        self.assertEqual(PrimitiveType.ED_EncapsulatedData, type(obj.thumbnail[0]))


class Test_ST_String(unittest.TestCase):
    def test_required_KO_emptySet(self):
        self.assertRaises(InvalidGivenValue, PrimitiveType.ST_String, "string", {})

    def test_required_KO_nonEmptySet(self):
        test_case = {
            "non_text": "googd"
        }
        self.assertRaises(InvalidGivenValue, PrimitiveType.ST_String, "string", test_case)

    def test_required_OK(self):
        test_case = {
            "text": True
        }
        obj = None
        try:
            obj = PrimitiveType.ST_String("string", test_case)
        except Exception as error:
            self.fail("Raised exception")

        self.assertEqual("string", obj.name)
        self.assertEqual(test_case["text"], obj.text)


class Test_CD_ConceptDescriptor(unittest.TestCase):
    def test_required_KO_emptySet(self):
        self.assertRaises(InvalidGivenValue, PrimitiveType.CD_ConceptDescriptor, "concept", {})

    def test_required_KO_nonEmptySet_noOptional(self):
        test_case = {
            "non_code": "0.0.0.0",
            "non_codeSystem": "LOINC"
        }
        self.assertRaises(InvalidGivenValue, PrimitiveType.CD_ConceptDescriptor, "concept", test_case)

    def test_required_OK(self):
        test_case = {
            "code": "1.2.3.4",
            "codeSystem": "LOINC"
        }
        obj = None
        try:
            obj = PrimitiveType.CD_ConceptDescriptor("concept", test_case)
        except Exception as error:
            self.fail("Raised exception")

        self.assertEqual("concept", obj.name)
        self.assertEqual(test_case["code"], obj.code)
        self.assertEqual(test_case["codeSystem"], obj.codeSystem)

    def test_optional_full_basic(self):
        test_case = {
            "code": "1.2.3.4",
            "codeSystem": "LOINC",
            "codeSystemVersion": "LOINC",
            "displayName": "LOINC",
            "originalText": {
                "text": "testo originale"
            },
            "translaction": {
                "code": "1.1.1.1",
                "codeSystem": "LOINC"
            },
            "qualifier": "QUALIFIER"
        }
        obj = None
        try:
            obj = PrimitiveType.CD_ConceptDescriptor("concept", test_case)
        except Exception as error:
            self.fail("Raised exception")

        self.assertEqual("concept", obj.name)
        self.assertEqual(test_case["code"], obj.code)
        self.assertEqual(test_case["codeSystem"], obj.codeSystem)
        self.assertEqual(test_case["codeSystemVersion"], obj.codeSystemVersion)
        self.assertEqual(test_case["displayName"], obj.displayName)
        self.assertEqual(test_case["qualifier"], obj.qualifier)
        self.assertEqual(PrimitiveType.ST_String, type(obj.originalText))
        self.assertEqual(PrimitiveType.CD_ConceptDescriptor, type(obj.translaction))

    def test_optional_full_list(self):
        test_case = {
            "code": "1.2.3.4",
            "codeSystem": "LOINC",
            "codeSystemVersion": "LOINC",
            "displayName": "LOINC",
            "originalText": [
                {
                    "text": "testo originale"
                },
                {
                    "text": "testo originale"
                },
                {
                    "text": "testo originale"
                },
                {
                    "text": "testo originale"
                }
            ],
            "translaction": [
                {
                    "code": "1.1.1.1",
                    "codeSystem": "LOINC"
                },
                {
                    "code": "1.1.1.1",
                    "codeSystem": "LOINC"
                },
                {
                    "code": "1.1.1.1",
                    "codeSystem": "LOINC"
                }
            ],
            "qualifier": "QUALIFIER"
        }
        obj = None
        try:
            obj = PrimitiveType.CD_ConceptDescriptor("concept", test_case)
        except Exception as error:
            self.fail("Raised exception")

        self.assertEqual("concept", obj.name)
        self.assertEqual(test_case["code"], obj.code)
        self.assertEqual(test_case["codeSystem"], obj.codeSystem)
        self.assertEqual(test_case["codeSystemVersion"], obj.codeSystemVersion)
        self.assertEqual(test_case["displayName"], obj.displayName)
        self.assertEqual(test_case["qualifier"], obj.qualifier)
        self.assertIsNotNone(obj.originalText)
        self.assertIsNotNone(obj.translaction)
        self.assertEqual(len(test_case["originalText"]), len(obj.originalText))
        self.assertEqual(len(test_case["translaction"]), len(obj.translaction))
        self.assertEqual(PrimitiveType.ST_String, type(obj.originalText[0]))
        self.assertEqual(PrimitiveType.CD_ConceptDescriptor, type(obj.translaction[0]))


class Test_CE_CodedWithEquivalents(unittest.TestCase):
    def test_required_KO_emptySet(self):
        self.assertRaises(InvalidGivenValue, PrimitiveType.CE_CodedWithEquivalents, "concept", {})

    def test_required_KO_nonEmptySet_noOptional(self):
        test_case = {
            "non_code": "0.0.0.0",
            "non_codeSystem": "LOINC"
        }
        self.assertRaises(InvalidGivenValue, PrimitiveType.CE_CodedWithEquivalents, "concept", test_case)

    def test_required_OK(self):
        test_case = {
            "code": "1.2.3.4",
            "codeSystem": "LOINC"
        }
        obj = None
        try:
            obj = PrimitiveType.CE_CodedWithEquivalents("concept", test_case)
        except Exception as error:
            self.fail("Raised exception")

        self.assertEqual("concept", obj.name)
        self.assertEqual(test_case["code"], obj.code)
        self.assertEqual(test_case["codeSystem"], obj.codeSystem)

    def test_optional_full_basic(self):
        test_case = {
            "code": "1.2.3.4",
            "codeSystem": "LOINC",
            "codeSystemVersion": "LOINC",
            "displayName": "LOINC",
            "originalText": {
                "text": "testo originale"
            },
            "translaction": {
                "code": "1.1.1.1",
                "codeSystem": "LOINC"
            }
        }
        obj = None
        try:
            obj = PrimitiveType.CE_CodedWithEquivalents("concept", test_case)
        except Exception as error:
            self.fail("Raised exception")

        self.assertEqual("concept", obj.name)
        self.assertEqual(test_case["code"], obj.code)
        self.assertEqual(test_case["codeSystem"], obj.codeSystem)
        self.assertEqual(test_case["codeSystemVersion"], obj.codeSystemVersion)
        self.assertEqual(test_case["displayName"], obj.displayName)
        self.assertEqual(PrimitiveType.ST_String, type(obj.originalText))
        self.assertEqual(PrimitiveType.CD_ConceptDescriptor, type(obj.translaction))

    def test_optional_full_list(self):
        test_case = {
            "code": "1.2.3.4",
            "codeSystem": "LOINC",
            "codeSystemVersion": "LOINC",
            "displayName": "LOINC",
            "originalText": [
                {
                    "text": "testo originale"
                },
                {
                    "text": "testo originale"
                },
                {
                    "text": "testo originale"
                },
                {
                    "text": "testo originale"
                }
            ],
            "translaction": [
                {
                    "code": "1.1.1.1",
                    "codeSystem": "LOINC"
                },
                {
                    "code": "1.1.1.1",
                    "codeSystem": "LOINC"
                },
                {
                    "code": "1.1.1.1",
                    "codeSystem": "LOINC"
                }
            ]
        }
        obj = None
        try:
            obj = PrimitiveType.CE_CodedWithEquivalents("concept", test_case)
        except Exception as error:
            self.fail("Raised exception")

        self.assertEqual("concept", obj.name)
        self.assertEqual(test_case["code"], obj.code)
        self.assertEqual(test_case["codeSystem"], obj.codeSystem)
        self.assertEqual(test_case["codeSystemVersion"], obj.codeSystemVersion)
        self.assertEqual(test_case["displayName"], obj.displayName)
        self.assertIsNotNone(obj.originalText)
        self.assertIsNotNone(obj.translaction)
        self.assertEqual(len(test_case["originalText"]), len(obj.originalText))
        self.assertEqual(len(test_case["translaction"]), len(obj.translaction))
        self.assertEqual(PrimitiveType.ST_String, type(obj.originalText[0]))
        self.assertEqual(PrimitiveType.CD_ConceptDescriptor, type(obj.translaction[0]))


class Test_CV_CodedValue(unittest.TestCase):
    def test_required_KO_emptySet(self):
        self.assertRaises(InvalidGivenValue, PrimitiveType.CV_CodedValue, "concept", {})

    def test_required_KO_nonEmptySet_noOptional(self):
        test_case = {
            "non_code": "0.0.0.0",
            "non_codeSystem": "LOINC"
        }
        self.assertRaises(InvalidGivenValue, PrimitiveType.CV_CodedValue, "concept", test_case)

    def test_required_OK(self):
        test_case = {
            "code": "1.2.3.4",
            "codeSystem": "LOINC"
        }
        obj = None
        try:
            obj = PrimitiveType.CV_CodedValue("concept", test_case)
        except Exception as error:
            self.fail("Raised exception")

        self.assertEqual("concept", obj.name)
        self.assertEqual(test_case["code"], obj.code)
        self.assertEqual(test_case["codeSystem"], obj.codeSystem)

    def test_optional_full_basic(self):
        test_case = {
            "code": "1.2.3.4",
            "codeSystem": "LOINC",
            "codeSystemVersion": "LOINC",
            "displayName": "LOINC",
            "originalText": {
                "text": "testo originale"
            }
        }
        obj = None
        try:
            obj = PrimitiveType.CV_CodedValue("concept", test_case)
        except Exception as error:
            self.fail("Raised exception")

        self.assertEqual("concept", obj.name)
        self.assertEqual(test_case["code"], obj.code)
        self.assertEqual(test_case["codeSystem"], obj.codeSystem)
        self.assertEqual(test_case["codeSystemVersion"], obj.codeSystemVersion)
        self.assertEqual(test_case["displayName"], obj.displayName)
        self.assertEqual(PrimitiveType.ST_String, type(obj.originalText))

    def test_optional_full_list(self):
        test_case = {
            "code": "1.2.3.4",
            "codeSystem": "LOINC",
            "codeSystemVersion": "LOINC",
            "displayName": "LOINC",
            "originalText": [
                {
                    "text": "testo originale"
                },
                {
                    "text": "testo originale"
                },
                {
                    "text": "testo originale"
                },
                {
                    "text": "testo originale"
                }
            ]
        }
        obj = None
        try:
            obj = PrimitiveType.CV_CodedValue("concept", test_case)
        except Exception as error:
            self.fail("Raised exception")

        self.assertEqual("concept", obj.name)
        self.assertEqual(test_case["code"], obj.code)
        self.assertEqual(test_case["codeSystem"], obj.codeSystem)
        self.assertEqual(test_case["codeSystemVersion"], obj.codeSystemVersion)
        self.assertEqual(test_case["displayName"], obj.displayName)
        self.assertIsNotNone(obj.originalText)
        self.assertEqual(len(test_case["originalText"]), len(obj.originalText))
        self.assertEqual(PrimitiveType.ST_String, type(obj.originalText[0]))


class Test_CS_CodedSimpleValue(unittest.TestCase):
    def test_required_KO_emptySet(self):
        self.assertRaises(InvalidGivenValue, PrimitiveType.CS_CodedSimpleValue, "concept", {})

    def test_required_KO_nonEmptySet_noOptional(self):
        test_case = {
            "non_code": "0.0.0.0",
        }
        self.assertRaises(InvalidGivenValue, PrimitiveType.CS_CodedSimpleValue, "concept", test_case)

    def test_required_OK(self):
        test_case = {
            "code": "1.2.3.4",
        }
        obj = None
        try:
            obj = PrimitiveType.CS_CodedSimpleValue("concept", test_case)
        except Exception as error:
            self.fail("Raised exception")

        self.assertEqual("concept", obj.name)
        self.assertEqual(test_case["code"], obj.code)


class Test_TEL_TelecomincationAddress(unittest.TestCase):
    def test_required_KO_emptySet(self):
        self.assertRaises(InvalidGivenValue, PrimitiveType.TEL_TelecomincationAddress, "telecomunication", {})

    def test_required_KO_nonEmptySet_noOptional(self):
        test_case = {
            "non_value": "mail@email.it",
        }
        self.assertRaises(InvalidGivenValue, PrimitiveType.TEL_TelecomincationAddress, "telecomunication", test_case)

    def test_required_OK(self):
        test_case = {
            "value": "mail@email.it",
        }
        obj = None
        try:
            obj = PrimitiveType.TEL_TelecomincationAddress("telecomunication", test_case)
        except Exception as error:
            self.fail("Raised exception")

        self.assertEqual("telecomunication", obj.name)
        self.assertEqual(test_case["value"], obj.value)

    def test_optional_full_basic(self):
        test_case = {
            "value": "mail@email.it",
            "use": "H",
            "useablePeriod": {
                "high": {
                    "value": "top"
                }
            }
        }
        obj = None
        try:
            obj = PrimitiveType.TEL_TelecomincationAddress("telecomunication", test_case)
        except Exception as error:
            self.fail("Raised exception")

        self.assertEqual("telecomunication", obj.name)
        self.assertEqual(test_case["value"], obj.value)
        self.assertEqual(test_case["use"], obj.use)
        self.assertIsNotNone(obj.useablePeriod)
        self.assertEqual(PrimitiveType.IVL_TS_IntervalOfTime, type(obj.useablePeriod))

    def test_optional_KO_list(self):
        test_case = {
            "value": "mail@email.it",
            "use": "H",
            "useablePeriod": [
                {
                    "high": {
                        "value": "top"
                    }
                },
                {
                    "high": {
                        "value": "top"
                    }
                }
            ]
        }
        obj = None
        try:
            obj = PrimitiveType.TEL_TelecomincationAddress("telecomunication", test_case)
        except Exception as error:
            self.fail("Raised exception")

        self.assertEqual("telecomunication", obj.name)
        self.assertEqual(test_case["value"], obj.value)
        self.assertEqual(test_case["use"], obj.use)
        self.assertIsNone(obj.useablePeriod)


class Test_AD_PostalAddress(unittest.TestCase):
    def test_required_KO_emptySet(self):
        self.assertRaises(InvalidGivenValue, PrimitiveType.AD_PostalAddress, "address", {})

    def test_optional_full_basic(self):
        test_case = {
            "use": "H",
            "streetAddressLine": {
                "text": "via bla bla"
            },
            "city": {
                "text": "Spezi"
            },
            "postalCode": {
                "text": "123456"
            },
            "country": {
                "text": "Italy"
            },
        }
        obj = None
        try:
            obj = PrimitiveType.AD_PostalAddress("address", test_case)
        except Exception as error:
            self.fail("Raised exception")

        self.assertEqual("address", obj.name)
        self.assertEqual(test_case["use"], obj.use)
        self.assertIsNotNone(obj.streetAddressLine)
        self.assertIsNotNone(obj.city)
        self.assertIsNotNone(obj.postalCode)
        self.assertIsNotNone(obj.country)
        self.assertEqual(PrimitiveType.ST_String, type(obj.streetAddressLine))
        self.assertEqual(PrimitiveType.ST_String, type(obj.city))
        self.assertEqual(PrimitiveType.ST_String, type(obj.postalCode))
        self.assertEqual(PrimitiveType.ST_String, type(obj.country))

    def test_optional_KO_list(self):
        test_case = {
            "use": "H",
            "streetAddressLine": [
                {
                    "text": "via bla bla"
                },
                {
                    "text": "via bla bla"
                }
            ],
            "city": [
                {
                    "text": "SPEZIA"
                },
                {
                    "text": "SPEZIA"
                }
            ],
            "postalCode": [
                {
                    "text": "123456"
                },
                {
                    "text": "123456"
                }
            ],
            "country": [
                {
                    "text": "ITALY"
                },
                {
                    "text": "ITALY"
                }
            ],
        }
        obj = None
        try:
            obj = PrimitiveType.AD_PostalAddress("address", test_case)
        except Exception as error:
            self.fail("Raised exception")

        self.assertEqual("address", obj.name)
        self.assertEqual(test_case["use"], obj.use)
        self.assertIsNone(obj.streetAddressLine)
        self.assertIsNone(obj.city)
        self.assertIsNone(obj.postalCode)
        self.assertIsNone(obj.country)


class Test_PN_PersonName(unittest.TestCase):
    pass


class Test_ON_OrganisationName(unittest.TestCase):
    pass


class Test_INT_IntegerNumber(unittest.TestCase):
    pass


class Test_PQ_PhysicalQuantities(unittest.TestCase):
    pass


class Test_TS_PointInTime(unittest.TestCase):
    pass


class Test_IVL_TS_IntervalOfTime(unittest.TestCase):
    pass


class Test_IVL_PQ_IntervalOfPhysicalQuantities(unittest.TestCase):
    pass


class Test_RTO_QTY_QTY_RatioOfQuantities(unittest.TestCase):
    pass
