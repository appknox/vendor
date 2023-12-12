from gettext import gettext as _

data = [
    {
        "id": "3_1_1",
        "code": "3.1.1",
        "title": _(
            "Limit system access to authorized users, processes acting on behalf of authorized users, and devices (including other systems)"
        ),
    },
    {
        "id": "3_1_5",
        "code": "3.1.5",
        "title": _(
            "Employ the principle of least privilege, including for specific security functions and privileged accounts"
        ),
    },
    {
        "id": "3_1_18",
        "code": "3.1.18",
        "title": _("Control connection of mobile devices."),
    },
    {
        "id": "3_1_19",
        "code": "3.1.19",
        "title": _("Encrypt CUI on mobile devices and mobile computing platforms"),
    },
    {
        "id": "3_1_20",
        "code": "3.1.20",
        "title": _(
            "Verify and control/limit connections to and use of external systems."
        ),
    },
    {
        "id": "3_2_2",
        "code": "3.2.2",
        "title": _(
            "Ensure that personnel are trained to carry out their assigned information security-related duties and responsibilities."
        ),
    },
    {
        "id": "3_4_1",
        "code": "3.4.1",
        "title": _(
            "Establish and maintain baseline configurations and inventories of organizational systems (including hardware, software, firmware, and documentation) throughout the respective system development life cycles."
        ),
    },
    {
        "id": "3_4_2",
        "code": "3.4.2",
        "title": _(
            "Establish and enforce security configuration settings for information technology products employed in organizational systems."
        ),
    },
    {
        "id": "3_5_2",
        "code": "3.5.2",
        "title": _(
            "Authenticate (or verify) the identities of users, processes, or devices, as a prerequisite to allowing access to organizational systems"
        ),
    },
    {
        "id": "3_5_10",
        "code": "3.5.10",
        "title": _("Store and transmit only cryptographically-protected passwords"),
    },
    {
        "id": "3_6_2",
        "code": "3.6.2",
        "title": _(
            "Track, document, and report incidents to designated officials and/or authorities both internal and external to the organization"
        ),
    },
    {
        "id": "3_8_9",
        "code": "3.8.9",
        "title": _("Protect the confidentiality of backup CUI at storage locations."),
    },
    {
        "id": "3_11_1",
        "code": "3.11.1",
        "title": _(
            "Periodically assess the risk to organizational operations (including mission, functions, image, or reputation), organizational assets, and individuals, resulting from the operation of organizational systems and the associated processing, storage, or transmission of CUI"
        ),
    },
    {
        "id": "3_11_2",
        "code": "3.11.2",
        "title": _(
            "Scan for vulnerabilities in organizational systems and applications periodically and when new vulnerabilities affecting those systems and applications are identified."
        ),
    },
    {
        "id": "3_11_3",
        "code": "3.11.3",
        "title": _("Remediate vulnerabilities in accordance with risk assessments."),
    },
    {
        "id": "3_12_1",
        "code": "3.12.1",
        "title": _(
            "Periodically assess the security controls in organizational systems to determine if the controls are effective in their application"
        ),
    },
    {
        "id": "3_13_1",
        "code": "3.13.1",
        "title": _(
            "Monitor, control, and protect communications (i.e., information transmitted or received by organizational systems) at the external boundaries and key internal boundaries of organizational systems."
        ),
    },
    {
        "id": "3_13_10",
        "code": "3.13.10",
        "title": _(
            "Establish and manage cryptographic keys for cryptography employed in organizational systems"
        ),
    },
    {
        "id": "3_13_13",
        "code": "3.13.13",
        "title": _("Control and monitor the use of mobile code."),
    },
    {
        "id": "3_13_16",
        "code": "3.13.16",
        "title": _("Protect the confidentiality of CUI at rest."),
    },
    {
        "id": "3_14_1",
        "code": "3.14.1",
        "title": _("Identify, report, and correct system flaws in a timely manner."),
    },
    {
        "id": "3_14_2",
        "code": "3.14.2",
        "title": _(
            "Provide protection from malicious code at designated locations within organizational systems."
        ),
    },
    {
        "id": "3_14_4",
        "code": "3.14.4",
        "title": _(
            "Update malicious code protection mechanisms when new releases are available."
        ),
    },
    {
        "id": "3_14_7",
        "code": "3.14.7",
        "title": _("Identify unauthorized use of organizational systems"),
    },
]


class NISTSP800171:
    def __init__(self, id, code, title):
        self.pk = id
        self.id = id
        self.title = title
        self.code = code

    def __str__(self):
        return f"{self.id} - {self.code} - {self.title}"

    def __repr__(self):
        return "<NISTSP800171: %s>" % self.__str__()


NISTSP800171_DATA = {d["id"]: NISTSP800171(**d) for d in data}
