from gettext import gettext as _

# Reference: https://eur-lex.europa.eu/eli/reg/2024/2847/oj

data = [
    {
        "id": "cra_i_2_a",
        "code": "Annex I, Part I, point (2)(a)",
        "title": _(
            "be made available on the market without known exploitable vulnerabilities;"
        ),
    },
    {
        "id": "cra_i_2_b",
        "code": "Annex I, Part I, point (2)(b)",
        "title": _(
            "be made available on the market with a secure by default configuration, "
            "unless otherwise agreed between manufacturer and business user in relation "
            "to a tailor-made product with digital elements, including the possibility "
            "to reset the product to its original state;"
        ),
    },
    {
        "id": "cra_i_2_d",
        "code": "Annex I, Part I, point (2)(d)",
        "title": _(
            "ensure protection from unauthorised access by appropriate control "
            "mechanisms, including but not limited to authentication, identity or "
            "access management systems, and report on possible unauthorised access;"
        ),
    },
    {
        "id": "cra_i_2_e",
        "code": "Annex I, Part I, point (2)(e)",
        "title": _(
            "protect the confidentiality of stored, transmitted or otherwise processed "
            "data, personal or other, such as by encrypting relevant data at rest or in "
            "transit by state of the art mechanisms, and by using other technical means;"
        ),
    },
    {
        "id": "cra_i_2_f",
        "code": "Annex I, Part I, point (2)(f)",
        "title": _(
            "protect the integrity of stored, transmitted or otherwise processed data, "
            "personal or other, commands, programs and configuration against any "
            "manipulation or modification not authorised by the user, and report on "
            "corruptions;"
        ),
    },
    {
        "id": "cra_i_2_g",
        "code": "Annex I, Part I, point (2)(g)",
        "title": _(
            "process only data, personal or other, that are adequate, relevant and "
            "limited to what is necessary in relation to the intended purpose of the "
            "product with digital elements (data minimisation);"
        ),
    },
    {
        "id": "cra_i_2_h",
        "code": "Annex I, Part I, point (2)(h)",
        "title": _(
            "protect the availability of essential and basic functions, also after an "
            "incident, including through resilience and mitigation measures against "
            "denial-of-service attacks;"
        ),
    },
    {
        "id": "cra_i_2_j",
        "code": "Annex I, Part I, point (2)(j)",
        "title": _(
            "be designed, developed and produced to limit attack surfaces, including "
            "external interfaces;"
        ),
    },
    {
        "id": "cra_i_2_k",
        "code": "Annex I, Part I, point (2)(k)",
        "title": _(
            "be designed, developed and produced to reduce the impact of an incident "
            "using appropriate exploitation mitigation mechanisms and techniques;"
        ),
    },
    {
        "id": "cra_ii_2",
        "code": "Annex I, Part II, point (2)",
        "title": _(
            "in relation to the risks posed to products with digital elements, address "
            "and remediate vulnerabilities without delay, including by providing "
            "security updates; where technically feasible, new security updates shall "
            "be provided separately from functionality updates;"
        ),
    },
]


class EUCRA:
    """Represents a single EU CRA (Regulation (EU) 2024/2847) annex entry."""

    def __init__(self, id, code, title):
        self.pk = id
        self.id = id
        self.code = code
        self.title = title

    def __str__(self):
        return f"{self.id} - {self.code} - {self.title}"

    def __repr__(self):
        return "<EUCRA: %s>" % self.__str__()


EUCRA_DATA = {d["id"]: EUCRA(**d) for d in data}
