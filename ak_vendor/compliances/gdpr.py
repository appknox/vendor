from gettext import gettext as _


data = [
    # Reference: https://gdpr-info.eu/art-25-gdpr/
    {
        "id": "gdpr_25",
        "code": "Art-25-GDPR",
        "title": _("Data protection by design and by default"),
    },
    # Reference: https://gdpr-info.eu/art-32-gdpr/
    {"id": "gdpr_32", "code": "Art-32-GDPR", "title": _("Security of processing"),},
]


class GDPR:
    def __init__(self, id, code, title):
        self.pk = id
        self.id = id
        self.title = title
        self.code = code

    def __str__(self):
        return "%s - %s - %s" % (self.id, self.code, self.title)

    def __repr__(self):
        return "<GDPR: %s>" % self.__str__()


GDPR_DATA = {d["id"]: GDPR(**d) for d in data}
