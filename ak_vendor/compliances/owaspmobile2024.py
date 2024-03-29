from gettext import gettext as _

data = [
    # Reference: https://owasp.org/www-project-mobile-top-10/
    {
        "id": "M1_2024",
        "code": "M1",
        "title": _("Improper Credential Usage"),
        "year": 2024,
        "active": True,
        "type": "mobile",
    },
    {
        "id": "M2_2024",
        "code": "M2",
        "title": _("Inadequate Supply Chain Security"),
        "year": 2024,
        "active": True,
        "type": "mobile",
    },
    {
        "id": "M3_2024",
        "code": "M3",
        "title": _("Insecure Authentication/Authorization"),
        "year": 2024,
        "active": True,
        "type": "mobile",
    },
    {
        "id": "M4_2024",
        "code": "M4",
        "title": _("Insufficient Input/Output Validation"),
        "year": 2024,
        "active": True,
        "type": "mobile",
    },
    {
        "id": "M5_2024",
        "code": "M5",
        "title": _("Insecure Communication"),
        "year": 2024,
        "active": True,
        "type": "mobile",
    },
    {
        "id": "M6_2024",
        "code": "M6",
        "title": _("Inadequate Privacy Controls"),
        "year": 2024,
        "active": True,
        "type": "mobile",
    },
    {
        "id": "M7_2024",
        "code": "M7",
        "title": _("Insufficient Binary Protections"),
        "year": 2024,
        "active": True,
        "type": "mobile",
    },
    {
        "id": "M8_2024",
        "code": "M8",
        "title": _("Security Misconfiguration"),
        "year": 2024,
        "active": True,
        "type": "mobile",
    },
    {
        "id": "M9_2024",
        "code": "M9",
        "title": _("Insecure Data Storage"),
        "year": 2024,
        "active": True,
        "type": "mobile",
    },
    {
        "id": "M10_2024",
        "code": "M10",
        "title": _("Insufficient Cryptography"),
        "year": 2024,
        "active": True,
        "type": "mobile",
    },
]


class OWASPMOBILE2024:
    def __init__(self, id, code, title, active=True, year=2024, type="mobile"):
        self.pk = id
        self.id = id
        self.title = title
        self.code = code
        self.year = year
        self.active = active
        self.type = type

    def __str__(self):
        return f"{self.id} - {self.code} - {self.title}"

    def __repr__(self):
        return "<OWASPMOBILE2024: %s>" % self.__str__()


OWASPMOBILE2024_DATA = {d["id"]: OWASPMOBILE2024(**d) for d in data}
