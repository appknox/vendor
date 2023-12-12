from gettext import gettext as _

data = [
    {"id": "AC_3", "code": "AC-3", "title": _("Access Enforcement")},
    {
        "id": "AC_3_11",
        "code": "AC-3(11)",
        "title": _("Restrict access to specific info type"),
    },
    {"id": "AC_4", "code": "AC-4", "title": _("Information Flow Enforcement")},
    {"id": "AC_5", "code": "AC-5", "title": _("Separation of Duties")},
    {"id": "AC_6", "code": "AC-6", "title": _("Least Privilege")},
    {"id": "AC_16", "code": "AC-16", "title": _("Security Attributes")},
    {
        "id": "AC_17",
        "code": "AC-17",
        "title": _("Remote Access | MONITORING AND CONTROL"),
    },
    {
        "id": "AC_17_2",
        "code": "AC-17(2)",
        "title": _("Protection of Confidentiality and Integrity Using Encryption"),
    },
    {"id": "AC_18_1", "code": "AC-18(1)", "title": _("Authentication and encryption")},
    {
        "id": "AC_19_5",
        "code": "AC-19(5)",
        "title": _("Full device/container based encryption"),
    },
    {
        "id": "AU_13",
        "code": "AU-13",
        "title": _("Monitoring for Information Disclosure"),
    },
    {"id": "CA_2", "code": "CA-2", "title": _("Control Assessments")},
    {"id": "CA_3", "code": "CA-3", "title": _("Information Exchange")},
    {"id": "CA_7", "code": "CA-7", "title": _("Continuous Monitoring")},
    {"id": "CA_8", "code": "CA-8", "title": _("Penetration Testing")},
    {"id": "CM_2", "code": "CM-2", "title": _("Baseline Configuration")},
    {"id": "CM_3", "code": "CM-3", "title": _("Configuration Management")},
    {"id": "CM_6", "code": "CM-6", "title": _("Configuration Settings")},
    {"id": "CM_7", "code": "CM-7", "title": _("Least Functionality")},
    {"id": "CM_8", "code": "CM-8", "title": _("System Component Inventory")},
    {"id": "IR_4", "code": "IR-4", "title": _("Incident Handling")},
    {
        "id": "MA_3",
        "code": "MA-3",
        "title": _("Maintenance Tools | Software Updates and Patches"),
    },
    {"id": "MA_3_6", "code": "MA-3(6)", "title": _("Software Updates And Patches")},
    {
        "id": "PE_3",
        "code": "PE-3",
        "title": _("Physical Access Control | Tamper Protection"),
    },
    {"id": "PE_6", "code": "PE-6", "title": _("Monitoring Physical Access")},
    {"id": "PM_5", "code": "PM-5", "title": _("System Inventory")},
    {"id": "PM_14", "code": "PM-14", "title": _("Testing, Training, and Monitoring")},
    {"id": "PS_6", "code": "PS-6", "title": _("Access Agreements")},
    {"id": "RA_2", "code": "RA-2", "title": _("Security Categorization")},
    {"id": "RA_3", "code": "RA-3", "title": _("Risk Assessment")},
    {"id": "RA_5", "code": "RA-5", "title": _("Vulnerability Monitoring and Scanning")},
    {"id": "RA_9", "code": "RA-9", "title": _("Criticality Analysis")},
    {"id": "SA_3", "code": "SA-3", "title": _("System Development Life Cycle")},
    {"id": "SA_11", "code": "SA-11", "title": _("Developer Testing and Evaluation")},
    {"id": "SA_11_1", "code": "SA-11(1)", "title": _("STATIC CODE ANALYSIS")},
    {"id": "SA_11_4", "code": "SA-11(4)", "title": _("MANUAL CODE REVIEWS ")},
    {"id": "SA_11_5", "code": "SA-11(5)", "title": _("PENETRATION TESTING")},
    {"id": "SA_11_8", "code": "SA-11(8)", "title": _("DYNAMIC CODE ANALYSIS")},
    {
        "id": "SA_15",
        "code": "SA-15",
        "title": _("Development process, standards and tools"),
    },
    {"id": "SA_18", "code": "SA-18", "title": _("Tamper Resistance And Detection")},
    {"id": "SI_2", "code": "SI-2", "title": _("Flaw Remediation")},
    {"id": "SI_3", "code": "SI-3", "title": _("Malicious Code Protection")},
    {"id": "SI_4", "code": "SI-4", "title": _("System Monitoring")},
    {"id": "SI_4_22", "code": "SI-4(22)", "title": _("UNAUTHORIZED NETWORK SERVICES")},
    {
        "id": "SI_7",
        "code": "SI-7",
        "title": _("Software, Firmware, And Information Integrity"),
    },
    {"id": "SI_7_6", "code": "SI-7(6)", "title": _("Cryptographic Protection")},
    {"id": "SI_10", "code": "SI-10", "title": _("Information Input Validation")},
    {
        "id": "SI_10_5",
        "code": "SI-10(5)",
        "title": _("RESTRICT INPUTS TO TRUSTED SOURCES AND APPROVED FORMATS"),
    },
    {"id": "SI_10_6", "code": "SI-10(6)", "title": _("INJECTION PREVENTION")},
    {"id": "SI_16", "code": "SI-16", "title": _("Memory Protection")},
    {"id": "SC_7", "code": "SC-7", "title": _("Boundary Protection")},
    {
        "id": "SC_8",
        "code": "SC-8",
        "title": _("Transmission Confidentiality and Integrity"),
    },
    {
        "id": "SC_12",
        "code": "SC-12",
        "title": _("Cryptographic Key Establishment and Management"),
    },
    {"id": "SC_13", "code": "SC-13", "title": _("Cryptographic Protection")},
    {
        "id": "SC_17",
        "code": "SC-17",
        "title": _("Public Key Infrastructure Certificates"),
    },
    {"id": "SC_18", "code": "SC-18", "title": _("Mobile Code")},
    {"id": "SC_28", "code": "SC-28", "title": _("Protection of Information at Rest")},
    {"id": "SC_31", "code": "SC-31", "title": _("Use of Cryptography")},
    {"id": "SR_9", "code": "SR-9", "title": _("Tamper Resistance and Detection")},
]


class NISTSP80053:
    def __init__(self, id, code, title):
        self.pk = id
        self.id = id
        self.title = title
        self.code = code

    def __str__(self):
        return f"{self.id} - {self.code} - {self.title}"

    def __repr__(self):
        return "<NISTSP80053: %s>" % self.__str__()


NISTSP80053_DATA = {d["id"]: NISTSP80053(**d) for d in data}
