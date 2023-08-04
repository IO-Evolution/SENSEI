import xml.etree.ElementTree as ET


class Factory:
    """FACTORY"""
    def __init__(self, root_name: str, data: dict):
        self.root_name = root_name
        self.dict_data = data

    def dict_to_xml(self):
        """dict_to_xml"""
        root = ET.Element(self.root_name)
        self._dict_to_xml(root, self.dict_data)
        ET.indent(root, space="\t", level=0)
        return ET.tostring(root, encoding='utf-8').decode()

    def _dict_to_xml(self, node, data: dict):
        for key, value in data.items():
            if isinstance(value, dict):
                if "text" in value and len(value) == 1:
                    subnode = ET.SubElement(node, key)
                    subnode.text = str(value["text"])
                else:
                    subnode = ET.Element(key)
                    node.append(subnode)
                    self._dict_to_xml(subnode, value)
            else:
                subnode = ET.SubElement(node, key)
                subnode.text = f"dato di {key}"

    def save_dict_to_xml(self, filename: str):
        """save_dict_to_xml"""
        xml_string = self.dict_to_xml()
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(xml_string)


test = {
    "realmCode": {
        "code": ""
    },
    "typeId": {
        "root": "",
        "extension": ""
    },
    "templateId": {
        "root": "",
        "extension": ""
    },
    "id": {
        "root": "",
        "extension": ""
    },
    "name": {
        "family": {
            "text": ""
        },
        "given": {
            "text": ""
        },
        "validTime": {
            "low": {
                "value": ""
            },
            "high": {
                "value": ""
            },
            "center": {
                "value": ""
            },
            "width": {
                "value": "",
                "unit": ""
            }
        }
    },
    "administrativeGenderCode": {
        "code": "",
        "codeSystem": "",
        "codeSysteVersion": "",
        "displayName": "",
        "originalText": {
            "text": ""
        },
        "translaction": {
            "code": "",
            "codeSystem": "",
            "codeSysteVersion": "",
            "displayName": "",
            "originalText": {
                "text": ""
            },
            "translaction": "RECURSIVE",
            "qualifier": ""
        }
    },
    "birthTime": {
        "value": ""
    },
    "maritalStatusCode": {
        "code": "",
        "codeSystem": "",
        "codeSysteVersion": "",
        "displayName": "",
        "originalText": {
            "text": ""
        },
        "translaction": {
            "code": "",
            "codeSystem": "",
            "codeSysteVersion": "",
            "displayName": "",
            "originalText": {
                "text": ""
            },
            "translaction": "RECURSIVE",
            "qualifier": ""
        }
    },
    "religiousAfflitionCode": {
        "code": "",
        "codeSystem": "",
        "codeSysteVersion": "",
        "displayName": "",
        "originalText": {
            "text": ""
        },
        "translaction": {
            "code": "",
            "codeSystem": "",
            "codeSysteVersion": "",
            "displayName": "",
            "originalText": {
                "text": ""
            },
            "translaction": "RECURSIVE",
            "qualifier": ""
        }
    },
    "raceCode": {
        "code": "",
        "codeSystem": "",
        "codeSysteVersion": "",
        "displayName": "",
        "originalText": {
            "text": ""
        },
        "translaction": {
            "code": "",
            "codeSystem": "",
            "codeSysteVersion": "",
            "displayName": "",
            "originalText": {
                "text": ""
            },
            "translaction": "RECURSIVE",
            "qualifier": ""
        }
    },
    "ethnicGroupCode": {
        "code": "",
        "codeSystem": "",
        "codeSysteVersion": "",
        "displayName": "",
        "originalText": {
            "text": ""
        },
        "translaction": {
            "code": "",
            "codeSystem": "",
            "codeSysteVersion": "",
            "displayName": "",
            "originalText": {
                "text": ""
            },
            "translaction": "RECURSIVE",
            "qualifier": ""
        }
    },
    "guardian": {
        "realmCode": {
            "code": ""
        },
        "typeId": {
            "root": "",
            "extension": ""
        },
        "templateId": {
            "root": "",
            "extension": ""
        },
        "id": {
            "root": "",
            "extension": ""
        },
        "code": {
            "code": "",
            "codeSystem": "",
            "codeSysteVersion": "",
            "displayName": "",
            "originalText": {
                "text": ""
            },
            "translaction": {
                "code": "",
                "codeSystem": "",
                "codeSysteVersion": "",
                "displayName": "",
                "originalText": {
                    "text": ""
                },
                "translaction": "RECURSIVE",
                "qualifier": ""
            }
        },
        "addr": {
            "use": "",
            "steedAddressLine": {
                "text": ""
            },
            "city": {
                "text": ""
            },
            "postalCode": {
                "text": ""
            },
            "country": {
                "text": ""
            }
        },
        "telecom": {
            "value": "",
            "use": "",
            "useablePeriod": {
                "low": {
                    "value": ""
                },
                "high": {
                    "value": ""
                },
                "center": {
                    "value": ""
                },
                "width": {
                    "value": "",
                    "unit": ""
                }
            }
        },
        "guardianPerson": {

        },
        "guardianOrganization": {

        },
        "classCode": ""
    },
    "birthplace": {

    },
    "languageCommunication": {

    },
    "classCode": "",
    "determinerCode": ""
}

fact = Factory("ClinicalDocument", test)
# print(fact.dict_to_xml())
fact.save_dict_to_xml("prova.xml")
