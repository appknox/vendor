from gettext import gettext as _


data = [
    # Reference: https://mobile-security.gitbook.io/masvs/security
    # -requirements/0x06-v1-architecture_design_and_threat_modelling_requireme
    {
        "id": "MSTG_1_1",
        "code": "MSTG-ARCH-1",
        "title": _("All app components are identified and known to be needed."),
        "active": True,
    },
    {
        "id": "MSTG_1_2",
        "code": "MSTG-ARCH-2",
        "title": _(
            "Security controls are never enforced only on the client "
            "side, but on the respective remote endpoints."
        ),
        "active": True,
    },
    {
        "id": "MSTG_1_3",
        "code": "MSTG-ARCH-3",
        "title": _(
            "A high-level architecture for the mobile app and all "
            "connected remote services has been defined and security "
            "has been addressed in that architecture."
        ),
        "active": True,
    },
    {
        "id": "MSTG_1_4",
        "code": "MSTG-ARCH-4",
        "title": _(
            "Data considered sensitive in the context of the mobile app "
            "is clearly identified."
        ),
        "active": True,
    },
    {
        "id": "MSTG_1_5",
        "code": "MSTG-ARCH-5",
        "title": _(
            "All app components are defined in terms of the business "
            "functions and/or security functions they provide."
        ),
        "active": True,
    },
    {
        "id": "MSTG_1_6",
        "code": "MSTG-ARCH-6",
        "title": _(
            "A threat model for the mobile app and the associated remote "
            "services has been produced that identifies potential "
            "threats and countermeasures."
        ),
        "active": True,
    },
    {
        "id": "MSTG_1_7",
        "code": "MSTG-ARCH-7",
        "title": _("All security controls have a centralized implementation."),
        "active": True,
    },
    {
        "id": "MSTG_1_8",
        "code": "MSTG-ARCH-8",
        "title": _(
            "There is an explicit policy for how cryptographic keys "
            "(if any) are managed, and the lifecycle of cryptographic "
            "keys is enforced. Ideally, follow a key management standard "
            "such as NIST SP 800-57."
        ),
        "active": True,
    },
    {
        "id": "MSTG_1_9",
        "code": "MSTG-ARCH-9",
        "title": _("A mechanism for enforcing updates of the mobile app exists."),
        "active": True,
    },
    {
        "id": "MSTG_1_10",
        "code": "MSTG-ARCH-10",
        "title": _(
            "Security is addressed within all parts of the software "
            "development lifecycle."
        ),
        "active": True,
    },
    {
        "id": "MSTG_1_11",
        "code": "MSTG-ARCH-11",
        "title": _(
            "A responsible disclosure policy is in place and effectively applied."
        ),
        "active": True,
    },
    {
        "id": "MSTG_1_12",
        "code": "MSTG-ARCH-12",
        "title": _("The app should comply with privacy laws and regulations."),
        "active": True,
    },
    # Reference: https://mobile-security.gitbook.io/masvs/security-requirements/
    # 0x07-v2-data_storage_and_privacy_requirements
    {
        "id": "MSTG_2_1",
        "code": "MSTG-STORAGE-1",
        "title": _(
            "System credential storage facilities need to be used to "
            "store sensitive data, such as PII, user credentials or "
            "cryptographic keys."
        ),
        "active": True,
    },
    {
        "id": "MSTG_2_2",
        "code": "MSTG-STORAGE-2",
        "title": _(
            "No sensitive data should be stored outside of the app "
            "container or system credential storage facilities."
        ),
        "active": True,
    },
    {
        "id": "MSTG_2_3",
        "code": "MSTG-STORAGE-3",
        "title": _("No sensitive data is written to application logs."),
        "active": True,
    },
    {
        "id": "MSTG_2_4",
        "code": "MSTG-STORAGE-4",
        "title": _(
            "No sensitive data is shared with third parties unless it is "
            "a necessary part of the architecture."
        ),
        "active": True,
    },
    {
        "id": "MSTG_2_5",
        "code": "MSTG-STORAGE-5",
        "title": _(
            "The keyboard cache is disabled on text inputs that process "
            "sensitive data."
        ),
        "active": True,
    },
    {
        "id": "MSTG_2_6",
        "code": "MSTG-STORAGE-6",
        "title": _("No sensitive data is exposed via IPC mechanisms."),
        "active": True,
    },
    {
        "id": "MSTG_2_7",
        "code": "MSTG-STORAGE-7",
        "title": _(
            "No sensitive data, such as passwords or pins, is exposed "
            "through the user interface."
        ),
        "active": True,
    },
    {
        "id": "MSTG_2_8",
        "code": "MSTG-STORAGE-8",
        "title": _(
            "No sensitive data is included in backups generated by the "
            "mobile operating system."
        ),
        "active": True,
    },
    {
        "id": "MSTG_2_9",
        "code": "MSTG-STORAGE-9",
        "title": _(
            "The app removes sensitive data from views when moved to the background."
        ),
        "active": True,
    },
    {
        "id": "MSTG_2_10",
        "code": "MSTG-STORAGE-10",
        "title": _(
            "The app does not hold sensitive data in memory longer than "
            "necessary, and memory is cleared explicitly after use."
        ),
        "active": True,
    },
    {
        "id": "MSTG_2_11",
        "code": "MSTG-STORAGE-11",
        "title": _(
            "The app enforces a minimum device-access-security policy, "
            "such as requiring the user to set a device passcode."
        ),
        "active": True,
    },
    {
        "id": "MSTG_2_12",
        "code": "MSTG-STORAGE-12",
        "title": _(
            "The app educates the user about the types of personally "
            "identifiable information processed, as well as security "
            "best practices the user should follow in using the app."
        ),
        "active": True,
    },
    {
        "id": "MSTG_2_13",
        "code": "MSTG-STORAGE-13",
        "title": _(
            "No sensitive data should be stored locally on the mobile "
            "device. Instead, data should be retrieved from a remote "
            "endpoint when needed and only be kept in memory."
        ),
        "active": True,
    },
    {
        "id": "MSTG_2_14",
        "code": "MSTG-STORAGE-14",
        "title": _(
            "If sensitive data is still required to be stored locally, it "
            "should be encrypted using a key derived from hardware backed "
            "storage which requires authentication."
        ),
        "active": True,
    },
    {
        "id": "MSTG_2_15",
        "code": "MSTG-STORAGE-15",
        "title": _(
            "The app’s local storage should be wiped after an excessive "
            "number of failed authentication attempts."
        ),
        "active": True,
    },
    # Reference: https://mobile-security.gitbook.io/masvs/security-requirements/
    # 0x08-v3-cryptography_verification_requirements
    {
        "id": "MSTG_3_1",
        "code": "MSTG-CRYPTO-1",
        "title": _(
            "The app does not rely on symmetric cryptography with "
            "hardcoded keys as a sole method of encryption."
        ),
        "active": True,
    },
    {
        "id": "MSTG_3_2",
        "code": "MSTG-CRYPTO-2",
        "title": _("The app uses proven implementations of cryptographic primitives."),
        "active": True,
    },
    {
        "id": "MSTG_3_3",
        "code": "MSTG-CRYPTO-3",
        "title": _(
            "The app uses cryptographic primitives that are appropriate "
            "for the particular use-case, configured with parameters "
            "that adhere to industry best practices."
        ),
        "active": True,
    },
    {
        "id": "MSTG_3_4",
        "code": "MSTG-CRYPTO-4",
        "title": _(
            "The app does not use cryptographic protocols or algorithms "
            "that are widely considered deprecated for security purposes."
        ),
        "active": True,
    },
    {
        "id": "MSTG_3_5",
        "code": "MSTG-CRYPTO-5",
        "title": _(
            "The app doesn't re-use the same cryptographic key for "
            "multiple purposes."
        ),
        "active": True,
    },
    {
        "id": "MSTG_3_6",
        "code": "MSTG-CRYPTO-6",
        "title": _(
            "All random values are generated using a sufficiently secure "
            "random number generator."
        ),
        "active": True,
    },
    # Reference: https://mobile-security.gitbook.io/masvs/security-requirements/
    # 0x09-v4-authentication_and_session_management_requirements
    {
        "id": "MSTG_4_1",
        "code": "MSTG-AUTH-1",
        "title": _(
            "If the app provides users access to a remote service, some "
            "form of authentication, such as username/password "
            "authentication, is performed at the remote endpoint."
        ),
        "active": True,
    },
    {
        "id": "MSTG_4_2",
        "code": "MSTG-AUTH-2",
        "title": _(
            "If stateful session management is used, the remote endpoint "
            "uses randomly generated session identifiers to authenticate "
            "client requests without sending the user's credentials."
        ),
        "active": True,
    },
    {
        "id": "MSTG_4_3",
        "code": "MSTG-AUTH-3",
        "title": _(
            "If stateless token-based authentication is used, the server "
            "provides a token that has been signed using a secure "
            "algorithm."
        ),
        "active": True,
    },
    {
        "id": "MSTG_4_4",
        "code": "MSTG-AUTH-4",
        "title": _(
            "The remote endpoint terminates the existing session when "
            "the user logs out."
        ),
        "active": True,
    },
    {
        "id": "MSTG_4_5",
        "code": "MSTG-AUTH-5",
        "title": _("A password policy exists and is enforced at the remote endpoint."),
        "active": True,
    },
    {
        "id": "MSTG_4_6",
        "code": "MSTG-AUTH-6",
        "title": _(
            "The remote endpoint implements a mechanism to protect "
            "against the submission of credentials an excessive number "
            "of times."
        ),
        "active": True,
    },
    {
        "id": "MSTG_4_7",
        "code": "MSTG-AUTH-7",
        "title": _(
            "Sessions are invalidated at the remote endpoint after a "
            "predefined period of inactivity and access tokens expire."
        ),
        "active": True,
    },
    {
        "id": "MSTG_4_8",
        "code": "MSTG-AUTH-8",
        "title": _(
            "Biometric authentication, if any, is not event-bound (i.e. "
            'using an API that simply returns "true" or "false"). '
            "Instead, it is based on unlocking the keychain/keystore."
        ),
        "active": True,
    },
    {
        "id": "MSTG_4_9",
        "code": "MSTG-AUTH-9",
        "title": _(
            "A second factor of authentication exists at the remote "
            "endpoint and the 2FA requirement is consistently enforced."
        ),
        "active": True,
    },
    {
        "id": "MSTG_4_10",
        "code": "MSTG-AUTH-10",
        "title": _("Sensitive transactions require step-up authentication."),
        "active": True,
    },
    {
        "id": "MSTG_4_11",
        "code": "MSTG-AUTH-11",
        "title": _(
            "The app informs the user of all sensitive activities with "
            "their account. Users are able to view a list of devices, "
            "view contextual information (IP address, location, etc.), "
            "and to block specific devices."
        ),
        "active": True,
    },
    {
        "id": "MSTG_4_12",
        "code": "MSTG-AUTH-12",
        "title": _(
            "Authorization models should be defined and enforced at the "
            "remote endpoint."
        ),
        "active": True,
    },
    # Reference: https://mobile-security.gitbook.io/masvs/security-requirements/
    # 0x10-v5-network_communication_requirements
    {
        "id": "MSTG_5_1",
        "code": "MSTG-NETWORK-1",
        "title": _(
            "Data is encrypted on the network using TLS. The secure "
            "channel is used consistently throughout the app."
        ),
        "active": True,
    },
    {
        "id": "MSTG_5_2",
        "code": "MSTG-NETWORK-2",
        "title": _(
            "The TLS settings are in line with current best practices, "
            "or as close as possible if the mobile operating system does "
            "not support the recommended standards."
        ),
        "active": True,
    },
    {
        "id": "MSTG_5_3",
        "code": "MSTG-NETWORK-3",
        "title": _(
            "The app verifies the X.509 certificate of the remote "
            "endpoint when the secure channel is established. Only "
            "certificates signed by a trusted CA are accepted."
        ),
        "active": True,
    },
    {
        "id": "MSTG_5_4",
        "code": "MSTG-NETWORK-4",
        "title": _(
            "The app either uses its own certificate store, or pins the "
            "endpoint certificate or public key, and subsequently does "
            "not establish connections with endpoints that offer a "
            "different certificate or key, even if signed by a trusted "
            "CA."
        ),
        "active": True,
    },
    {
        "id": "MSTG_5_5",
        "code": "MSTG-NETWORK-5",
        "title": _(
            "The app doesn't rely on a single insecure communication "
            "channel (email or SMS) for critical operations, such as "
            "enrollments and account recovery."
        ),
        "active": True,
    },
    {
        "id": "MSTG_5_6",
        "code": "MSTG-NETWORK-6",
        "title": _(
            "The app only depends on up-to-date connectivity and security libraries."
        ),
        "active": True,
    },
    # Reference: https://mobile-security.gitbook.io/masvs/security-requirements/
    # 0x11-v6-interaction_with_the_environment
    {
        "id": "MSTG_6_1",
        "code": "MSTG-PLATFORM-1",
        "title": _("The app only requests the minimum set of permissions necessary."),
        "active": True,
    },
    {
        "id": "MSTG_6_2",
        "code": "MSTG-PLATFORM-2",
        "title": _(
            "All inputs from external sources and the user are validated "
            "and if necessary sanitized. This includes data received via "
            "the UI, IPC mechanisms such as intents, custom URLs, and "
            "network sources."
        ),
        "active": True,
    },
    {
        "id": "MSTG_6_3",
        "code": "MSTG-PLATFORM-3",
        "title": _(
            "The app does not export sensitive functionality via custom "
            "URL schemes, unless these mechanisms are properly protected."
        ),
        "active": True,
    },
    {
        "id": "MSTG_6_4",
        "code": "MSTG-PLATFORM-4",
        "title": _(
            "The app does not export sensitive functionality through IPC "
            "facilities, unless these mechanisms are properly protected."
        ),
        "active": True,
    },
    {
        "id": "MSTG_6_5",
        "code": "MSTG-PLATFORM-5",
        "title": _("JavaScript is disabled in WebViews unless explicitly required."),
        "active": True,
    },
    {
        "id": "MSTG_6_6",
        "code": "MSTG-PLATFORM-6",
        "title": _(
            "WebViews are configured to allow only the minimum set of "
            "protocol handlers required (ideally, only https is "
            "supported). Potentially dangerous handlers, such as file, "
            "tel and app-id, are disabled."
        ),
        "active": True,
    },
    {
        "id": "MSTG_6_7",
        "code": "MSTG-PLATFORM-7",
        "title": _(
            "If native methods of the app are exposed to a WebView, "
            "verify that the WebView only renders JavaScript contained "
            "within the app package."
        ),
        "active": True,
    },
    {
        "id": "MSTG_6_8",
        "code": "MSTG-PLATFORM-8",
        "title": _(
            "Object deserialization, if any, is implemented using safe "
            "serialization APIs."
        ),
        "active": True,
    },
    {
        "id": "MSTG_6_9",
        "code": "MSTG-PLATFORM-9",
        "title": _(
            "The app protects itself against screen overlay attacks. (Android only)"
        ),
        "active": True,
    },
    {
        "id": "MSTG_6_10",
        "code": "MSTG-PLATFORM-10",
        "title": _(
            "A WebView's cache, storage, and loaded resources "
            "(JavaScript, etc.) should be cleared before the WebView is "
            "destroyed."
        ),
        "active": True,
    },
    {
        "id": "MSTG_6_11",
        "code": "MSTG-PLATFORM-11",
        "title": _(
            "Verify that the app prevents usage of custom third-party "
            "keyboards whenever sensitive data is entered (iOS only)."
        ),
        "active": True,
    },
    # Reference: https://mobile-security.gitbook.io/masvs/security-requirements/
    # 0x12-v7-code_quality_and_build_setting_requirements
    {
        "id": "MSTG_7_1",
        "code": "MSTG-CODE-1",
        "title": _(
            "The app is signed and provisioned with a valid certificate, "
            "of which the private key is properly protected."
        ),
        "active": True,
    },
    {
        "id": "MSTG_7_2",
        "code": "MSTG-CODE-2",
        "title": _(
            "The app has been built in release mode, with settings "
            "appropriate for a release build (e.g. non-debuggable)."
        ),
        "active": True,
    },
    {
        "id": "MSTG_7_3",
        "code": "MSTG-CODE-3",
        "title": _("Debugging symbols have been removed from native binaries."),
        "active": True,
    },
    {
        "id": "MSTG_7_4",
        "code": "MSTG-CODE-4",
        "title": _(
            "Debugging code and developer assistance code (e.g. test "
            "code, backdoors, hidden settings) have been removed. The "
            "app does not log verbose errors or debugging messages."
        ),
        "active": True,
    },
    {
        "id": "MSTG_7_5",
        "code": "MSTG-CODE-5",
        "title": _(
            "All third party components used by the mobile app, such as "
            "libraries and frameworks, are identified, and checked for "
            "known vulnerabilities."
        ),
        "active": True,
    },
    {
        "id": "MSTG_7_6",
        "code": "MSTG-CODE-6",
        "title": _("The app catches and handles possible exceptions."),
        "active": True,
    },
    {
        "id": "MSTG_7_7",
        "code": "MSTG-CODE-7",
        "title": _(
            "Error handling logic in security controls denies access by default."
        ),
        "active": True,
    },
    {
        "id": "MSTG_7_8",
        "code": "MSTG-CODE-8",
        "title": _("In unmanaged code, memory is allocated, freed and used securely."),
        "active": True,
    },
    {
        "id": "MSTG_7_9",
        "code": "MSTG-CODE-9",
        "title": _(
            "Free security features offered by the toolchain, such as "
            "byte-code minification, stack protection, PIE support and "
            "automatic reference counting, are activated."
        ),
        "active": True,
    },
    # Reference: https://mobile-security.gitbook.io/masvs/security-requirements/
    # 0x15-v8-resiliency_against_reverse_engineering_requirements
    {
        "id": "MSTG_8_1",
        "code": "MSTG-RESILIENCE-1",
        "title": _(
            "The app detects, and responds to, the presence of a rooted "
            "or jailbroken device either by alerting the user or "
            "terminating the app."
        ),
        "active": True,
    },
    {
        "id": "MSTG_8_2",
        "code": "MSTG-RESILIENCE-2",
        "title": _(
            "The app prevents debugging and/or detects, and responds to, "
            "a debugger being attached. All available debugging "
            "protocols must be covered."
        ),
        "active": True,
    },
    {
        "id": "MSTG_8_3",
        "code": "MSTG-RESILIENCE-3",
        "title": _(
            "The app detects, and responds to, tampering with executable "
            "files and critical data within its own sandbox."
        ),
        "active": True,
    },
    {
        "id": "MSTG_8_4",
        "code": "MSTG-RESILIENCE-4",
        "title": _(
            "The app detects, and responds to, the presence of widely "
            "used reverse engineering tools and frameworks on the device."
        ),
        "active": True,
    },
    {
        "id": "MSTG_8_5",
        "code": "MSTG-RESILIENCE-5",
        "title": _("The app detects, and responds to, being run in an emulator."),
        "active": True,
    },
    {
        "id": "MSTG_8_6",
        "code": "MSTG-RESILIENCE-6",
        "title": _(
            "The app detects, and responds to, tampering the code and "
            "data in its own memory space."
        ),
        "active": True,
    },
    {
        "id": "MSTG_8_7",
        "code": "MSTG-RESILIENCE-7",
        "title": _(
            "The app implements multiple mechanisms in each defense "
            "category (8.1 to 8.6). Note that resiliency scales with the "
            "amount, diversity of the originality of the mechanisms used."
        ),
        "active": True,
    },
    {
        "id": "MSTG_8_8",
        "code": "MSTG-RESILIENCE-8",
        "title": _(
            "The detection mechanisms trigger responses of different "
            "types, including delayed and stealthy responses."
        ),
        "active": True,
    },
    {
        "id": "MSTG_8_9",
        "code": "MSTG-RESILIENCE-9",
        "title": _(
            "Obfuscation is applied to programmatic defenses, which in "
            "turn impede de-obfuscation via dynamic analysis."
        ),
        "active": True,
    },
    {
        "id": "MSTG_8_10",
        "code": "MSTG-RESILIENCE-10",
        "title": _(
            "The app implements a 'device binding' functionality using a "
            "device fingerprint derived from multiple properties unique "
            "to the device."
        ),
        "active": True,
    },
    {
        "id": "MSTG_8_11",
        "code": "MSTG-RESILIENCE-11",
        "title": _(
            "All executable files and libraries belonging to the app are "
            "either encrypted on the file level and/or important code "
            "and data segments inside the executables are encrypted or "
            "packed. Trivial static analysis does not reveal important "
            "code or data."
        ),
        "active": True,
    },
    {
        "id": "MSTG_8_12",
        "code": "MSTG-RESILIENCE-12",
        "title": _(
            "If the goal of obfuscation is to protect sensitive "
            "computations, an obfuscation scheme is used that is both "
            "appropriate for the particular task and robust against "
            "manual and automated de-obfuscation methods, considering "
            "currently published research. The effectiveness of the "
            "obfuscation scheme must be verified through manual testing. "
            "Note that hardware-based isolation features are preferred "
            "over obfuscation whenever possible."
        ),
        "active": True,
    },
    {
        "id": "MSTG_8_13",
        "code": "MSTG-RESILIENCE-13",
        "title": _(
            "As a defense in depth, next to having solid hardening of "
            "the communicating parties, application level payload "
            "encryption can be applied to further impede eavesdropping."
        ),
        "active": True,
    },
]


class MSTG:
    def __init__(self, id, code, title, active=True):
        self.pk = id
        self.id = id
        self.title = title
        self.code = code
        self.active = active

    def __str__(self):
        return "%s - %s - %s" % (self.id, self.code, self.title)

    def __repr__(self):
        return "<MSTG: %s>" % self.__str__()


MSTG_DATA = {d["id"]: MSTG(**d) for d in data}
