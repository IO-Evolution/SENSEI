from .exceptions import InvalidGivenValue, InvalidGivenSubelementData

class Attribute:
    """ XML Attributes Class """
    def __new__(cls, name: str, data: dict, required: bool = False, fixed: str = None):
        try:
            if fixed == None:
                return data[name]
            else:
                return data[name] if data[name] == fixed else None
        except Exception as error:
            if required:
                raise InvalidGivenValue(f"Something went wrong generating {name}") from error
            return None


class Component:
    """ XML Component Class """
    def __new__(cls, className: type, name: str, data: dict, required: bool = False, as_list: bool = True):
        try:
            # if type(className) == PrimitiveType:
            if type(data[name]) == dict:
                return className(name, data[name])
            elif type(data[name]) == list and as_list:
                return [className(name, elem) for elem in data[name]]
            else:
                if type(data[name]) == list and as_list:
                    raise InvalidGivenSubelementData(f"{name} of type {className.__class__} can't be listed")
                else:  
                    raise InvalidGivenSubelementData(f"{name} of type {className.__class__} must be dict or list")
            # elif type(className) == ComplexType:
            #     if type(data[name]) == dict:
            #         return className(name, data[name])
            #     elif type(data[name]) == list and as_list:
            #         return [className(name, elem) for elem in data[name]]
            #     else:
            #         if type(data[name]) == list and as_list:
            #             raise InvalidGivenSubelementData(f"{name} of type {className.__class__} can't be listed")
            #         else:  
            #             raise InvalidGivenSubelementData(f"{name} of type {className.__class__} must be dict or list")
        except Exception as error:
            if required:
                raise InvalidGivenSubelementData(f"Something went wrong generating {name} of type {className.__class__}") from error
            return None
