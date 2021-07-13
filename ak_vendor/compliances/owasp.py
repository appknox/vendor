from gettext import gettext as _


data = [
    {
        "id": "M1_2016",
        "code": "M1",
        "title": _("Improper Platform Usage"),
        "year": 2016,
        "active": True,
        "type": "mobile",
    },
    {
        "id": "M2_2016",
        "code": "M2",
        "title": _("Insecure Data Storage"),
        "year": 2016,
        "active": True,
        "type": "mobile",
    },
    {
        "id": "M3_2016",
        "code": "M3",
        "title": _("Insecure Communication"),
        "year": 2016,
        "active": True,
        "type": "mobile",
    },
    {
        "id": "M4_2016",
        "code": "M4",
        "title": _("Insecure Authentication"),
        "year": 2016,
        "active": True,
        "type": "mobile",
    },
    {
        "id": "M5_2016",
        "code": "M5",
        "title": _("Insufficient Cryptography"),
        "year": 2016,
        "active": True,
        "type": "mobile",
    },
    {
        "id": "M6_2016",
        "code": "M6",
        "title": _("Insecure Authorization"),
        "year": 2016,
        "active": True,
        "type": "mobile",
    },
    {
        "id": "M7_2016",
        "code": "M7",
        "title": _("Client Code Quality"),
        "year": 2016,
        "active": True,
        "type": "mobile",
    },
    {
        "id": "M8_2016",
        "code": "M8",
        "title": _("Code Tampering"),
        "year": 2016,
        "active": True,
        "type": "mobile",
    },
    {
        "id": "M9_2016",
        "code": "M9",
        "title": _("Reverse Engineering"),
        "year": 2016,
        "active": True,
        "type": "mobile",
    },
    {
        "id": "M10_2016",
        "code": "M10",
        "title": _("Extraneous Functionality"),
        "year": 2016,
        "active": True,
        "type": "mobile",
    },
    {
        "id": "A1_2013",
        "code": "A1",
        "title": _("Injection"),
        "year": 2013,
        "active": True,
        "type": "api",
    },
    {
        "id": "A2_2013",
        "code": "A2",
        "title": _("Broken Authentication and Session Management"),
        "year": 2013,
        "active": True,
        "type": "api",
    },
    {
        "id": "A3_2013",
        "code": "A3",
        "title": _("Cross Site Scripting"),
        "year": 2013,
        "active": True,
        "type": "api",
    },
    {
        "id": "A4_2013",
        "code": "A4",
        "title": _("Insecure Direct Object References"),
        "year": 2013,
        "active": True,
        "type": "api",
    },
    {
        "id": "A5_2013",
        "code": "A5",
        "title": _("Security Misconfiguration"),
        "year": 2013,
        "active": True,
        "type": "api",
    },
    {
        "id": "A6_2013",
        "code": "A6",
        "title": _("Sensitive Data Exposure"),
        "year": 2013,
        "active": True,
        "type": "api",
    },
    {
        "id": "A7_2013",
        "code": "A7",
        "title": _("Missing Function Level Access Control"),
        "year": 2013,
        "active": True,
        "type": "api",
    },
    {
        "id": "A8_2013",
        "code": "A8",
        "title": _("Cross-Site Request Forgery (CSRF)"),
        "year": 2013,
        "active": True,
        "type": "api",
    },
    {
        "id": "A9_2013",
        "code": "A9",
        "title": _("Using Components with Known Vulnerabilities"),
        "year": 2013,
        "active": True,
        "type": "api",
    },
    {
        "id": "A10_2013",
        "code": "A10",
        "title": _("Unvalidated Redirects and Forwards"),
        "year": 2013,
        "active": True,
        "type": "api",
    },
]


class OWASP:
    TYPE_MOBILE = "mobile"
    TYPE_API = "api"

    def __init__(self, id, code, title, year, type, description="", active=True):
        self.pk = id
        self.id = id
        self.title = title
        self.code = code
        self.description = description
        self.year = year
        self.active = active
        self.type = type

    @property
    def is_mobile(self):
        return self.type == self.TYPE_MOBILE

    @property
    def is_api(self):
        return self.type == self.TYPE_API

    def __str__(self):
        return "%s - %s - %s - %s" % (self.id, self.code, self.title, self.year)

    def __repr__(self):
        return "<OWASP: %s>" % self.__str__()


OWASP_DATA = {d["id"]: OWASP(**d) for d in data}
