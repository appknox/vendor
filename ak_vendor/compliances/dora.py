from gettext import gettext as _

# Reference: https://eur-lex.europa.eu/eli/reg/2022/2554/oj/eng

data = [
    {
        "id": "dora_8_5_6",
        "code": "Art. 8(5)-(6)",
        "title": _(
            "Identify and document processes dependent on ICT third-party service "
            "providers and interconnections supporting critical/important functions; "
            "maintain and periodically update relevant inventories."
        ),
    },
    {
        "id": "dora_9_2_transit",
        "code": "Art. 9(2)",
        "title": _(
            "Maintain the availability, authenticity, integrity and confidentiality "
            "of data in transit."
        ),
    },
    {
        "id": "dora_9_2_crypto",
        "code": "Art. 9(2)",
        "title": _("Maintain the confidentiality and integrity of data."),
    },
    {
        "id": "dora_9_2_malformed",
        "code": "Art. 9(2)",
        "title": _(
            "Maintain the availability, integrity and confidentiality of ICT systems"
            " and data."
        ),
    },
    {
        "id": "dora_9_2_sensitive",
        "code": "Art. 9(2) and 9(3)(c)",
        "title": _(
            "Maintain confidentiality/integrity of data at rest or in use; prevent "
            "confidentiality breaches and loss of data."
        ),
    },
    {
        "id": "dora_9_3_a",
        "code": "Art. 9(3)(a)",
        "title": _("Ensure the security of the means of transfer of data."),
    },
    {
        "id": "dora_9_3_bc_external",
        "code": "Art. 9(3)(b)-(c)",
        "title": _(
            "Relevant where the exposure creates a risk of unauthorised access or"
            " data loss."
        ),
    },
    {
        "id": "dora_9_3_bc_malformed",
        "code": "Art. 9(3)(b)-(c)",
        "title": _(
            "Minimise technical flaws (e.g. overflow/DoS-type conditions) that may"
            " hinder business activity or cause data loss/integrity breach."
        ),
    },
    {
        "id": "dora_9_3_bc_unauthorised",
        "code": "Art. 9(3)(b)-(c)",
        "title": _(
            "Minimise the risk of corruption or loss of data, unauthorised access "
            "and technical flaws; prevent unavailability, impairment of "
            "authenticity/integrity, breaches of confidentiality and loss of data."
        ),
    },
    {
        "id": "dora_9_4_c",
        "code": "Art. 9(4)(c)",
        "title": _(
            "Limit the physical or logical access to information assets and ICT "
            "assets to what is required for legitimate and approved functions only."
        ),
    },
    {
        "id": "dora_9_4_d_crypto",
        "code": "Art. 9(4)(d)",
        "title": _(
            "Implement strong authentication mechanisms and protection of "
            "cryptographic keys, encrypting data based on approved "
            "data-classification and ICT risk-assessment processes."
        ),
    },
    {
        "id": "dora_9_4_d_sensitive",
        "code": "Art. 9(4)(d)",
        "title": _(
            "Apply encryption / key-protection controls appropriate to the "
            "classification of the data."
        ),
    },
    {
        "id": "dora_25_1_transit",
        "code": "Art. 25(1)",
        "title": _(
            "Evidenced via vulnerability assessments/scans and penetration testing."
        ),
    },
    {
        "id": "dora_25_1_security_testing",
        "code": "Art. 25(1)",
        "title": _("Evidenced via vulnerability assessments/security testing."),
    },
    {
        "id": "dora_25_1_unauthorised",
        "code": "Art. 25(1)",
        "title": _(
            "Evidenced via vulnerability assessments/scans, source-code reviews "
            "where feasible, and penetration testing."
        ),
    },
]


class DORA:
    """Represents a single DORA (Regulation (EU) 2022/2554) article entry."""

    def __init__(self, id, code, title):
        self.pk = id
        self.id = id
        self.code = code
        self.title = title

    def __str__(self):
        return f"{self.id} - {self.code} - {self.title}"

    def __repr__(self):
        return "<DORA: %s>" % self.__str__()


DORA_DATA = {d["id"]: DORA(**d) for d in data}
