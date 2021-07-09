import attr
from typing import List
from gettext import gettext as _


data = [
    {
        "id": "164_312_a_1",
        "code": "164.312(a)(1)",
        "safeguard": _("Technical Safeguards"),
        "title": _("Access Control"),
        "standards": [
            {
                "title": _("Unique User Identification"),
                "description": _(
                    "Assign a unique name and/or number for identifying and "
                    "tracking user identity"
                ),
                "specifications": "Required"
            },
            {
                "title": _("Emergency Access Procedure"),
                "description": _(
                    "Establish (and implement as needed) procedures for "
                    "obtaining  necessary electronic protected health "
                    "information during an emergency."
                ),
                "specifications": "Required"
            },
            {
                "title": _("Automatic Logoff"),
                "description": _(
                    "Implement electronic procedures that terminate an "
                    "electronic session after a predetermined time of "
                    "inactivity."
                ),
                "specifications": "Addressable"
            },
            {
                "title": _("Encryption and Decryption"),
                "description": _(
                    "Implement a method to encrypt and decrypt electronic "
                    "protected health information."
                ),
                "specifications": "Addressable"
            },
        ]
    },
    {
        "id": "164_312_c_1",
        "code": "164.312(c)(1)",
        "safeguard": _("Technical Safeguards"),
        "title": _("Integrity"),
        "standards": [
            {
                "title": _("Mechanism to Authenticate Electronic Protected"),
                "description": _(
                    "Implement electronic mechanisms to corroborate that "
                    "electronic protected health information has not been "
                    "altered or destroyed in an unauthorized manner."
                ),
                "specifications": "Addressable"
            }
        ]
    },
    {
        "id": "164_312_d",
        "code": "164.312(d)",
        "safeguard": _("Technical Safeguards"),
        "title": _("Person or Entity Authentication"),
        "standards": [
            {
                "title": _("Person or Entity Authentication"),
                "description": _(
                    "Implement procedures to verify that a person or entity "
                    "seeking access to ePHI is the one claimed"
                ),
                "specifications": "Required"
            },
        ]
    },
    {
        "id": "164_312_e_1",
        "code": "164.312(e)(1)",
        "safeguard": _("Technical Safeguards"),
        "title": _("Transmission Security"),
        "standards": [
            {
                "title": _("Integrity Controls"),
                "description": _(
                    "Implement security measures to ensure that "
                    "electronically  transmitted ePHI is not improperly "
                    "modified without detection."
                ),
                "specifications": "Addressable"
            },
            {
                "title": _("Encryption"),
                "description": _(
                    "Implement a mechanism to encrypt ePHI in transit."
                ),
                "specifications": "Addressable"
            },
        ]
    },
    {
        "id": "164_310_a_1",
        "code": "164.310(a)(1)",
        "safeguard": _("Physical Safeguards"),
        "title": _("Facility Access Control"),
        "standards": [
            {
                "title": _("Contingency Operations"),
                "description": _(
                    "Establish (and implement as needed) procedures that "
                    "allow facility access in support of restoration of lost "
                    "data under the disaster recovery plan and emergency mode "
                    "operations plan in the event of an emergency"
                ),
                "specifications": "Addressable"
            },
            {
                "title": _("Facility Security Plan"),
                "description": _(
                    "Implement policies and procedures to safeguard the "
                    "facility  and the equipment therein from unauthorized "
                    "physical access, tampering, and theft."
                ),
                "specifications": "Addressable"
            },
            {
                "title": _("Access Control and Validation Procedures"),
                "description": _(
                    "Implement procedures to control and validate a person's "
                    "access to facilities based on their role or function, "
                    "including visitor control, and control of access to "
                    "software  programs for testing and revision."
                ),
                "specifications": "Addressable"
            },
            {
                "title": _("Maintenance Records"),
                "description": _(
                    "Implement policies and procedures to document repairs "
                    "and  modifications to the physical components of a "
                    "facility which are related to security (for example, "
                    "hardware, walls, doors, and locks)."
                ),
                "specifications": "Addressable"
            },
        ]
    },
    {
        "id": "164_310_b",
        "code": "164.310(b)",
        "safeguard": _("Physical Safeguards"),
        "title": _("Workstation Use"),
        "standards": [
            {
                "title": _("Workstation Use"),
                "description": _(
                    "Implement policies and procedures that specify the "
                    "proper functions to be performed, the manner in which "
                    "those functions are to be performed, and the physical "
                    "attributes of the surroundings of a specific workstation "
                    "or class of workstation that can access ePHI."
                ),
                "specifications": "Required"
            },
        ]
    },
    {
        "id": "164_310_c",
        "code": "164.310(c)",
        "safeguard": _("Physical Safeguards"),
        "title": _("Workstation Security"),
        "standards": [
            {
                "title": _("Workstation Use"),
                "description": _(
                    "Implement physical safeguards for all workstations that "
                    "access ePHI, to restrict access to authorized users."
                ),
                "specifications": "Required"
            },
        ]
    },
    {
        "id": "164_310_d_1",
        "code": "164.310(d)(1)",
        "safeguard": _("Physical Safeguards"),
        "title": _("Device and Media Controls"),
        "standards": [
            {
                "title": _("Disposal"),
                "description": _(
                    "Implement policies and procedures to address the final "
                    "disposition of ePHI, and/or the hardware or electronic "
                    "media on which it is stored."
                ),
                "specifications": "Required"
            },
            {
                "title": _("Medical Re-use"),
                "description": _(
                    "Implement procedures for removal of ePHI from electronic "
                    "media before the media are made available for re-use."
                ),
                "specifications": "Required"
            },
            {
                "title": _("Accountability"),
                "description": _(
                    "Maintain a record of the movements of hardware and "
                    "electronic media and any person responsible therefore."
                ),
                "specifications": "Addressable"
            },
            {
                "title": _("Data Storage and Backup"),
                "description": _(
                    "ImpCreate a retrievable, exact copy of electronic "
                    "protected health information, when needed, before "
                    "movement of equipment."
                ),
                "specifications": "Addressable"
            },
        ]
    },
    {
        "id": "164_308_a_1",
        "code": "164.308(a)(1)",
        "safeguard": _("Administrative Safeguards"),
        "title": _("Security Management Process"),
        "standards": [
            {
                "title": _("Risk Analysis"),
                "description": _(
                    "Conduct an accurate and thorough assessment of the "
                    "potential risks and vulnerabilities to the "
                    "confidentiality, integrity, and availability of "
                    "electronic PHI held by the covered entity."
                ),
                "specifications": "Required"
            },
            {
                "title": _("Risk Management"),
                "description": _(
                    "Implement security measures sufficient to reduce risks "
                    "and vulnerabilities to a reasonable and appropriate "
                    "level to comply with Sec. 164.306(a) [Security "
                    "standards: General rules; (a) General requirements]."
                ),
                "specifications": "Required"
            },
            {
                "title": _("Sanction Policy"),
                "description": _(
                    "Apply appropriate sanctions against workforce members "
                    "who fail to comply with the security policies and "
                    "procedures of the covered entity."
                ),
                "specifications": "Required"
            },
            {
                "title": _("Information System Activity Review"),
                "description": _(
                    "Implement procedures to regularly review records of "
                    "information system activity, such as audit logs, access "
                    "reports, and security incident tracking reports."
                ),
                "specifications": "Required"
            },
        ]
    },
    {
        "id": "164_308_a_2",
        "code": "164.308(a)(2)",
        "safeguard": _("Administrative Safeguards"),
        "title": _("Assigned Security Responsibility"),
        "standards": [
            {
                "title": _("Assigned Security Responsibility"),
                "description": _(
                    "Identify the security official who is "
                    "responsible for the development and implementation of "
                    "the policies and procedures required by this subpart "
                    "for the entity."
                ),
                "specifications": "Required"
            },
        ]
    },
    {
        "id": "164_308_a_3",
        "code": "164.308(a)(3)",
        "safeguard": _("Administrative Safeguards"),
        "title": _("Workforce Security"),
        "standards": [
            {
                "title": _("Termination Procedures"),
                "description": _(
                    "Implement procedures for the authorization and/or "
                    "supervision of workforce members who work with "
                    "electronic  protected health information or in locations "
                    "where it might be accessed."
                ),
                "specifications": "Addressable"
            },
            {
                "title": _("Workforce Clearance Procedures"),
                "description": _(
                    "Implement procedures to determine that the access of a "
                    "workforce member to electronic protected health "
                    "information is appropriate."
                ),
                "specifications": "Addressable"
            },
            {
                "title": _("Authorization and/or Supervision"),
                "description": _(
                    "Implement procedures for terminating access to "
                    "electronic protected health information when the "
                    "employment of a workforce member ends or as required by "
                    "determinations made as specified in paragraph "
                    "(a)(3)(ii)(B) [Workforce Clearance Procedures] of this "
                    "section."
                ),
                "specifications": "Addressable"
            },
        ]
    },
    {
        "id": "164_308_a_4",
        "code": "164.308(a)(4)",
        "safeguard": _("Administrative Safeguards"),
        "title": _("Information Access Management"),
        "standards": [
            {
                "title": _("Isolating Health Care Clearinghouse Functions"),
                "description": _(
                    "If a health care clearinghouse is part of a larger "
                    "organization, the clearinghouse must implement policies "
                    "and procedures that protect the electronic protected "
                    "health information of the clearinghouse from "
                    "unauthorized access by the larger organization."
                ),
                "specifications": "Required"
            },
            {
                "title": _("Access Authorization"),
                "description": _(
                    "Implement policies and procedures for granting access to "
                    "electronic protected health information, for example, "
                    "through access to a workstation, transaction, program, "
                    "process, or other mechanism."
                ),
                "specifications": "Addressable"
            },
            {
                "title": _("Access Establishment and Modification"),
                "description": _(
                    "Implement policies and procedures that, based upon the "
                    "entity's access authorization policies, establish, "
                    "document, review, and modify a user's right of access to "
                    "a workstation, transaction, program, or process."
                ),
                "specifications": "Addressable"
            },
        ]
    },
    {
        "id": "164_308_a_5",
        "code": "164.308(a)(5)",
        "safeguard": _("Administrative Safeguards"),
        "title": _("Security Awareness and Training"),
        "standards": [
            {
                "title": _("Security Reminders"),
                "description": _("Periodic security updates."),
                "specifications": "Addressable"
            },
            {
                "title": _("Protection from Malicious Software"),
                "description": _(
                    "Procedures for guarding against, detecting, and "
                    "reporting malicious software."
                ),
                "specifications": "Addressable"
            },
            {
                "title": _("Log-in Monitoring"),
                "description": _(
                    "Procedures for monitoring log-in attempts and reporting "
                    "discrepancies."
                ),
                "specifications": "Addressable"
            },
            {
                "title": _("Password Management"),
                "description": _(
                    "Procedures for creating, changing, and safeguarding "
                    "passwords."
                ),
                "specifications": "Addressable"
            },
        ]
    },
    {
        "id": "164_308_a_6",
        "code": "164.308(a)(6)",
        "safeguard": _("Administrative Safeguards"),
        "title": _("Security Incident Procedures"),
        "standards": [
            {
                "title": _("Response and Report"),
                "description": _(
                    "Identify and respond to suspected or known security "
                    "incidents; mitigate, to the extent practicable, harmful "
                    "effects of security incidents that are known to the "
                    "covered entity; and document security incidents and "
                    "their outcomes."
                ),
                "specifications": "Required"
            },
        ]
    },
    {
        "id": "164_308_a_7",
        "code": "164.308(a)(7)",
        "safeguard": _("Administrative Safeguards"),
        "title": _("Contingency Plan"),
        "standards": [
            {
                "title": _("Data Backup Plan"),
                "description": _(
                    "Establish and implement procedures to create and "
                    "maintain retrievable exact copies of electronic "
                    "protected health information."
                ),
                "specifications": "Required"
            },
            {
                "title": _("Disaster Recovery Plan"),
                "description": _(
                    "Establish (and implement as needed) procedures to "
                    "restore any loss of data."
                ),
                "specifications": "Required"
            },
            {
                "title": _("Emergency Mode Operation Plan"),
                "description": _(
                    "Establish (and implement as needed) procedures to enable "
                    "continuation of critical business processes for "
                    "protection of the security of electronic PHI while "
                    "operating in emergency mode."
                ),
                "specifications": "Required"
            },
            {
                "title": _("Testing and Revision Procedures"),
                "description": _(
                    "Implement procedures for periodic testing and revision "
                    "of contingency plans."
                ),
                "specifications": "Addressable"
            },
            {
                "title": _("Applications and Data Criticality Analysis"),
                "description": _(
                    "Assess the relative criticality of specific applications "
                    "and data in support of other contingency plan components."
                ),
                "specifications": "Addressable"
            },
        ]
    },
    {
        "id": "164_308_a_8",
        "code": "164.308(a)(8)",
        "safeguard": _("Administrative Safeguards"),
        "title": _("Evaluation"),
        "standards": [
            {
                "title": _("Evaluation"),
                "description": _(
                    "Perform a periodic technical and non-technical "
                    "evaluation, based initially upon the standards "
                    "implemented under this rule and subsequently, in "
                    "response to environmental or operational changes "
                    "affecting the security of electronic PHI that "
                    "establishes the extent to which an entity's security "
                    "policies and procedures meet the requirements of this "
                    "subpart."
                ),
                "specifications": "Required"
            },
        ]
    },
    {
        "id": "164_308_b_1",
        "code": "164.308(b)(1)",
        "safeguard": _("Administrative Safeguards"),
        "title": _("Business Associate Contracts and Other Arrangements"),
        "standards": [
            {
                "title": _("Written Contract or Other Arrangement"),
                "description": _(
                    "A covered entity, in accordance with § 164.306 "
                    "[Security Standards: General Rules], may permit a "
                    "business associate to create, receive, maintain, or "
                    "transmit electronic protected health information on "
                    "the covered entity™s behalf only if the covered entity "
                    "obtains satisfactory assurances, in accordance with "
                    "§ 164.314(a) [Business Associate Contracts or Other "
                    "Arrangements] that the business associate will "
                    "appropriately safeguard the information. Document the "
                    "satisfactory assurances required by paragraph (b)(1) "
                    "[Business Associate Contracts and Other Arrangements] "
                    "of this section through a written contract or other "
                    "arrangement with the business associate that meets the "
                    "applicable requirements of § 164.314(a) [Business "
                    "Associate Contracts or Other Arrangements]."
                ),
                "specifications": "Required"
            },
        ]
    },
]


@attr.s
class HIPAAStandard:
    title = attr.ib(type=str)
    description = attr.ib(type=str)
    specifications = attr.ib(type=str)

    @classmethod
    def from_json(cls, data):
        return cls(
            title=data.get("title"),
            description=data.get("description"),
            specifications=data.get("specifications"),
        )


@attr.s
class HIPAA:
    id = attr.ib(type=int)
    pk = attr.ib(init=False)
    code = attr.ib(type=str)
    safeguard = attr.ib(type=str)
    title = attr.ib(type=str)
    standards = attr.ib(factory=list, type=List[HIPAAStandard])
    active = attr.ib(type=bool, default=True)

    def __attrs_post_init__(self):
        object.__setattr__(self, "pk", self.id)

    def __str__(self):
        return "%s - %s - %s - %s" % (self.id, self.code, self.title, self.description)

    def __repr__(self):
        return "<HIPAA: %s>" % self.__str__()

    @classmethod
    def from_json(cls, data):
        return cls(
            id=data.get("id"),
            code=data.get("code"),
            safeguard=data.get("safeguard"),
            title=data.get("title"),
            standards=[
                HIPAAStandard.from_json(std) for std in data.get("standards", [])
            ],
            active=data.get("active", True),
        )


HIPAA_DATA = {d["id"]: HIPAA.from_json(d) for d in data}
