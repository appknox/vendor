from gettext import gettext as _

# Reference - SAMA 1.0 From https://www.sama.gov.sa/en-US/RulesInstructions/CyberSecurity/Cyber%20Security%20Framework.pdf

data = [
    {
        "id": "3_2_1",
        "code": "3.2.1",
        "title": _("Cyber Security Risk Management"),
        "description": _(
            "A cyber security risk management process should be defined,"
            " approved and implemented, and should be aligned with the Member"
            " Organization's enterprise risk management process."
        ),
    },
    {
        "id": "3_2_2",
        "code": "3.2.2",
        "title": _("Regulatory Compliance"),
        "description": _(
            "A process should be established by the Member Organization to identify,"
            " communicate and comply with the cyber security implications of relevant"
            " regulations."
        ),
    },
    {
        "id": "3_2_3",
        "code": "3.2.3",
        "title": _("Compliance with (inter)national industry standards"),
        "description": _(
            "The Member Organization should comply with mandatory"
            " (inter)national industry standards."
        ),
    },
    {
        "id": "3_3_4",
        "code": "3.3.4",
        "title": _("Cyber Security Architecture"),
        "description": _(
            "The cyber security status of the Member Organization's information assets"
            " should be subject to periodic cyber security review."
        ),
    },
    {
        "id": "3_3_5",
        "code": "3.3.5",
        "title": _("Cyber Security Audits"),
        "description": _(
            "The cyber security status of the Member Organization's information assets"
            " should be subject to thorough, independent and regular cyber security"
            " audits performed in accordance with generally accepted auditing"
            " standards and SAMA cyber security framework."
        ),
    },
    {
        "id": "3_3_1",
        "code": "3.3.1",
        "title": _("Human Resources"),
        "description": _(
            "The Member Organization should incorporate cyber security"
            " requirements into human resources processes."
        ),
    },
    {
        "id": "3_3_2",
        "code": "3.3.2",
        "title": _("Physical Security"),
        "description": _(
            "The Member Organization should ensure all facilities"
            " which host information assets are physically"
            " protected against intentional and unintentional security events."
        ),
    },
    {
        "id": "3_3_3",
        "code": "3.3.3",
        "title": _("Asset Management"),
        "description": _(
            "The Member Organization should define, approve, implement,"
            " communicate and monitor an asset management"
            " process, which supports an accurate,"
            " up-to-date and unified asset register."
        ),
    },
    {
        "id": "3_3_4",
        "code": "3.3.4",
        "title": _("Cyber Security Architecture"),
        "description": _(
            "The Member Organization should define, follow and review the"
            " cyber security architecture, which outlines the cyber security"
            " requirements in the enterprise "
            " architecture and addresses the design principles"
            " for developing cyber security capabilities."
        ),
    },
    {
        "id": "3_3_5",
        "code": "3.3.5",
        "title": _("Identity and Access Management"),
        "description": _(
            "The Member Organization should restrict access to its information assets"
            " in line with their business requirements based on"
            " the need-to-have or need-to-know principles."
        ),
    },
    {
        "id": "3_3_6",
        "code": "3.3.6",
        "title": _("Application Security"),
        "description": _(
            "The Member Organization should define, approve and implement "
            " cyber security standards for application systems. The compliance with"
            " these standards should be monitored and the effectiveness"
            " of these controls should be measured and periodically evaluated."
        ),
    },
    {
        "id": "3_3_7",
        "code": "3.3.7",
        "title": _("Change Management"),
        "description": _(
            "The Member Organization should define, approve and implement a change"
            " management process that controls all changes to information assets."
            " The compliance with the process should be monitored and the effectiveness"
            " should be measured and periodically evaluated."
        ),
    },
    {
        "id": "3_3_8",
        "code": "3.3.8",
        "title": _("Infrastructure Security"),
        "description": _(
            "The Member Organization should define, approve and"
            " implement cyber security standards for their infrastructure components."
            " The compliance with these standards should be monitored and the"
            " effectiveness should be measured and periodically evaluated."
        ),
    },
    {
        "id": "3_3_9",
        "code": "3.3.9",
        "title": _("Cryptography"),
        "description": _(
            "The use of cryptographic solutions within the Member"
            " Organizations should be defined, approved and implemented."
        ),
    },
    {
        "id": "3_3_10",
        "code": "3.3.10",
        "title": _("Bring Your Own Device (BYOD)"),
        "description": _(
            "When the Member Organization allows the use of personal devices"
            " (e.g., smartphones, tablets, laptops) for business purposes,"
            " the use should be supported by a defined, approved and implemented"
            " cyber security standard, additional staff agreements and a"
            " cyber security awareness training."
        ),
    },
    {
        "id": "3_3_11",
        "code": "3.3.11",
        "title": _("Secure Disposal of Information Assets"),
        "description": _(
            "The information assets of the Member Organization should be securely"
            " disposed when the information assets are no longer required."
        ),
    },
    {
        "id": "3_3_12",
        "code": "3.3.12",
        "title": _("Payment Systems"),
        "description": _(
            "The Member Organization should define, approve,implement and"
            " monitor a cyber security standard for payment systems. The effectiveness"
            " of this process should be measured and periodically evaluated."
        ),
    },
    {
        "id": "3_3_13",
        "code": "3.3.13",
        "title": _("Electronic Banking Services"),
        "description": _(
            "The Member Organization should define, approve, implement"
            " and monitor a cyber security standard for electronic banking services."
            " The effectiveness of this standard should be measured"
            " and periodically evaluated."
        ),
    },
    {
        "id": "3_3_14",
        "code": "3.3.14",
        "title": _("Cyber Security Event Management"),
        "description": _(
            "The Member Organization should define, approve and implement"
            " a security event management process to analyze operational and security"
            " loggings and respond to security events. The effectiveness of this "
            " process should be measured and periodically evaluated."
        ),
    },
    {
        "id": "3_3_15",
        "code": "3.3.15",
        "title": _("Cyber Security Incident Management"),
        "description": _(
            "The Member Organization should define, approve and implement"
            " a cyber security incident management that is aligned with the enterprise"
            " incident management process, to identify, respond to and recover from "
            " cyber security incidents. The effectiveness of this process should "
            " be measured and periodically evaluated."
        ),
    },
    {
        "id": "3_3_16",
        "code": "3.3.16",
        "title": _("Threat Management"),
        "description": _(
            "The Member Organization should define, approve and implement a threat"
            " intelligence management process to identify, assess and understand"
            " threats to the Member Organization information assets, using multiple"
            " reliable sources. The effectiveness of this process should be measured"
            " and periodically evaluated."
        ),
    },
    {
        "id": "3_3_17",
        "code": "3.3.17",
        "title": _("Vulnerability Management"),
        "description": _(
            "The Member Organization should define, approve and implement a"
            " vulnerability management process for the identification and mitigation"
            " of application and infrastructural vulnerabilities. The effectiveness"
            " of this process should be measured and the effectiveness should be"
            " periodically evaluated."
        ),
    },
    {
        "id": "3_4_1",
        "code": "3.4.1",
        "title": _("Contract and Vendor Management"),
        "description": _(
            "The Member Organization should define, approve,"
            " implement and monitor the required cyber security controls"
            " within the contract and vendor management processes."
        ),
    },
    {
        "id": "3_4_2",
        "code": "3.4.2",
        "title": _("Outsourcing"),
        "description": _(
            "The Member Organization should define, implement and monitor"
            " the required cyber security controls within outsourcing policy"
            " and outsourcing process. The effectiveness of the defined cyber security"
            " controls should periodically be measured and evaluated."
        ),
    },
    {
        "id": "3_4_3",
        "code": "3.4.3",
        "title": _("Cloud Computing"),
        "description": _(
            "The Member Organization should define, implement and monitor the required"
            " cyber security controls within the cloud computing policy and process"
            " for hybrid and public cloud services. The effectiveness of the defined"
            " cyber security controls should periodically be measured and evaluated."
        ),
    },
]


class SAMA:
    def __init__(self, id, code, title, description):
        self.pk = id
        self.id = id
        self.title = title
        self.code = code
        self.description = description

    def __str__(self):
        return f"{self.id} - {self.code} - {self.title} - {self.description}"

    def __repr__(self):
        return "<sama: %s>" % self.__str__()


SAMA_DATA = {d["id"]: SAMA(**d) for d in data}
