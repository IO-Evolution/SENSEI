from dataclasses import dataclass

class InvalidGivenValue(Exception):
    """ One or more given value is invalid """
    pass

class Attribute():
    """ XML Attributes structures """
    required: bool
    name: str
    value: str

    def __new__(cls, name: str, data: dict, required: bool = True):
        instance = super().__new__(cls)
        try:
            instance.name = name
            instance.value = data[name]
            instance.required = required
            return instance
        except Exception:
            if required:
                raise InvalidGivenValue
            return None

class Sub():
    """ XML Element structures """
    def __new__(cls, className: type, name: str, data: dict, required: bool = True):
        
        try:
            instance = className(name, data, required)
            return instance
        except Exception as error:
            if required:
                raise error
            return None

class Value():
    """ XML Element structures """
    pass
