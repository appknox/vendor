from gettext import gettext as _


data = [
  {
    "id": "164_312_a_1",
    "code": "164.312(a)(1)",
    "safeguard": _("Technical Safeguards"),
    "title": _("Access Control"),
    "standards": [
        {
            "title": "Unique User Identification",
            "description": "Assign a unique name and/or number for identifying and tracking user identity",
            "specifications": "Required"
        },
        {
            "title": "Emergency Access Procedure",
            "description": "Establish (and implement as needed) procedures for obtaining necessary electronic protected health information during an emergency.",
            "specifications": "Required"
        },
        {
            "title": "Automatic Logoff",
            "description": "Implement electronic procedures that terminate an electronic session after a predetermined time of inactivity.",
            "specifications": "Addressable"
        },
        {
            "title": "Encryption and Decryption",
            "description": "Implement a method to encrypt and decrypt electronic protected health information.",
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
            "title": "Mechanism to Authenticate Electronic Protected",
            "description": "Implement electronic mechanisms to corroborate that electronic protected health information has not been altered or destroyed in an unauthorized manner.",
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
            "title": "Person or Entity Authentication",
            "description": "Implement procedures to verify that a person or entity seeking access to ePHI is the one claimed",
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
            "title": "Integrity Controls",
            "description": "Implement security measures to ensure that electronically transmitted ePHI is not improperly modified without detection.",
            "specifications": "Addressable"
        },
        {
            "title": "Encryption",
            "description": "Implement a mechanism to encrypt ePHI in transit.",
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
            "title": "Contingency Operations",
            "description": "Establish (and implement as needed) procedures that allow facility access in support of restoration of lost data under the disaster recovery plan and emergency mode operations plan in the event of an emergency",
            "specifications": "Addressable"
        },
        {
            "title": "Facility Security Plan",
            "description": "Implement policies and procedures to safeguard the facility and the equipment therein from unauthorized physical access, tampering, and theft.",
            "specifications": "Addressable"
        },
        {
            "title": "Access Control and Validation Procedures",
            "description": "Implement procedures to control and validate a person's access to facilities based on their role or function, including visitor control, and control of access to software programs for testing and revision.",
            "specifications": "Addressable"
        },
        {
            "title": "Maintenance Records",
            "description": "Implement policies and procedures to document repairs and modifications to the physical components of a facility which are related to security (for example, hardware, walls, doors, and locks).",
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
            "title": "Workstation Use",
            "description": "Implement policies and procedures that specify the proper functions to be performed, the manner in which those functions are to be performed, and the physical attributes of the surroundings of a specific workstation or class of workstation that can access ePHI.",
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
            "title": "Workstation Use",
            "description": "Implement physical safeguards for all workstations that access ePHI, to restrict access to authorized users.",
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
            "title": "Disposal",
            "description": "Implement policies and procedures to address the final disposition of ePHI, and/or the hardware or electronic media on which it is stored.",
            "specifications": "Required"
        },
        {
            "title": "Medical Re-use",
            "description": "Implement procedures for removal of ePHI from electronic media before the media are made available for re-use.",
            "specifications": "Required"
        },
        {
            "title": "Accountability",
            "description": "Maintain a record of the movements of hardware and electronic media and any person responsible therefore.",
            "specifications": "Addressable"
        },
        {
            "title": "Data Storage and Backup",
            "description": "ImpCreate a retrievable, exact copy of electronic protected health information, when needed, before movement of equipment.",
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
            "title": "Risk Analysis",
            "description": "Conduct an accurate and thorough assessment of the potential risks and vulnerabilities to the confidentiality, integrity, and availability of electronic PHI held by the covered entity.",
            "specifications": "Required"
        },
        {
            "title": "Risk Management",
            "description": "Implement security measures sufficient to reduce risks and vulnerabilities to a reasonable and appropriate level to comply with Sec. 164.306(a) [Security standards: General rules; (a) General requirements].",
            "specifications": "Required"
        },
        {
            "title": "Sanction Policy",
            "description": "Apply appropriate sanctions against workforce members who fail to comply with the security policies and procedures of the covered entity.",
            "specifications": "Required"
        },
        {
            "title": "Information System Activity Review",
            "description": "Implement procedures to regularly review records of information system activity, such as audit logs, access reports, and security incident tracking reports.",
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
            "title": "Assigned Security Responsibility",
            "description": "Identify the security official who is responsible for the development and implementation of the policies and procedures required by this subpart for the entity.",
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
            "title": "Termination Procedures",
            "description": "Implement procedures for the authorization and/or supervision of workforce members who work with electronic protected health information or in locations where it might be accessed.",
            "specifications": "Addressable"
        },
        {
            "title": "Workforce Clearance Procedures",
            "description": "Implement procedures to determine that the access of a workforce member to electronic protected health information is appropriate.",
            "specifications": "Addressable"
        },
        {
            "title": "Authorization and/or Supervision",
            "description": "Implement procedures for terminating access to electronic protected health information when the employment of a workforce member ends or as required by determinations made as specified in paragraph (a)(3)(ii)(B) [Workforce Clearance Procedures] of this section.",
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
            "title": "Isolating Health Care Clearinghouse Functions",
            "description": "If a health care clearinghouse is part of a larger organization, the clearinghouse must implement policies and procedures that protect the electronic protected health information of the clearinghouse from unauthorized access by the larger organization.",
            "specifications": "Required"
        },
        {
            "title": "Access Authorization",
            "description": "Implement policies and procedures for granting access to electronic protected health information, for example, through access to a workstation, transaction, program, process, or other mechanism.",
            "specifications": "Addressable"
        },
        {
            "title": "Access Establishment and Modification",
            "description": "Implement policies and procedures that, based upon the entity's access authorization policies, establish, document, review, and modify a user's right of access to a workstation, transaction, program, or process.",
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
            "title": "Security Reminders",
            "description": "Periodic security updates.",
            "specifications": "Addressable"
        },
        {
            "title": "Protection from Malicious Software",
            "description": "Procedures for guarding against, detecting, and reporting malicious software.",
            "specifications": "Addressable"
        },
        {
            "title": "Log-in Monitoring",
            "description": "Procedures for monitoring log-in attempts and reporting discrepancies.",
            "specifications": "Addressable"
        },
        {
            "title": "Password Management",
            "description": "Procedures for creating, changing, and safeguarding passwords.",
            "specifications": "Addressable"
        },
    ]
  },
  {
    "id": "164_308_a_6_",
    "code": "164.308(a)(6)",
    "safeguard": _("Administrative Safeguards"),
    "title": _("Security Incident Procedures"),
    "standards": [
        {
            "title": "Response and Report",
            "description": "Identify and respond to suspected or known security incidents; mitigate, to the extent practicable, harmful effects of security incidents that are known to the covered entity; and document security incidents and their outcomes.",
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
            "title": "Data Backup Plan",
            "description": "Establish and implement procedures to create and maintain retrievable exact copies of electronic protected health information.",
            "specifications": "Required"
        },
        {
            "title": "Disaster Recovery Plan",
            "description": "Establish (and implement as needed) procedures to restore any loss of data.",
            "specifications": "Required"
        },
        {
            "title": "Emergency Mode Operation Plan",
            "description": "Establish (and implement as needed) procedures to enable continuation of critical business processes for protection of the security of electronic PHI while operating in emergency mode.",
            "specifications": "Required"
        },
        {
            "title": "Testing and Revision Procedures",
            "description": "Implement procedures for periodic testing and revision of contingency plans.",
            "specifications": "Addressable"
        },
        {
            "title": "Applications and Data Criticality Analysis",
            "description": "Assess the relative criticality of specific applications and data in support of other contingency plan components.",
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
            "title": "Evaluation",
            "description": "Perform a periodic technical and non-technical evaluation, based initially upon the standards implemented under this rule and subsequently, in response to environmental or operational changes affecting the security of electronic PHI that establishes the extent to which an entity's security policies and procedures meet the requirements of this subpart.",
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
            "title": "Written Contract or Other Arrangement",
            "description": "A covered entity, in accordance with Â§ 164.306 [Security Standards: General Rules], may permit a business associate to create, receive, maintain, or transmit electronic protected health information on the covered entityâ€™s behalf only if the covered entity obtains satisfactory assurances, in accordance with Â§ 164.314(a) [Business Associate Contracts or Other Arrangements] that the business associate will appropriately safeguard the information. Document the satisfactory assurances required by paragraph (b)(1) [Business Associate Contracts and Other Arrangements] of this section through a written contract or other arrangement with the business associate that meets the applicable requirements of Â§ 164.314(a) [Business Associate Contracts or Other Arrangements].",
            "specifications": "Required"
        },
    ]
  },
]
