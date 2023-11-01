from gettext import gettext as _

data = [
    # Reference: https://owasp.org/API-Security/editions/2023/en/0x11-t10/
    {
        "id": "API1_2023",
        "code": "API1:2023",
        "title": _("Broken Object Level Authorization"),
        "year": 2023,
        "active": True,
        "type": "api",
    },
    {
        "id": "API2_2023",
        "code": "API2:2023",
        "title": _("Broke Authentication"),
        "year": 2023,
        "active": True,
        "type": "api",
    },
    {
        "id": "API3_2023",
        "code": "API3:2023",
        "title": _("Broken Object Property Level Authorization"),
        "year": 2023,
        "active": True,
        "type": "api",
    },
    {
        "id": "API4_2023",
        "code": "API4:2023",
        "title": _("Unrestricted Resource Consumption"),
        "year": 2023,
        "active": True,
        "type": "api",
    },
    {
        "id": "API5_2023",
        "code": "API5:2023",
        "title": _("Broken Function Level Authorization"),
        "year": 2023,
        "active": True,
        "type": "api",
    },
    {
        "id": "API6_2023",
        "code": "API6:2023",
        "title": _("Unrestricted Access to Sensitive Business Flows"),
        "year": 2023,
        "active": True,
        "type": "api",
    },
    {
        "id": "API7_2023",
        "code": "API7:2023",
        "title": _("Server Side Request Forgery"),
        "year": 2023,
        "active": True,
        "type": "api",
    },
    {
        "id": "API8_2023",
        "code": "API8:2023",
        "title": _("Security Misconfiguration"),
        "year": 2023,
        "active": True,
        "type": "api",
    },
    {
        "id": "API9_2023",
        "code": "API9:2023",
        "title": _("Improper Inventory Management"),
        "year": 2023,
        "active": True,
        "type": "api",
    },
    {
        "id": "API10_2023",
        "code": "API10:2023",
        "title": _("Unsafe Consumption of APIs"),
        "year": 2023,
        "active": True,
        "type": "api",
    },
]


class OWASPAPI2023:
    def __init__(self, id, code, title, active=True, year=2023, type="api"):
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
        return "<OWASPAPI2023: %s>" % self.__str__()


OWASPAPI2023_DATA = {d["id"]: OWASPAPI2023(**d) for d in data}
