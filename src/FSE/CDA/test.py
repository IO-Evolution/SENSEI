import cda_types as Type
import elements as Element

test = {
    "prova": {
        "extension": "1234567689"
    }
}

# print(Element.Component(Type.InfrastructureRootTypeId, "prova", test, required=True, as_list=False).root)
# print(Element.Component(Type.InfrastructureRootTypeId, "prova", test, required=True, as_list=False).extension)

print(Type.AD_PostalAddress.as_dict())