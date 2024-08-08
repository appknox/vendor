from gettext import gettext as _

# Reference: PCIDSS-4.0 :- https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Supporting%20Document/PCI_DSS-QRG-v4_0.pdf

data = [
    {
        "title": _(
            "Install and maintain network security controls"
        ),
        "code": "1.1",
        "id": "1_1",
        "description": _(
            "Processes and mechanisms for installing and maintaining network security "
            "controls are defined and understood."
        ),
    },
    {
        "title": _(
            "Install and maintain network security controls"
        ),
        "code": "1.2",
        "id": "1_2",
        "description": _(
            "Network security controls (NSCs) are configured and maintained"
        ),
    },
    {
        "title": _(
            "Install and maintain network security controls"
        ),
        "code": "1.3",
        "id": "1_3",
        "description": _(
            "Network access to and from the cardholder data environment is restricted."
        ),
    },
    {
        "title": _(
            "Install and maintain network security controls"
        ),
        "code": "1.4",
        "id": "1_4",
        "description": _(
            "Network connections between trusted and untrusted networks are controlled."
        ),
    },
        {
        "title": _(
            "Install and maintain network security controls"
        ),
        "code": "1.5",
        "id": "1_5",
        "description": _(
            "Risks to the CDE from computing devices that are able to connect to both untrusted "
            "networks and the CDE are mitigated"
        ),
    },
    {
        "title": _(
            "Apply secure configurations to all system components"
        ),
        "code": "2.1",
        "id": "2_1",
        "description": _(
            "Processes and mechanisms for applying secure configurations to all system "
            "components are defined and understood"
        ),
    },
    {
        "title": _(
            "Apply secure configurations to all system components"
        ),
        "code": "2.2",
        "id": "2_2",
        "description": _(
            "System components are configured and managed securely"
        ),
    },
    {
        "title": _(
            "Apply secure configurations to all system components"
        ),
        "code": "2.3",
        "id": "2_3",
        "description": _(
            "Wireless environments are configured and managed securely"
        ),
    },
    {
        "title": _("Protect Account Data"),
        "code": "3.1",
        "id": "3_1",
        "description": _(
            "Processes and mechanisms for protecting stored account data are defined and understood"
        ),
    },
    {
        "title": _("Protect Account Data"),
        "code": "3.2",
        "id": "3_2",
        "description": _(
            "Storage of account data is kept to a minimum"
        ),
    },
    {
        "title": _("Protect Account Data"),
        "code": "3.3",
        "id": "3_3",
        "description": _(
            "Sensitive authentication data (SAD) is not stored after authorization"
        ),
    },
    {
        "title": _("Protect Account Data"),
        "code": "3.4",
        "id": "3_4",
        "description": _(
            "Access to displays of full PAN and ability to copy cardholder data are restricted"
        ),
    },
    {
        "title": _("Protect Account Data"),
        "code": "3.5",
        "id": "3_5",
        "description": _(
            "Primary account number (PAN) is secured wherever it is stored"
        ),
    },
    {
        "title": _("Protect Account Data"),
        "code": "3.6",
        "id": "3_6",
        "description": _(
            "Cryptographic keys used to protect stored account data are secured."
        ),
    },
     {
        "title": _("Protect Account Data"),
        "code": "3.7",
        "id": "3_7",
        "description": _(
            "Where cryptography is used to protect stored account data, key management "
            "processes and procedures covering all aspects of the key lifecycle are "
            "defined and implemented"
        ),
    },
    {
        "title": _(
            "Protect cardholder data with strong cryptography during transmission over open, public networks"
        ),
        "code": "4.1",
        "id": "4_1",
        "description": _(
            "Processes and mechanisms for protecting cardholder data with strong " 
            "cryptography during transmission over open, public networks are "
            "defined and documented."
        ),
    },
    {
        "title": _(
            "Protect cardholder data with strong cryptography during transmission over open, public networks"
        ),
        "code": "4.2",
        "id": "4_2",
        "description": _(
            "PAN is protected with strong cryptography during transmission"
        ),
    },
    {
        "title": _("Protect all systems and networks from malicious software"),
        "code": "5.1",
        "id": "5_1",
        "description": _(
            "Processes and mechanisms for protecting all systems and networks "
            "from malicious software are defined and understood"
        ),
    },
    {
        "title": _("Protect all systems and networks from malicious software"),
        "code": "5.2",
        "id": "5_2",
        "description": _(
            "Malicious software (malware) is prevented, or detected and addressed"
        ),
    },
      {
        "title": _("Protect all systems and networks from malicious software"),
        "code": "5.3",
        "id": "5_3",
        "description": _(
            "Anti-malware mechanisms and processes are active, maintained, and monitored"
        ),
    },
      {
        "title": _("Protect all systems and networks from malicious software"),
        "code": "5.4",
        "id": "5_4",
        "description": _(
            "Anti-phishing mechanisms protect users against phishing attacks"
        ),
    },
    {
        "title": _("Develop and maintain secure systems and applications"),
        "code": "6.1",
        "id": "6_1",
        "description": _(
            "Processes and mechanisms for developing and maintaining secure "
            "systems and software are defined and understood"
        ),
    },
    {
        "title": _("Develop and maintain secure systems and applications"),
        "code": "6.2",
        "id": "6_2",
        "description": _(
            "Bespoke and custom software are developed securely"
        ),
    },
    {
        "title": _("Develop and maintain secure systems and applications"),
        "code": "6.3",
        "id": "6_3",
        "description": _(
            "Security vulnerabilities are identified and addressed"
        ),
    },
    {
        "title": _("Develop and maintain secure systems and applications"),
        "code": "6.4",
        "id": "6_4",
        "description": _(
            "Public-facing web applications are protected against attacks"
        ),
    },
    {
        "title": _("Develop and maintain secure systems and applications"),
        "code": "6.5",
        "id": "6_5",
        "description": _(
            "Changes to all system components are managed securely"
        ),
    },
    {
        "title": _("Restrict access to cardholder data by business need to know"),
        "code": "7.1",
        "id": "7_1",
        "description": _(
            "Processes and mechanisms for restricting access to system components "
            "and cardholder data by business need to know are "
            "defined and understood"
        ),
    },
    {
        "title": _("Restrict access to cardholder data by business need to know"),
        "code": "7.2",
        "id": "7_2",
        "description": _(
            "Access to system components and data is appropriately defined and assigned"
        ),
    },
        {
        "title": _("Restrict access to cardholder data by business need to know"),
        "code": "7.3",
        "id": "7_3",
        "description": _(
            "Access to system components and data is managed via an access control system(s)"
        ),
    },
    {
        "title": _("Identify users and authenticate access to system components"),
        "code": "8.1",
        "id": "8_1",
        "description": _(
            "Processes and mechanisms for identifying users and authenticating access "
            "to system components are defined and understood"
        ),
    },
    {
        "title": _("Identify users and authenticate access to system components"),
        "code": "8.2",
        "id": "8_2",
        "description": _(
            "User identification and related accounts for users and administrators "
            "are strictly managed throughout an account’s lifecycle"
        ),
    },
    {
        "title": _("Identify users and authenticate access to system components"),
        "code": "8.3",
        "id": "8_3",
        "description": _(
            "Strong authentication for users and administrators is established and managed"
        ),
    },
    {
        "title": _("Identify users and authenticate access to system components"),
        "code": "8.4",
        "id": "8_4",
        "description": _(
            "Multi-factor authentication (MFA) is implemented to secure access into the CDE"
        ),
    },
    {
        "title": _("Identify users and authenticate access to system components"),
        "code": "8.5",
        "id": "8_5",
        "description": _(
            "Multi-factor authentication (MFA) systems are configured to prevent misuse"
        ),
    },
    {
        "title": _("Identify users and authenticate access to system components"),
        "code": "8.6",
        "id": "8_6",
        "description": _(
            "Use of application and system accounts and associated authentication factors "
            "is strictly managed."
        ),
    },
    {
        "title": _("Restrict physical access to cardholder data"),
        "code": "9.1",
        "id": "9_1",
        "description": _(
            "Processes and mechanisms for restricting physical access to "
            "cardholder data are defined and understood"
        ),
    },
    {
        "title": _("Restrict physical access to cardholder data"),
        "code": "9.2",
        "id": "9_2",
        "description": _(
            "Physical access controls manage entry into facilities and "
            "systems containing cardholder data"
        ),
    },
    {
        "title": _("Restrict physical access to cardholder data"),
        "code": "9.3",
        "id": "9_3",
        "description": _(
            "Physical access for personnel and visitors is authorized and managed"
        ),
    },
    {
        "title": _("Restrict physical access to cardholder data"),
        "code": "9.4",
        "id": "9_4",
        "description": _(
            "Media with cardholder data is securely stored, accessed, "
            "distributed, and destroyed"
        ),
    },
    {
        "title": _("Restrict physical access to cardholder data"),
        "code": "9.5",
        "id": "9_5",
        "description": _(
            "Point-of-interaction (POI) devices are protected from tampering "
            "and unauthorized substitution"
        ),
    },
    {
        "title": _(
            "Log and monitor all access to system components and cardholder data"
        ),
        "code": "10.1",
        "id": "10_1",
        "description": _(
            "Processes and mechanisms for logging and monitoring all access "
            "to system components and cardholder data are defined "
            "and documented"
        ),
    },
    {
        "title": _(
            "Log and monitor all access to system components and cardholder data"
        ),
        "code": "10.2",
        "id": "10_2",
        "description": _(
            "Audit logs are implemented to support the detection of anomalies "
            "and suspicious activity, and the "
            "forensic analysis of events"
        ),
    },
    {
        "title": _(
            "Log and monitor all access to system components and cardholder data"
        ),
        "code": "10.3",
        "id": "10_3",
        "description": _(
            "Audit logs are protected from destruction and unauthorized modifications"
        ),
    },
    {
        "title": _(
            "Log and monitor all access to system components and cardholder data"
        ),
        "code": "10.4",
        "id": "10_4",
        "description": _(
            "Audit logs are reviewed to identify anomalies or suspicious activity"
        ),
    },
    {
        "title": _(
            "Log and monitor all access to system components and cardholder data"
        ),
        "code": "10.5",
        "id": "10_5",
        "description": _(
            "Audit log history is retained and available for analysis"
        ),
    },
    {
        "title": _(
            "Log and monitor all access to system components and cardholder data"
        ),
        "code": "10.6",
        "id": "10_6",
        "description": _(
            "Time-synchronization mechanisms support consistent time "
            "settings across all systems"
        ),
    },
    {
        "title": _(
            "Log and monitor all access to system components and cardholder data"
        ),
        "code": "10.7",
        "id": "10_7",
        "description": _(
            "Failures of critical security control systems are detected, "
            "reported, and responded to promptly"
        ),
    },
    {
        "title": _("Test security of systems and networks regularly"),
        "code": "11.1",
        "id": "11_1",
        "description": _(
            "Processes and mechanisms for regularly testing security of systems "
            "and networks are defined and understood"
        ),
    },
    {
        "title": _("Test security of systems and networks regularly"),
        "code": "11.2",
        "id": "11_2",
        "description": _(
            "Wireless access points are identified and monitored, and unauthorized "
            "wireless access points are addressed"
        ),
    },
    {
        "title": _("Test security of systems and networks regularly"),
        "code": "11.3",
        "id": "11_3",
        "description": _(
            "External and internal vulnerabilities are regularly identified, "
            "prioritized, and addressed"
        ),
    },
    {
        "title": _("Test security of systems and networks regularly"),
        "code": "11.4",
        "id": "11_4",
        "description": _(
            "External and internal penetration testing is regularly performed, "
            "and exploitable vulnerabilities and security "
            "weaknesses are corrected"
        ),
    },
    {
        "title": _("Test security of systems and networks regularly"),
        "code": "11.5",
        "id": "11_5",
        "description": _(
            "Network intrusions and unexpected file changes are detected and responded to."
        ),
    },
        {
        "title": _("Test security of systems and networks regularly"),
        "code": "11.6",
        "id": "11_6",
        "description": _(
            "Unauthorized changes on payment pages are detected and responded to"
        ),
    },
    {
        "title": _(
            "Support information security with organizational policies and programs"
        ),
        "code": "12.1",
        "id": "12_1",
        "description": _(
            "A comprehensive information security policy that governs and provides "
            "direction for protection of the entity’s information assets "
            "is known and current"
        ),
    },
    {
        "title": _(
            "Support information security with organizational policies and programs"
        ),
        "code": "12.2",
        "id": "12_2",
        "description": _(
            "Acceptable use policies for end-user technologies are defined and implemented"
        ),
    },
    {
        "title": _(
            "Support information security with organizational policies and programs"
        ),
        "code": "12.3",
        "id": "12_3",
        "description": _(
            "Risks to the cardholder data environment are formally identified, "
            "evaluated, and managed"
        ),
    },
    {
        "title": _(
            "Support information security with organizational policies and programs"
        ),
        "code": "12.4",
        "id": "12_4",
        "description": _(
            "PCI DSS compliance is managed"
        ),
    },
    {
        "title": _(
            "Support information security with organizational policies and programs"
        ),
        "code": "12.5",
        "id": "12_5",
        "description": _(
            "PCI DSS scope is documented and validated"
        ),
    },
    {
        "title": _(
            "Support information security with organizational policies and programs"
        ),
        "code": "12.6",
        "id": "12_6",
        "description": _(
            "Security awareness education is an ongoing activity"
        ),
    },
    {
        "title": _(
            "Support information security with organizational policies and programs"
        ),
        "code": "12.7",
        "id": "12_7",
        "description": _(
            "Personnel are screened to reduce risks from insider threats"
        ),
    },
    {
        "title": _(
            "Support information security with organizational policies and programs"
        ),
        "code": "12.8",
        "id": "12_8",
        "description": _(
            "Risk to information assets associated with third-party service provider "
            "(TPSP) relationships is managed"
        ),
    },
    {
        "title": _(
            "Support information security with organizational policies and programs"
        ),
        "code": "12.9",
        "id": "12_9",
        "description": _(
            "Third-party service providers (TPSPs) support their customers’ "
            "PCI DSS compliance"
        ),
    },
        {
        "title": _(
            "Support information security with organizational policies and programs"
        ),
        "code": "12.10",
        "id": "12_10",
        "description": _(
            "Suspected and confirmed security incidents that could impact "
            "the CDE are responded to immediately"
        ),
    },
]


class PCIDSS4:
    def __init__(self, id, code, title, description, active=True):
        self.pk = id
        self.id = id
        self.title = title
        self.code = code
        self.description = description
        self.active = active

    def __str__(self):
        return f"{self.id} - {self.code} - {self.title} - {self.description}"

    def __repr__(self):
        return "<PCIDSS4: %s>" % self.__str__()


PCIDSS4_DATA = {d["id"]: PCIDSS4(**d) for d in data}
