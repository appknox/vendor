import enum
import json


class PlatformEnum(enum.IntEnum):
    """
    Platform Type Enum
    """
    ANDROID = 0
    IOS = 1


class DeviceTypeEnum(enum.IntEnum):
    """
    Enum to detect device type
    """
    PHONE = 0
    TABLET = 1


def to_dict(enum_class):
    data = {}
    for attrib in dir(enum_class):

        if attrib.startswith('__'):
            continue
        attr = getattr(enum_class, attrib)
        data[attr.name] = attr.value
    return data


enums_dict = {}
enums = [PlatformEnum, DeviceTypeEnum]
for e in enums:
    enums_dict[e.__name__] = to_dict(e)

enums_json = json.dumps(enums_dict)
