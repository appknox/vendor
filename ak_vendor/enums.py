# (c) 2017, XYSec Labs

from orm_choices import choices_with_unknown as choices
from orm_choices import choices as choices_without_unknown


from ak_vendor.constants import RISK_ENUM_PASSED, RISK_ENUM_LOW, \
    RISK_ENUM_MEDIUM, RISK_ENUM_HIGH, RISK_ENUM_CRITICAL


@choices
class ProductEnum:
    class Meta:
        APPKNOX = [0, 'Appknox']
        DEVKNOX = [1, 'Devknox']


@choices
class AppactionEnum:
    class Meta:
        NO_PREFERENCE = [0, 'NO_PREFERENCE']
        HALT = [1, 'HALT']
        PROCEED = [2, 'PROCEED']


@choices
class OrganizationRolesEnum:
    class Meta:
        MEMBER = [0, 'MEMBER']
        OWNER = [1, 'OWNER']
        ADMIN = [2, 'ADMIN']


@choices_without_unknown
class OWASPEnum:
    """
    OWASP Enum
    """
    class Meta:
        A1_2013 = ['A1_2013', 'A1_2013']
        A2_2013 = ['A2_2013', 'A2_2013']
        A3_2013 = ['A3_2013', 'A3_2013']
        A4_2013 = ['A4_2013', 'A4_2013']
        A5_2013 = ['A5_2013', 'A5_2013']
        A6_2013 = ['A6_2013', 'A6_2013']
        A7_2013 = ['A7_2013', 'A7_2013']
        A8_2013 = ['A8_2013', 'A8_2013']
        A9_2013 = ['A9_2013', 'A9_2013']
        A10_2013 = ['A10_2013', 'A10_2013']

        M1_2016 = ['M1_2016', 'M1_2016']
        M2_2016 = ['M2_2016', 'M2_2016']
        M3_2016 = ['M3_2016', 'M3_2016']
        M4_2016 = ['M4_2016', 'M4_2016']
        M5_2016 = ['M5_2016', 'M5_2016']
        M6_2016 = ['M6_2016', 'M6_2016']
        M7_2016 = ['M7_2016', 'M7_2016']
        M8_2016 = ['M8_2016', 'M8_2016']
        M9_2016 = ['M9_2016', 'M9_2016']
        M10_2016 = ['M10_2016', 'M10_2016']


@choices
class PlatformEnum:
    '''
    Platform Type Enum
    '''
    class Meta:
        ANDROID = [0, 'Android']
        IOS = [1, 'iOS']
        WINDOWS = [2, 'Windows']
        COMMON = [3, 'common (meta)']


@choices
class DeviceTypeEnum:
    """
    Device type enum
    """
    class Meta:
        NO_PREFERENCE = [0, 'No Preference']
        PHONE_REQUIRED = [1, 'Phone Required']
        TABLET_REQUIRED = [2, 'Tablet Required']


@choices_without_unknown
class DynamicStatusEnum:
    '''
    The Dynamic scanning status
    '''
    class Meta:
        ERROR = [-1, 'Error']
        NONE = [0, 'None']
        INQUEUE = [1, 'In Queue']
        BOOTING = [2, 'Booting']
        DOWNLOADING = [3, 'Downloading Package']
        INSTALLING = [4, 'Installing Package']
        LAUNCHING = [5, 'Launching App']
        HOOKING = [6, 'Hooking']
        READY = [7, 'Ready']
        SHUTTING_DOWN = [8, 'Shutting Down']
        COMPLETED = [9, 'Completed']


@choices
class RiskEnum:
    '''
    The risk level that is associated with an analysis
    '''
    class Meta:
        PASSED = [RISK_ENUM_PASSED, 'Passed']
        LOW = [RISK_ENUM_LOW, 'Low']
        MEDIUM = [RISK_ENUM_MEDIUM, 'Medium']
        HIGH = [RISK_ENUM_HIGH, 'High']
        CRITICAL = [RISK_ENUM_CRITICAL, 'Critical']


@choices
class AnalysisEnum:
    '''
    The status of the analysis
    '''
    class Meta:
        ERROR = [0, 'Error']
        WAITING = [1, 'Waiting']
        RUNNING = [2, 'Running']
        COMPLETED = [3, 'Completed']


@choices
class ManualEnum:
    '''
    Manual Assessment request state
    '''
    class Meta:
        NONE = [0, 'None']
        REQUESTED = [1, 'Requested']
        ASSESSING = [2, 'Assessing']
        DONE = [3, 'Done']


@choices
class NotifyEnum:
    class Meta:
        INFO = [0, 'Info']
        SUCCESS = [2, 'Success']
        WARNING = [3, 'Warning']
        ALERT = [4, 'Alert']
        ERROR = [5, 'Error']


@choices
class SubmissionStatusEnum:
    '''
    Submission status enum
    '''
    class Meta:
        DOWNLOAD_PREPARE = [0, 'Preparing to download the URL']
        DOWNLOADING = [1, 'Downloading the URL']
        DOWNLOAD_FAILED = [2, 'Failed to download the URL']
        VALIDATE_PREPARE = [3, 'Preparing to validate the file']
        VALIDATING = [4, 'Validating the file']
        VALIDATE_FAILED = [5, 'Failed to validate the file']
        ANALYZE_PREPARE = [6, 'Preparing to analyze the file']
        ANALYZING = [7, 'The file is being analyzed']


@choices
class SubmissionSourceEnum:
    '''
    Submission Source Enum
    '''
    class Meta:
        UPLOAD = [0, 'Upload']
        STORE = [1, 'Store']
        SCM = [2, 'Source Code Management']
        DEVKNOX = [3, 'Devknox']


@choices
class CollaborationRoleEnum:
    '''
    User project role
    '''
    class Meta:
        ADMIN = [0, 'Admin']
        MANAGER = [1, 'Manager']
        READ_ONLY = [2, 'Read Only']


@choices
class ContactSourceEnum:
    '''
    Enum to identify the contact source
    '''
    class Meta:
        HOME_PAGE = [0, 'Home Page']
        CONTACT_US = [1, 'Contact Us']


@choices
class ContactStatusEnum:
    '''
    Enum to recognize the status  of the contact
    '''
    class Meta:
        DEAD = [0, 'Dead']
        LIVE = [1, 'Live']


@choices
class ContactValidityEnum:
    '''
    Enum to differentiate between contacts
    with valid info and invalid info.
    '''
    class Meta:
        URL_INVALID = [0, 'URL Invalid']
        EMAIL_INVALID = [1, 'Email Invalid']
        NEW_NAME_SPACE = [2, 'New Namespace']
        ALL_VALID = [3, 'All Valid']


@choices
class PaymentSourceEnum:
    '''
    Where did the payment take place?
    '''
    class Meta:
        PAYPAL = [1, 'Paypal']
        STRIPE_MANUAL = [2, 'Stripe Manual']
        BANK_TRANSFER = [3, 'Bank Transfer']
        MANUAL = [4, 'Manual']
        STRIPE_RECURRING = [5, 'Stripe Recurring']


@choices
class PaymentDurationEnum:
    '''
    Duration - Yearly/Monthly
    NOTE:
        This is a special-case of enum. Each enum represents no.of months
        rather than sequential number. This way, the codebase will be much
        smaller and cleaner.

        I know I asked no one should change ENUMS after deployment.
        But I am doing this only because I know for a fact that no one has
        used Yearly. Just verified

        -dhilipsiva
    '''
    class Meta:
        MONTHLY = [1, 'Monthly']  # 1 Month
        QUARTERLY = [3, 'Quaterly']  # 3 Months
        HALFYEARLY = [6, 'Halfyearly']  # 6 months
        YEARLY = [10, 'Yearly']  # 10 months + 2 free months

    @staticmethod
    def days_for_duration(duration):
        '''
        Number of days for given duration
        '''
        months = duration
        DAYS = 31
        if duration == PaymentDurationEnum.YEARLY:
            months = 12
        # 31 days because Appknox is gracious
        return months * DAYS


@choices
class VulnerabilityTypeEnum:
    '''
    Vulnerability Type
    '''
    class Meta:
        STATIC = [1, 'Static']
        DYNAMIC = [2, 'Dynamic']
        MANUAL = [3, 'Manual']
        API = [4, 'API']


@choices
class ConfidenceEnum:
    '''
    Confidence about the occurrence of a vulnerability
    '''
    class Meta:
        LOW = [1, 'Low']
        MEDIUM = [2, 'Medium']
        HIGH = [3, 'High']


@choices
class UserTypeEnum:
    '''
    Use Types
    '''
    class Meta:
        APPKNOX = [1, 'Appknox']
        DEVKNOX = [2, 'Devknox']


@choices
class UserRoleEnum:
    """
    Role of User at Appknox
    """
    class Meta:
        CO_FOUNDER = [1, "Co-Founder"]
        EMPLOYEE = [2, "Employee"]
        PARTNER = [3, "Partner"]
        REGULAR = [4, "Regular"]


@choices
class UserDepartmentEnum:
    """
    The Department that the user belongs to
    """
    class Meta:
        TECHNOLOGY = [1, "Technology"]
        SECURITY = [2, "Security"]
        SALES = [3, "Sales"]
        MARKETING = [4, "Marketing"]
        DESIGN = [5, "Design"]


@choices
class AttackVectorEnum:
    """
    CVSSv3 attack vector
    """
    class Meta:
        NETWORK = ['N', 'Network']
        ADJACENT = ['A', 'Adjacent']
        LOCAL = ['L', 'Local']
        PHYSICAL = ['P', 'Physical']


@choices
class AttackComplexityEnum:
    """
    CVSSv3 attack complexity
    """
    class Meta:
        LOW = ['L', 'Low']
        HIGH = ['H', 'High']


@choices
class PrivilegesRequiredEnum:
    """
    CVSSv3 privileges required
    """
    class Meta:
        NONE = ['N', 'None']
        LOW = ['L', 'Low']
        HIGH = ['H', 'High']


@choices
class UserInteractionEnum:
    """
    CVSSv3 user interaction
    """
    class Meta:
        NOT_REQUIRED = ['N', 'Not Required']
        REQUIRED = ['R', 'Required']


@choices
class ScopeEnum:
    """
    CVSSv3 scope
    """
    class Meta:
        UNCHANGED = ['U', 'Unchanged']
        CHANGED = ['C', 'Changed']


@choices
class ConfidentialityImpactEnum:
    """
    CVSSv3 confidentiality impact
    """
    class Meta:
        HIGH = ['H', 'High']
        LOW = ['L', 'Low']
        NONE = ['N', 'None']


@choices
class IntegrityImpactEnum:
    """
    CVSSv3 integrity impact
    """
    class Meta:
        HIGH = ['H', 'High']
        LOW = ['L', 'Low']
        NONE = ['N', 'None']


@choices
class AvailabilityImpactEnum:
    """
    CVSSv3 availability impact
    """
    class Meta:
        HIGH = ['H', 'High']
        LOW = ['L', 'Low']
        NONE = ['N', 'None']


@choices
class MFAMethodEnum:
    """
    Multi-factor authentication method
    """
    class Meta:
        NONE = [0, 'None']
        TOTP = [1, 'TOTP']
        HOTP = [2, 'HOTP']
