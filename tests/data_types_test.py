import unittest

import sys
import os.path

parent_folder = os.getcwd()
sys.path.append(parent_folder + '/src/FSE/CDA')

import data_types as el
from exceptions import InvalidGivenValue, InvalidGivenSubelementData

class Test_BL_Boolean(unittest.TestCase):
    print("OK")

class Test_II_InstanceIdentifier(unittest.TestCase):
    pass

class Test_ED_EncapsulatedData(unittest.TestCase):
    pass

class Test_ST_String(unittest.TestCase):
    pass

class Test_CD_ConceptDescriptor(unittest.TestCase):
    pass

class Test_CE_CodedWithEquivalents(unittest.TestCase):
    pass

class Test_CV_CodedValue(unittest.TestCase):
    pass

class Test_CS_CodedSimpleValue(unittest.TestCase):
    pass

class Test_TEL_TelecomincationAddress(unittest.TestCase):
    pass

class Test_AD_PostalAddress(unittest.TestCase):
    pass

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
