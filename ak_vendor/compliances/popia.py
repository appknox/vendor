from gettext import gettext as _

# Reference: Protection of Personal Information Act 4 of 2013
# (Government Gazette No. 37067)

data = [
    {
        "id": "popia_19_1_a",
        "code": "s 19(1)(a)",
        "title": _(
            "Secure the integrity and confidentiality of personal information "
            "against loss, damage or unauthorised destruction."
        ),
    },
    {
        "id": "popia_19_1_b",
        "code": "s 19(1)(b)",
        "title": _("Prevent unlawful access to or processing of personal information."),
    },
    {
        "id": "popia_19_2_b",
        "code": "s 19(2)(b)",
        "title": _(
            "Establish and maintain appropriate safeguards against the "
            "risks identified."
        ),
    },
    {
        "id": "popia_19_2_d",
        "code": "s 19(2)(d)",
        "title": _(
            "Ensure that safeguards are continually updated in response to new risks "
            "or deficiencies in previously implemented safeguards."
        ),
    },
    {
        "id": "popia_19_3",
        "code": "s 19(3)",
        "title": _(
            "Have due regard to generally accepted information security practices."
        ),
    },
    {
        "id": "popia_6_1_b",
        "code": "s 6(1)(b) / s 1",
        "title": _(
            "The Act does not apply to personal information that has been "
            "de-identified to the extent that it cannot be re-identified again "
            "(s 6(1)(b)); s 1 defines 'de-identify' and 're-identify'."
        ),
    },
    {
        "id": "popia_10",
        "code": "s 10",
        "title": _(
            "Processing must be adequate, relevant and not excessive given the "
            "purpose. The minimality rule."
        ),
    },
    {
        "id": "popia_11",
        "code": "s 11",
        "title": _(
            "Processing requires one of the six lawful grounds in s 11(1), of which "
            "consent — defined in s 1 as a voluntary, specific and informed "
            "expression of will — is one; the responsible party bears the burden of "
            "proving consent (s 11(2)(a))."
        ),
    },
    {
        "id": "popia_12",
        "code": "s 12",
        "title": _(
            "Personal information must be collected directly from the data subject, "
            "subject to the s 12(2) exceptions (a)-(f)."
        ),
    },
    {
        "id": "popia_18",
        "code": "s 18",
        "title": _(
            "Take reasonably practicable steps to make the data subject aware of "
            "what is collected and from where, by whom, why, and any further "
            "information necessary in the circumstances, including recipients; "
            "subject to the s 18(4) exceptions."
        ),
    },
]


class POPIA:
    """Represents a single POPIA (Act 4 of 2013) section entry."""

    def __init__(self, id, code, title):
        self.pk = id
        self.id = id
        self.code = code
        self.title = title

    def __str__(self):
        return f"{self.id} - {self.code} - {self.title}"

    def __repr__(self):
        return "<POPIA: %s>" % self.__str__()


POPIA_DATA = {d["id"]: POPIA(**d) for d in data}
