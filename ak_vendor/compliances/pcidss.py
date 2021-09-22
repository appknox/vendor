from gettext import gettext as _


data = [
    {
        "title": _(
            "Install and maintain a firewall and router configuration to protect"
            "cardholder data"
        ),
        "code": "1.1",
        "id": "1_1",
        "description": _(
            "Establish firewall and router configuration standards that formalize "
            "testing whenever configurations change; that identify all "
            "connections to cardholder data (including wireless); that use "
            "various technical settings for each implementation; and stipulate "
            "a review of configuration rule sets at least every six months."
        ),
    },
    {
        "title": _(
            "Install and maintain a firewall and router configuration to protect "
            "cardholder data"
        ),
        "code": "1.2",
        "id": "1_2",
        "description": _(
            "Build firewall and router configurations that restrict "
            "all traffic from untrusted networks and hosts, except for protocols "
            "necessary for the cardholder data environment."
        ),
    },
    {
        "title": _(
            "Install and maintain a firewall and router configuration to protect "
            "cardholder data"
        ),
        "code": "1.3",
        "id": "1_3",
        "description": _(
            "Prohibit direct public access between the Internet and any system "
            "component in the cardholder data environment."
        ),
    },
    {
        "title": _(
            "Install and maintain a firewall and router configuration to protect "
            "cardholder data"
        ),
        "code": "1.4",
        "id": "1_4",
        "description": _(
            "Install personal firewall software on any mobile and/or "
            "employee-owned computers with direct connectivity to the Internet "
            "that are used to access the organization's network"
        ),
    },
    {
        "title": _(
            "Do not use vendor-supplied defaults for system passwords and other "
            "security parameters"
        ),
        "code": "2.1",
        "id": "2_1",
        "description": _(
            "Always change vendor-supplied defaults before installing a system "
            "on the network. This includes wireless devices that are connected "
            "to the cardholder data environment or are used to transmit "
            "cardholder data"
        ),
    },
    {
        "title": _(
            "Do not use vendor-supplied defaults for system passwords and other "
            "security parameters"
        ),
        "code": "2.2",
        "id": "2_2",
        "description": _(
            "Develop configuration standards for all system components that "
            "address all known security vulnerabilities and are consistent with "
            "industry-accepted definitions. Update system configuration standards "
            "as new vulnerability issues are identified."
        ),
    },
    {
        "title": _(
            "Do not use vendor-supplied defaults for system passwords and other "
            "security parameters"
        ),
        "code": "2.3",
        "id": "2_3",
        "description": _(
            "Encrypt using strong cryptography all non-console administrative "
            "access such as browser/web- based management tools"
        ),
    },
    {
        "title": _(
            "Do not use vendor-supplied defaults for system passwords and other "
            "security parameters"
        ),
        "code": "2.4",
        "id": "2_4",
        "description": _(
            "Shared hosting providers must protect each entity's hosted "
            "environment and cardholder data (details are in PCI DSS Appendix A: "
            "Additional PCI DSS Requirements for Shared Hosting Providers.)"
        ),
    },
    {
        "title": _("Protect stored cardholder data"),
        "code": "3.1",
        "id": "3_1",
        "description": _(
            "Limit cardholder data storage and retention time to that required "
            "for business, legal, and/or regulatory purposes, as documented in "
            "your data retention policy. Purge unnecessary stored data at least "
            "quarterly."
        ),
    },
    {
        "title": _("Protect stored cardholder data"),
        "code": "3.2",
        "id": "3_2",
        "description": _(
            "Do not store sensitive authentication data after authorization"
            " (even if it is encrypted). See guidelines in table below. Issuers "
            "and related entities may store sensitive authentication data if "
            "there is a business justification, and the data is stored securely."
        ),
    },
    {
        "title": _("Protect stored cardholder data"),
        "code": "3.3",
        "id": "3_3",
        "description": _(
            "Mask PAN when displayed; the first six and last four digits are the "
            "maximum number of digits you may display. Not applicable for "
            "authorized people with a legitimate business need to see the full "
            "PAN. Does not supersede stricter requirements in place for displays "
            "of cardholder data such as on a point-of-sale receipt."
        ),
    },
    {
        "title": _("Protect stored cardholder data"),
        "code": "3.4",
        "id": "3_4",
        "description": _(
            "Render PAN unreadable anywhere it is stored including on portable "
            "digital media, backup media, in logs, and data received from or "
            "stored by wireless networks. Technology solutions for this "
            "requirement may include strong one-way hash functions of the "
            "entire PAN, truncation, index tokens with securely stored pads, "
            "or strong cryptography. (See PCI DSS Glossary for definition of "
            "strong cryptography.)"
        ),
    },
    {
        "title": _("Protect stored cardholder data"),
        "code": "3.5",
        "id": "3_5",
        "description": _(
            "Protect any keys used for encryption of cardholder data from "
            "disclosure and misuse"
        ),
    },
    {
        "title": _("Protect stored cardholder data"),
        "code": "3.6",
        "id": "3_6",
        "description": _(
            "Fully document and implement all appropriate key management "
            "processes and procedures for cryptographic keys used for encryption "
            "of cardholder data"
        ),
    },
    {
        "title": _(
            "Encrypt transmission of cardholder data across open, public networks"
        ),
        "code": "4.1",
        "id": "4_1",
        "description": _(
            "Use strong cryptography and security protocols such as SSL/TLS, SSH "
            "or IPSec to safeguard sensitive cardholder data during transmission "
            "over open, public networks (e.g. Internet, wireless technologies, "
            "Global System for Mobile communications [GSM], General Packet Radio "
            "Service [GPRS]). Ensure wireless networks transmitting cardholder "
            "data or connected to the cardholder data environment use industry "
            "best practices (e.g., IEEE 802.11i) to implement strong encryption "
            "for authentication and transmission. The use of WEP as a security "
            "control is prohibited"
        ),
    },
    {
        "title": _(
            "Encrypt transmission of cardholder data across open, public networks"
        ),
        "code": "4.2",
        "id": "4_2",
        "description": _(
            "Never send unprotected PANs by end user messaging technologies"
        ),
    },
    {
        "title": _("Use and regularly update anti-virus software or programs"),
        "code": "5.1",
        "id": "5_1",
        "description": _(
            "Deploy anti-virus software on all systems affected by malicious "
            "software (particularly personal computers and servers)"
        ),
    },
    {
        "title": _("Use and regularly update anti-virus software or programs"),
        "code": "5.2",
        "id": "5_2",
        "description": _(
            "Ensure that all anti-virus mechanisms are current, actively running, "
            "and generating audit logs"
        ),
    },
    {
        "title": _("Develop and maintain secure systems and applications"),
        "code": "6.1",
        "id": "6_1",
        "description": _(
            "Ensure that all system components and software are protected from "
            "known vulnerabilities by having the latest vendor-supplied security "
            "patches installed. Deploy critical patches within a month of release"
        ),
    },
    {
        "title": _("Develop and maintain secure systems and applications"),
        "code": "6.2",
        "id": "6_2",
        "description": _(
            "Establish a process to identify and assign a risk ranking to newly "
            "discovered security vulnerabilities. Risk rankings should be based "
            "on industry best practices and guidelines."
        ),
    },
    {
        "title": _("Develop and maintain secure systems and applications"),
        "code": "6.3",
        "id": "6_3",
        "description": _(
            "Develop software applications (internal and external, and including "
            "web-based administrative access) in accordance with PCI DSS and "
            "based on industry best practices. Incorporate information security "
            "throughout the software development life cycle."
        ),
    },
    {
        "title": _("Develop and maintain secure systems and applications"),
        "code": "6.4",
        "id": "6_4",
        "description": _(
            "Follow change control processes and procedures for all changes to "
            "system components"
        ),
    },
    {
        "title": _("Develop and maintain secure systems and applications"),
        "code": "6.5",
        "id": "6_5",
        "description": _(
            "Develop applications based on secure coding guidelines and review "
            "custom application code to identify coding vulnerabilities. "
            "Follow up-to-date industry best practices to identify and manage "
            "vulnerabilities."
        ),
    },
    {
        "title": _("Develop and maintain secure systems and applications"),
        "code": "6.6",
        "id": "6_6",
        "description": _(
            "Ensure all public-facing web applications are protected against "
            "known attacks, either by performing code vulnerability reviews at "
            "least annually or by installing a web application firewall in front "
            "of public-facing web applications"
        ),
    },
    {
        "title": _("Restrict access to cardholder data by business need to know"),
        "code": "7.1",
        "id": "7_1",
        "description": _(
            "Limit access to system components and cardholder data to only those "
            "individuals whose job requires such access."
        ),
    },
    {
        "title": _("Restrict access to cardholder data by business need to know"),
        "code": "7.2",
        "id": "7_2",
        "description": _(
            "Establish an access control system for systems components with "
            "multiple users that restricts access based on a user's need to know, "
            "and is set to deny all unless specifically allowed"
        ),
    },
    {
        "title": _("Assign a unique ID to each person with computer access"),
        "code": "8.1",
        "id": "8_1",
        "description": _(
            "Assign all users a unique user name before allowing them to access "
            "system components or cardholder data."
        ),
    },
    {
        "title": _("Assign a unique ID to each person with computer access"),
        "code": "8.2",
        "id": "8_2",
        "description": _(
            "Employ at least one of these to authenticate all users: something "
            "you know, such as a password or passphrase; something you have, "
            "such as a token device or smart card; or something you are, "
            "such as a biometric"
        ),
    },
    {
        "title": _("Assign a unique ID to each person with computer access"),
        "code": "8.3",
        "id": "8_3",
        "description": _(
            "Implement two-factor authentication for remote access to the network "
            "by employees, administrators, and third parties. For example, use "
            "technologies such as remote authentication and dialin service "
            "(RADIUS) with tokens; terminal access controller access control "
            "system (TACACS) with tokens; or other technologies that facilitate "
            "two-factor authentication. Using one factor twice (e.g. using two "
            "separate passwords) is not considered two-factor authentication"
        ),
    },
    {
        "title": _("Assign a unique ID to each person with computer access"),
        "code": "8.4",
        "id": "8_4",
        "description": _(
            "Render all passwords unreadable during storage and transmission, "
            "for all system components, by using strong cryptography."
        ),
    },
    {
        "title": _("Assign a unique ID to each person with computer access"),
        "code": "8.5",
        "id": "8_5",
        "description": _(
            "Ensure proper user identification and authentication management for "
            "non-consumer users and administrators on all system components"
        ),
    },
    {
        "title": _("Assign a unique ID to each person with computer access"),
        "code": "8.6",
        "id": "8_6",
        "description": _(
            "Use of other authentication mechanisms such as physical security tokens, "
            "smart cards, and certificates must be assigned to an individual account."
        ),
    },
    {
        "title": _("Assign a unique ID to each person with computer access"),
        "code": "8.7",
        "id": "8_7",
        "description": _(
            "All access to any database containing cardholder data must be restricted: "
            "all user access must be through programmatic methods; only database "
            "administrators can have direct or query access; and application IDs for "
            "database applications can only be used by the applications (and not by "
            "users or non-application processes)."
        ),
    },
    {
        "title": _("Assign a unique ID to each person with computer access"),
        "code": "8.8",
        "id": "8_8",
        "description": _(
            "Ensure that related security policies and operational procedures are "
            "documented, in use, and known to all affected parties."
        ),
    },
    {
        "title": _("Restrict physical access to cardholder data"),
        "code": "9.1",
        "id": "9_1",
        "description": _(
            "Use appropriate facility entry controls to limit and monitor "
            "physical access to systems in the cardholder data environment"
        ),
    },
    {
        "title": _("Restrict physical access to cardholder data"),
        "code": "9.2",
        "id": "9_2",
        "description": _(
            "Develop procedures to easily distinguish between onsite personnel "
            "and visitors, especially in areas where cardholder data is accessible"
        ),
    },
    {
        "title": _("Restrict physical access to cardholder data"),
        "code": "9.3",
        "id": "9_3",
        "description": _(
            "Ensure all visitors are authorized before entering areas where "
            "cardholder data is processed or maintained; given a physical token "
            "that expires and that identifies visitors as not onsite personnel; "
            "and are asked to surrender the physical token before leaving the "
            "facility or at the date of expiration."
        ),
    },
    {
        "title": _("Restrict physical access to cardholder data"),
        "code": "9.4",
        "id": "9_4",
        "description": _(
            "Use a visitor log to maintain a physical audit trail of visitor "
            "information and activity, including visitor name and company, and "
            "the onsite personnel authorizing physical access. Retain the log "
            "for at least three months unless otherwise restricted by law."
        ),
    },
    {
        "title": _("Restrict physical access to cardholder data"),
        "code": "9.5",
        "id": "9_5",
        "description": _(
            "Store media back-ups in a secure location, preferably off site."
        ),
    },
    {
        "title": _("Restrict physical access to cardholder data"),
        "code": "9.6",
        "id": "9_6",
        "description": _("Physically secure all media."),
    },
    {
        "title": _("Restrict physical access to cardholder data"),
        "code": "9.7",
        "id": "9_7",
        "description": _(
            "Maintain strict control over the internal or external distribution "
            "of any kind of media. Classify media so the sensitivity of the data "
            "can be determined."
        ),
    },
    {
        "title": _("Restrict physical access to cardholder data"),
        "code": "9.8",
        "id": "9_8",
        "description": _(
            "Ensure that management approves any and all media moved from a "
            "secured area, especially when media is distributed to individuals"
        ),
    },
    {
        "title": _("Restrict physical access to cardholder data"),
        "code": "9.9",
        "id": "9_9",
        "description": _(
            "Maintain strict control over the storage and accessibility of media"
        ),
    },
    {
        "title": _("Restrict physical access to cardholder data"),
        "code": "9.10",
        "id": "9_10",
        "description": _(
            "Destroy media when it is no longer needed for business or legal " "reasons"
        ),
    },
    {
        "title": _(
            "Track and monitor all access to network resources and cardholder  " "data"
        ),
        "code": "10.1",
        "id": "10_1",
        "description": _(
            "Establish a process for linking all access to system components "
            "to each individual user especially access done with administrative "
            "privileges."
        ),
    },
    {
        "title": _(
            "Track and monitor all access to network resources and cardholder  " "data"
        ),
        "code": "10.2",
        "id": "10_2",
        "description": _(
            "Implement automated audit trails for all system components for "
            "reconstructing these events: all individual user accesses to "
            "cardholder data; all actions taken by any individual with root or "
            "administrative privileges; access to all audit trails; invalid "
            "logical access attempts; use of identification and authentication "
            "mechanisms; initialization of the audit logs; creation and "
            "deletion of system-level objects"
        ),
    },
    {
        "title": _(
            "Track and monitor all access to network resources and cardholder  " "data"
        ),
        "code": "10.3",
        "id": "10_3",
        "description": _(
            "Record audit trail entries for all system components for each event, "
            "including at a minimum: user identification, type of event, date and "
            "time, success or failure indication, origination of event, and "
            "identity or name of affected data, system component or resource. "
        ),
    },
    {
        "title": _(
            "Track and monitor all access to network resources and cardholder  " "data"
        ),
        "code": "10.4",
        "id": "10_4",
        "description": _(
            "Using time synchronization technology, synchronize all critical "
            "system clocks and times and implement controls for acquiring, "
            "distributing, and storing time."
        ),
    },
    {
        "title": _(
            "Track and monitor all access to network resources and cardholder  " "data"
        ),
        "code": "10.5",
        "id": "10_5",
        "description": _("Secure audit trails so they cannot be altered."),
    },
    {
        "title": _(
            "Track and monitor all access to network resources and cardholder  " "data"
        ),
        "code": "10.6",
        "id": "10_6",
        "description": _(
            "Review logs for all system components related to security functions "
            "at least daily"
        ),
    },
    {
        "title": _(
            "Track and monitor all access to network resources and cardholder  " "data"
        ),
        "code": "10.7",
        "id": "10_7",
        "description": _(
            "Retain audit trail history for at least one year; at least three "
            "months of history must be immediately available for analysis"
        ),
    },
    {
        "title": _("Regularly test security systems and processes"),
        "code": "11.1",
        "id": "11_1",
        "description": _(
            "Test for the presence of wireless access points and detect "
            "unauthorized wireless access points on a quarterly basis. "
            "Typical methods are wireless network scans, physical/logical "
            "inspections of system components and infrastructure, network "
            "access control (NAC), or wireless IDS/IPS. "
        ),
    },
    {
        "title": _("Regularly test security systems and processes"),
        "code": "11.2",
        "id": "11_2",
        "description": _(
            "Run internal and external network vulnerability scans at least "
            "quarterly and after any significant change in the network. After "
            "passing a scan for initial PCI DSS compliance, an entity must, in "
            "subsequent years, pass four consecutive quarterly scans as a "
            "requirement for compliance. Quarterly external scans must be "
            "performed by an Approved Scanning Vendor (ASV). Scans conducted "
            "after network changes may be performed by internal staff"
        ),
    },
    {
        "title": _("Regularly test security systems and processes"),
        "code": "11.3",
        "id": "11_3",
        "description": _(
            "Perform external and internal penetration testing, including "
            "network- and application-layer penetration tests, at least "
            "annually and after any significant infrastructure or application "
            "upgrade or modification."
        ),
    },
    {
        "title": _("Regularly test security systems and processes"),
        "code": "11.4",
        "id": "11_4",
        "description": _(
            "Use network intrusion detection systems and/or intrusion prevention "
            "systems to monitor all traffic at the perimeter of the cardholder "
            "data environment as well as at critical points inside of the "
            "cardholder data environment, and alert personnel to suspected "
            "compromises. IDS/IPS engines, baselines, and signatures must be "
            "kept up to date"
        ),
    },
    {
        "title": _("Regularly test security systems and processes"),
        "code": "11.5",
        "id": "11_5",
        "description": _(
            "Deploy file integrity monitoring tools to alert personnel to "
            "unauthorized modification of critical system files, configuration "
            "files or content files. Configure the software to perform critical "
            "file comparisons at least weekly"
        ),
    },
    {
        "title": _(
            "Maintain a policy that addresses information security for all " "personnel"
        ),
        "code": "12.1",
        "id": "12_1",
        "description": _(
            "Establish, publish, maintain, and disseminate a security policy "
            "that addresses all PCI DSS requirements, includes an annual "
            "process for identifying vulnerabilities and formally assessing "
            "risks, and includes a review at least once a year and when the "
            "environment changes"
        ),
    },
    {
        "title": _(
            "Maintain a policy that addresses information security for all " "personnel"
        ),
        "code": "12.2",
        "id": "12_2",
        "description": _(
            "Develop daily operational security procedures that are consistent "
            "with requirements in PCI DSS"
        ),
    },
    {
        "title": _(
            "Maintain a policy that addresses information security for all " "personnel"
        ),
        "code": "12.3",
        "id": "12_3",
        "description": _(
            "Develop usage policies for critical technologies to define their "
            "proper use by all personnel. These include remote access, wireless, "
            "removable electronic media, laptops, tablets, handheld devices, "
            "email and Internet"
        ),
    },
    {
        "title": _(
            "Maintain a policy that addresses information security for all " "personnel"
        ),
        "code": "12.4",
        "id": "12_4",
        "description": _(
            "Ensure that the security policy and procedures clearly define "
            "information security responsibilities for all personnel."
        ),
    },
    {
        "title": _(
            "Maintain a policy that addresses information security for all " "personnel"
        ),
        "code": "12.5",
        "id": "12_5",
        "description": _(
            "Assign to an individual or team information security "
            "responsibilities defined by 12.5 subsections."
        ),
    },
    {
        "title": _(
            "Maintain a policy that addresses information security for all " "personnel"
        ),
        "code": "12.6",
        "id": "12_6",
        "description": _(
            "Implement a formal security awareness program to make all "
            "personnel aware of the importance of cardholder data security"
        ),
    },
    {
        "title": _(
            "Maintain a policy that addresses information security for all " "personnel"
        ),
        "code": "12.7",
        "id": "12_7",
        "description": _(
            "Screen potential personnel prior to hire to minimize the risk of "
            "attacks from internal sources. Example screening includes previous "
            "employment history, criminal record, credit history, and reference "
            "checks"
        ),
    },
    {
        "title": _(
            "Maintain a policy that addresses information security for all " "personnel"
        ),
        "code": "12.8",
        "id": "12_8",
        "description": _(
            "If cardholder data is shared with service providers, maintain "
            "policies and procedures to formally identify service provider "
            "responsibilities for securing cardholder data, and monitor service "
            "providers' PCI DSS compliance status at least annually"
        ),
    },
    {
        "title": _(
            "Maintain a policy that addresses information security for all " "personnel"
        ),
        "code": "12.9",
        "id": "12_9",
        "description": _(
            "Implement an incident response plan. Be prepared to respond "
            "immediately to a system breach."
        ),
    },
]


class PCIDSS:
    def __init__(self, id, code, title, description, active=True):
        self.pk = id
        self.id = id
        self.title = title
        self.code = code
        self.description = description
        self.active = active

    def __str__(self):
        return "%s - %s - %s - %s" % (self.id, self.code, self.title, self.description)

    def __repr__(self):
        return "<PCIDSS: %s>" % self.__str__()


PCIDSS_DATA = {d["id"]: PCIDSS(**d) for d in data}
