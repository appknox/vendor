from gettext import gettext as _

data = [
    # Reference: https://mas.owasp.org/MASVS/#the-masvs-control-groups
    {
        "id": "MASVS_1_1",
        "code": "MASVS-STORAGE-1",
        "title": _("The app securely stores sensitive data."),
        "active": True,
    },
    {
        "id": "MASVS_1_2",
        "code": "MASVS-STORAGE-2",
        "title": _("The app prevents leakage of sensitive data."),
        "active": True,
    },
    {
        "id": "MASVS_2_1",
        "code": "MASVS-CRYPTO-1",
        "title": _(
            "The app employs current strong cryptography "
            "and uses it according to industry best practices."
        ),
        "active": True,
    },
    {
        "id": "MASVS_2_2",
        "code": "MASVS-CRYPTO-2",
        "title": _(
            "The app performs key management according to industry best practices."
        ),
        "active": True,
    },
    {
        "id": "MASVS_3_1",
        "code": "MASVS-AUTH-1",
        "title": _(
            "The app uses secure authentication and "
            "authorization protocols and follows the "
            "relevant best practices."
        ),
        "active": True,
    },
    {
        "id": "MASVS_3_2",
        "code": "MASVS-AUTH-2",
        "title": _(
            "The app performs local authentication securely "
            "according to the platform best practices."
        ),
        "active": True,
    },
    {
        "id": "MASVS_3_3",
        "code": "MASVS-AUTH-3",
        "title": _(
            "The app secures sensitive operations with additional authentication."
        ),
        "active": True,
    },
    {
        "id": "MASVS_4_1",
        "code": "MASVS-CODE-1",
        "title": _("The app requires an up-to-date platform version."),
        "active": True,
    },
    {
        "id": "MASVS_4_2",
        "code": "MASVS-CODE-2",
        "title": _("The app has a mechanism for enforcing app updates."),
        "active": True,
    },
    {
        "id": "MASVS_4_3",
        "code": "MASVS-CODE-3",
        "title": _(
            "The app only uses software components without known vulnerabilities."
        ),
        "active": True,
    },
    {
        "id": "MASVS_4_4",
        "code": "MASVS-CODE-4",
        "title": _("The app validates and sanitizes all untrusted inputs."),
        "active": True,
    },
    {
        "id": "MASVS_5_1",
        "code": "MASVS-NETWORK-1",
        "title": _(
            "The app secures all network traffic "
            "according to the current best practices."
        ),
        "active": True,
    },
    {
        "id": "MASVS_5_2",
        "code": "MASVS-NETWORK-2",
        "title": _(
            "The app performs identity pinning for all remote "
            "endpoints under the developer's control."
        ),
        "active": True,
    },
    {
        "id": "MASVS_6_1",
        "code": "MASVS-PLATFORM-1",
        "title": _("The app uses IPC mechanisms securely."),
        "active": True,
    },
    {
        "id": "MASVS_6_2",
        "code": "MASVS-PLATFORM-2",
        "title": _("The app uses WebViews securely."),
        "active": True,
    },
    {
        "id": "MASVS_6_3",
        "code": "MASVS-PLATFORM-3",
        "title": _("The app uses the user interface securely."),
        "active": True,
    },
    {
        "id": "MASVS_7_1",
        "code": "MASVS-RESILIANCE-1",
        "title": _("The app validates the integrity of the platform."),
        "active": True,
    },
    {
        "id": "MASVS_7_2",
        "code": "MASVS-RESILIANCE-2",
        "title": _("The app implements anti-tampering mechanisms."),
        "active": True,
    },
    {
        "id": "MASVS_7_3",
        "code": "MASVS-RESILIANCE-3",
        "title": _("The app implements anti-static analysis mechanisms."),
        "active": True,
    },
    {
        "id": "MASVS_7_4",
        "code": "MASVS-RESILIANCE-4",
        "title": _("The app implements anti-dynamic analysis techniques."),
        "active": True,
    },
]


class MASVS:
    def __init__(self, id, code, title, active=True):
        self.pk = id
        self.id = id
        self.title = title
        self.code = code
        self.active = active

    def __str__(self):
        return f"{self.id} - {self.code} - {self.title}"

    def __repr__(self):
        return "<MASVS: %s>" % self.__str__()


MASVS_DATA = {d["id"]: MASVS(**d) for d in data}
