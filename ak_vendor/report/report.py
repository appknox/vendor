import attr
import enum
import maya
import json
import html2text
from datetime import datetime
from urllib.parse import quote
from cvss import CVSS3
from typing import List
from ..constants import PLATFORM_ICONS

ATTACHMENT_IMAGE_FORMATS = ["png", "jpg", "jpeg", "bmp", "svg", "gif"]


class PlatformEnum(enum.Enum):
    ANDROID = "Android"
    IOS = "iOS"
    WINDOWS = "Windows"


class PlatformIconEnum(enum.Enum):
    ANDROID = PLATFORM_ICONS["ANDROID"]
    IOS = PLATFORM_ICONS["IOS"]
    WINDOWS = PLATFORM_ICONS["WINDOWS"]


class RiskColorEnum(enum.Enum):
    CRITICAL = "#EF4836"
    HIGH = "#FF8C00"
    MEDIUM = "#F5D76E"
    LOW = "#2CC2F8"
    PASSED = "#80C081"
    UNTESTED = "#6B6B6B"


class RiskValueEnum(enum.Enum):
    CRITICAL = 4
    HIGH = 3
    MEDIUM = 2
    LOW = 1
    PASSED = 0
    UNTESTED = -1


class RiskLabelEnum(enum.Enum):
    CRITICAL = "Critical"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"
    PASSED = "Passed"
    UNTESTED = "Untested"


class AnalysisTypeEnum(enum.Enum):
    STATIC = "Static"
    DYNAMIC = "Dynamic"
    MANUAL = "Manual"
    API = "API"


class AttackVectorEnum(enum.Enum):
    N = "NETWORK"
    A = "ADJACENT_NETWORK"
    L = "LOCAL"
    P = "PHYSICAL"


class AttackComplexityEnum(enum.Enum):
    H = "HIGH"
    L = "LOW"


class PrivilegesRequiredEnum(enum.Enum):
    H = "HIGH"
    L = "LOW"
    N = "NONE"


class UserInteractionEnum(enum.Enum):
    N = "NONE"
    R = "REQUIRED"


class ScopeEnum(enum.Enum):
    U = "UNCHANGED"
    C = "CHANGED"


class ConfidentialityImpactEnum(enum.Enum):
    H = "HIGH"
    L = "LOW"
    N = "NONE"


class IntegrityImpactEnum(enum.Enum):
    H = "HIGH"
    L = "LOW"
    N = "NONE"


class AvailabilityImpactEnum(enum.Enum):
    H = "HIGH"
    L = "LOW"
    N = "NONE"


@attr.s
class Platform:
    ANDROID = PlatformEnum.ANDROID.value
    IOS = PlatformEnum.IOS.value
    WINDOWS = PlatformEnum.WINDOWS.value
    ICON_ANDROID = PlatformIconEnum.ANDROID.value
    ICON_IOS = PlatformIconEnum.IOS.value
    ICON_WINDOWS = PlatformIconEnum.WINDOWS.value
    name = attr.ib(type=str)
    icon = attr.ib(type=str)


@attr.s
class Application:
    name = attr.ib(type=str)
    icon = attr.ib(type=str)
    version = attr.ib(type=str)
    version_code = attr.ib(type=int)
    sha1 = attr.ib(type=str)
    md5 = attr.ib(type=str)


@attr.s
class Company:
    name = attr.ib(type=str, default="")
    logo = attr.ib(type=str, default="")
    hide = attr.ib(type=bool, default=False)


@attr.s
class Reference:
    id = attr.ib(type=int)
    name = attr.ib(type=str)
    url = attr.ib(type=str)


@attr.s
class CustomMetaData:
    key = attr.ib(type=str)
    val = attr.ib(type=str)


@attr.s
class Content:
    html = attr.ib(type=str)
    text = attr.ib(type=str, default="")
    markdown = attr.ib(type=str, default="")

    def html_to_text(self):
        return html2text.html2text(self.html)[:-2]


@attr.s
class Attachment:
    id = attr.ib(type=str)
    name = attr.ib(type=str)
    extension = attr.ib(type=str)
    url = attr.ib(type=str)


@attr.s
class CVSSv3:
    version = attr.ib(type=str)
    vector_string = attr.ib(type=str)
    base_score = attr.ib(type=str)
    base_severity = attr.ib(type=str)
    attack_vector = attr.ib(
        type=str,
        validator=attr.validators.in_([e.value for e in AttackVectorEnum]),
        default=AttackVectorEnum.P.value,
    )
    attack_complexity = attr.ib(
        type=str,
        validator=attr.validators.in_([e.value for e in AttackComplexityEnum]),
        default=AttackComplexityEnum.H.value,
    )
    privileges_required = attr.ib(
        type=str,
        validator=attr.validators.in_([e.value for e in PrivilegesRequiredEnum]),
        default=PrivilegesRequiredEnum.H.value,
    )
    user_interaction = attr.ib(
        type=str,
        validator=attr.validators.in_([e.value for e in UserInteractionEnum]),
        default=UserInteractionEnum.R.value,
    )
    scope = attr.ib(
        type=str,
        validator=attr.validators.in_([e.value for e in ScopeEnum]),
        default=ScopeEnum.U.value,
    )
    confidentiality_impact = attr.ib(
        type=str,
        validator=attr.validators.in_([e.value for e in ConfidentialityImpactEnum]),
        default=ConfidentialityImpactEnum.N.value,
    )
    integrity_impact = attr.ib(
        type=str,
        validator=attr.validators.in_([e.value for e in IntegrityImpactEnum]),
        default=IntegrityImpactEnum.N.value,
    )
    availability_impact = attr.ib(
        type=str,
        validator=attr.validators.in_([e.value for e in AvailabilityImpactEnum]),
        default=AvailabilityImpactEnum.N.value,
    )

    @classmethod
    def parse_vector(cls, vector_string: str) -> "CVSSv3":
        if not vector_string:
            return None
        cvssv3 = CVSS3(vector_string)
        (base_severity, temporal_severity, environmental_severity) = cvssv3.severities()
        return CVSSv3(
            version="3",
            vector_string=vector_string,
            base_score=str(cvssv3.base_score),
            base_severity=base_severity,
            attack_vector=(AttackVectorEnum[cvssv3.metrics.get("AV")].value),
            attack_complexity=(AttackComplexityEnum[cvssv3.metrics.get("AC")].value),
            privileges_required=(
                PrivilegesRequiredEnum[cvssv3.metrics.get("PR")].value
            ),
            user_interaction=(UserInteractionEnum[cvssv3.metrics.get("UI")].value),
            scope=(ScopeEnum[cvssv3.metrics.get("S")].value),
            confidentiality_impact=(
                ConfidentialityImpactEnum[cvssv3.metrics.get("C")].value
            ),
            integrity_impact=(IntegrityImpactEnum[cvssv3.metrics.get("I")].value),
            availability_impact=(AvailabilityImpactEnum[cvssv3.metrics.get("A")].value),
        )


@attr.s
class Risk:
    value = attr.ib(type=int, default=RiskValueEnum.UNTESTED.value)
    value_label = attr.ib(type=str, default=RiskLabelEnum.UNTESTED.value)
    value_color = attr.ib(type=str, default=RiskColorEnum.UNTESTED.value)
    computed_value = attr.ib(type=int, default=RiskValueEnum.UNTESTED.value)
    computed_value_label = attr.ib(type=str, default=RiskLabelEnum.UNTESTED.value)
    computed_value_color = attr.ib(type=str, default=RiskColorEnum.UNTESTED.value)
    is_overridden = attr.ib(type=bool, default=False)
    override_comment = attr.ib(type=str, default="")


@attr.s
class OWASP:
    code = attr.ib(type=str)
    year = attr.ib(type=int)
    title = attr.ib(type=str)


@attr.s
class CWE:
    code = attr.ib(type=str)
    url = attr.ib(type=str)


@attr.s
class ASVS:
    code = attr.ib(type=str)
    title = attr.ib(type=str)


@attr.s
class MSTG:
    code = attr.ib(type=str)
    title = attr.ib(type=str)


@attr.s
class PCIDSS:
    code = attr.ib(type=str)
    title = attr.ib(type=str)
    description = attr.ib(type=str)


@attr.s
class HIPAAStandard:
    title = attr.ib(type=str)
    description = attr.ib(type=str)
    specifications = attr.ib(type=str)


@attr.s
class HIPAA:
    code = attr.ib(type=str)
    safeguard = attr.ib(type=str)
    title = attr.ib(type=str)
    standards = attr.ib(factory=list, type=List[HIPAAStandard])

    @classmethod
    def create_standard(
        cls, title: str, description: str, specifications: str
    ) -> HIPAAStandard:
        return HIPAAStandard(
            title=title, description=description, specifications=specifications
        )

    @classmethod
    def from_json(cls, data: dict):
        return cls(
            code=data.get("code"),
            safeguard=data.get("safeguard"),
            title=data.get("title"),
            standards=[
                cls.create_standard(**standard)
                for standard in data.get("standards", [])
            ],
        )

    def add_standard(self, standard: HIPAAStandard) -> List[HIPAAStandard]:
        self.standards.append(standard)
        return self.standards


@attr.s
class GDPR:
    code = attr.ib(type=str)
    title = attr.ib(type=str)


@attr.s
class Regulatory:
    owasp = attr.ib(factory=list, type=List[dict])
    cwe = attr.ib(factory=list, type=List[dict])
    asvs = attr.ib(factory=list, type=List[dict])
    mstg = attr.ib(factory=list, type=List[dict])
    pcidss = attr.ib(factory=list, type=List[dict])
    hipaa = attr.ib(factory=list, type=List[dict])
    gdpr = attr.ib(factory=list, type=List[dict])

    @classmethod
    def from_json(cls, data):
        return cls(
            owasp=[OWASP(**owasp) for owasp in data.get("owasp", [])],
            cwe=[CWE(**cwe) for cwe in data.get("cwe", [])],
            asvs=[ASVS(**asvs) for asvs in data.get("asvs", [])],
            mstg=[MSTG(**mstg) for mstg in data.get("mstg", [])],
            pcidss=[PCIDSS(**pcidss) for pcidss in data.get("pcidss", [])],
            hipaa=[HIPAA.from_json(hipaa) for hipaa in data.get("hipaa", [])],
            gdpr=[GDPR(**gdpr) for gdpr in data.get("gdpr", [])],
        )

    @classmethod
    def create_owasp(cls, code: str, year: int, title: str) -> OWASP:
        return OWASP(code=code, year=year, title=title)

    @classmethod
    def create_cwe(cls, code: str, url: str) -> CWE:
        return CWE(code=code, url=url)

    @classmethod
    def create_asvs(cls, code: str, title: str) -> ASVS:
        return ASVS(code=code, title=title)

    @classmethod
    def create_mstg(cls, code: str, title: str) -> MSTG:
        return MSTG(code=code, title=title)

    @classmethod
    def create_pcidss(cls, code: str, title: str, description: str) -> PCIDSS:
        return PCIDSS(code=code, title=title, description=description)

    @classmethod
    def create_hipaa(
        cls, code: str, safeguard: str, title: str, standards: List[HIPAAStandard] = []
    ) -> HIPAA:
        return HIPAA(
            code=code,
            safeguard=safeguard,
            title=title,
            standards=standards,
        )

    @classmethod
    def create_gdpr(cls, code: str, title: str) -> GDPR:
        return GDPR(code=code, title=title)

    def add_owasp(self, owasp: OWASP) -> List[OWASP]:
        self.owasp.append(owasp)
        return self.owasp

    def add_cwe(self, cwe: CWE) -> List[MSTG]:
        self.cwe.append(cwe)
        return self.cwe

    def add_asvs(self, asvs: ASVS) -> List[ASVS]:
        self.asvs.append(asvs)
        return self.asvs

    def add_mstg(self, mstg: MSTG) -> List[MSTG]:
        self.mstg.append(mstg)
        return self.mstg

    def add_pcidss(self, pcidss: PCIDSS) -> List[PCIDSS]:
        self.pcidss.append(pcidss)
        return self.pcidss

    def add_hipaa(self, hipaa: HIPAA) -> List[HIPAA]:
        self.hipaa.append(hipaa)
        return self.hipaa

    def add_gdpr(self, gdpr: GDPR) -> List[GDPR]:
        self.gdpr.append(gdpr)
        return self.gdpr


@attr.s
class Tag:
    val = attr.ib(type=str)


@attr.s
class Finding:
    title = attr.ib(type=Content)
    description = attr.ib(type=Content)


@attr.s
class Analysis:
    id = attr.ib(type=int)
    title = attr.ib(type=Content)
    desc = attr.ib(type=Content)
    intro = attr.ib(type=Content)
    business_implication = attr.ib(type=Content)
    correct_implementation = attr.ib(type=Content)
    incorrect_implementation = attr.ib(type=Content)
    question = attr.ib(type=Content)
    success_message = attr.ib(type=Content)
    vulnerability_references = attr.ib(type=Content)
    risk = attr.ib(type=Risk, default=Risk())
    cvss_v3 = attr.ib(type=CVSSv3, default=None)
    regulatory = attr.ib(
        type=Regulatory,
        default=Regulatory(
            owasp=[], pcidss=[], hipaa=[], asvs=[], cwe=[], gdpr=[], mstg=[]
        ),
    )
    findings = attr.ib(factory=list, type=List[Content])
    tags = attr.ib(factory=list, type=List[Tag])
    attachments = attr.ib(factory=list, type=List[Attachment])

    @classmethod
    def from_json(cls, data):
        cvssv3 = data.get("cvss_v3")
        return cls(
            id=data.get("id"),
            title=Content(**data.get("title")),
            desc=Content(**data.get("desc")),
            intro=Content(**data.get("intro")),
            business_implication=Content(**data.get("business_implication")),
            correct_implementation=Content(**data.get("correct_implementation")),
            incorrect_implementation=Content(**data.get("incorrect_implementation")),
            question=Content(**data.get("question")),
            success_message=Content(**data.get("success_message")),
            vulnerability_references=Content(**data.get("vulnerability_references")),
            risk=Risk(**data.get("risk", {})),
            cvss_v3=CVSSv3(**cvssv3) if cvssv3 else None,
            regulatory=Regulatory.from_json(data.get("regulatory")),
            findings=[
                cls.create_finding(
                    title=Content(**finding.get("title")),
                    description=Content(**finding.get("description")),
                )
                for finding in data.get("findings", [])
            ],
            tags=[Tag(**tag) for tag in data.get("tags", [])],
            attachments=[
                Attachment(**attachment) for attachment in data.get("attachments", [])
            ],
        )

    @classmethod
    def create_regulatory(
        cls,
        owasp: List[dict] = [],
        cwe: List[dict] = [],
        asvs: List[dict] = [],
        mstg: List[dict] = [],
        pcidss: List[dict] = [],
        hipaa: List[dict] = [],
        gdpr: List[dict] = [],
    ) -> Regulatory:
        return Regulatory(
            owasp=owasp,
            cwe=cwe,
            asvs=asvs,
            mstg=mstg,
            pcidss=pcidss,
            hipaa=hipaa,
            gdpr=gdpr,
        )

    @classmethod
    def create_attachment(
        cls, id: str, name: str, extension: str, url: str
    ) -> Attachment:
        return Attachment(id=id, name=name, extension=extension, url=url)

    @classmethod
    def create_finding(cls, title: Content, description: Content) -> Finding:
        if title.html:
            title.html = cls.trim_unsupported_chars(title.html)
        if description.html:
            description.html = cls.trim_unsupported_chars(description.html)
        return Finding(title=title, description=description)

    @classmethod
    def create_tag(cls, val: str) -> Tag:
        return Tag(val=val)

    @classmethod
    def create_risk(
        cls,
        value: int,
        value_label: str,
        value_color: str,
        computed_value: int,
        computed_value_label: str,
        computed_value_color: str,
        is_overridden: bool,
        override_comment: str,
    ) -> Risk:
        return Risk(
            value=value,
            value_label=value_label,
            value_color=value_color,
            computed_value=computed_value,
            computed_value_label=computed_value_label,
            computed_value_color=computed_value_color,
            is_overridden=is_overridden,
            override_comment=override_comment,
        )

    def add_finding(self, finding: Finding) -> Finding:
        self.findings.append(finding)
        return self.findings

    def add_tag(self, tag: Tag) -> Tag:
        self.tags.append(tag)
        return self.tags

    def remove_tag(self, tag_val: str) -> Tag:
        for t in self.tags:
            if tag_val == t.val:
                self.tags.remove(t)
        return self.tags

    def add_attachment(self, attachment: Attachment) -> Attachment:
        if attachment.extension.lower() not in ATTACHMENT_IMAGE_FORMATS:
            return False
        self.attachments.append(attachment)
        return self.attachments

    @classmethod
    def trim_unsupported_chars(cls, string: str) -> str:
        """trim non-font characters"""
        s = string
        for char in ["\u001b", "\\u001b", "\x1b"]:  # ESCAPE char
            s = s.replace(char, "")
        return s


@attr.s
class Report:
    COLOR_CRITICAL = RiskColorEnum.CRITICAL.value
    COLOR_HIGH = RiskColorEnum.HIGH.value
    COLOR_MEDIUM = RiskColorEnum.MEDIUM.value
    COLOR_LOW = RiskColorEnum.LOW.value
    COLOR_PASSED = RiskColorEnum.PASSED.value
    COLOR_UNTESTED = RiskColorEnum.UNTESTED.value
    RISK_COLOR = {
        "critical": COLOR_CRITICAL,
        "high": COLOR_HIGH,
        "medium": COLOR_MEDIUM,
        "low": COLOR_LOW,
        "passed": COLOR_PASSED,
        "untested": COLOR_UNTESTED,
    }
    package_name = attr.ib(type=str)
    platform = attr.ib(type=Platform)
    application = attr.ib(type=Application)
    appknox_file_id = attr.ib(type=int, default=None)
    prepared_for = attr.ib(type=Company, default=Company(name=""))
    prepared_by = attr.ib(
        type=Company,
        default=Company(name="Appknox", logo="https://appknox.com/in/img/logo.png"),
    )
    powered_by = attr.ib(type=Company, default=Company(hide=True))
    created_on = attr.ib(type=datetime, default=maya.now().iso8601())
    show_copyright = attr.ib(type=bool, default=True)
    is_partnered = attr.ib(type=bool, default=False)
    rating = attr.ib(type=int, default=0)
    is_included_static_scan = attr.ib(type=bool, default=True)
    is_included_dynamic_scan = attr.ib(type=bool, default=True)
    is_included_api_scan = attr.ib(type=bool, default=True)
    is_included_manual_scan = attr.ib(type=bool, default=True)
    is_done_static_scan = attr.ib(type=bool, default=False)
    is_done_dynamic_scan = attr.ib(type=bool, default=False)
    is_done_api_scan = attr.ib(type=bool, default=False)
    is_done_manual_scan = attr.ib(type=bool, default=False)
    references = attr.ib(factory=list, type=List[Reference])
    custom_meta_data = attr.ib(factory=list, type=List[CustomMetaData])
    analyses = attr.ib(factory=list, type=List[Analysis])

    def to_dict(self) -> dict:
        return attr.asdict(self)

    def to_json(self) -> dict:
        return json.loads(
            json.dumps(self.to_dict(), indent=4, sort_keys=True, default=str)
        )

    @classmethod
    def from_json(cls, data):
        return cls(
            package_name=data.get("package_name"),
            platform=Platform(**data.get("platform")),
            application=Application(**data.get("application")),
            appknox_file_id=data.get("appknox_file_id"),
            prepared_for=Company(**data.get("prepared_for")),
            prepared_by=Company(**data.get("prepared_by")),
            powered_by=Company(**data.get("powered_by")),
            created_on=cls.create_created_on(data.get("created_on")),
            show_copyright=data.get("show_copyright"),
            is_partnered=data.get("is_partnered"),
            rating=data.get("rating"),
            is_included_static_scan=data.get(
                "is_included_static_scan",
                cls.__attrs_attrs__.is_included_static_scan.default,
            ),
            is_included_dynamic_scan=data.get(
                "is_included_dynamic_scan",
                cls.__attrs_attrs__.is_included_dynamic_scan.default,
            ),
            is_included_api_scan=data.get(
                "is_included_api_scan", cls.__attrs_attrs__.is_included_api_scan.default
            ),
            is_included_manual_scan=data.get(
                "is_included_manual_scan",
                cls.__attrs_attrs__.is_included_manual_scan.default,
            ),
            is_done_static_scan=data.get(
                "is_done_static_scan", cls.__attrs_attrs__.is_done_static_scan.default
            ),
            is_done_dynamic_scan=data.get(
                "is_done_dynamic_scan", cls.__attrs_attrs__.is_done_dynamic_scan.default
            ),
            is_done_api_scan=data.get(
                "is_done_api_scan", cls.__attrs_attrs__.is_done_api_scan.default
            ),
            is_done_manual_scan=data.get(
                "is_done_manual_scan", cls.__attrs_attrs__.is_done_manual_scan.default
            ),
            references=[
                Reference(**reference) for reference in data.get("references", [])
            ],
            custom_meta_data=[
                CustomMetaData(**cmd) for cmd in data.get("custom_meta_data", [])
            ],
            analyses=[
                Analysis.from_json(analysis) for analysis in data.get("analyses", [])
            ],
        )

    def add_analysis(self, analysis: Analysis) -> Analysis:
        self.analyses.append(analysis)

    def add_reference(self, reference: Reference) -> Reference:
        self.references.append(reference)

    def add_custom_metadata(self, customdata: CustomMetaData) -> CustomMetaData:
        self.custom_meta_data.append(customdata)

    @classmethod
    def create_platform(cls, name: str, icon: str) -> Platform:
        return Platform(name=name, icon=icon)

    @classmethod
    def create_application(
        cls, name: str, icon: str, version: str, version_code: str, sha1: str, md5: str
    ) -> Application:
        return Application(
            name=name,
            icon=icon,
            version=version,
            version_code=version_code,
            sha1=sha1,
            md5=md5,
        )

    @classmethod
    def create_company(cls, name, logo, hide) -> Company:
        return Company(name=name, logo=logo, hide=hide)

    @classmethod
    def create_created_on(cls, isodate: str = (maya.now().iso8601())) -> datetime:
        return maya.parse(isodate).datetime()

    @classmethod
    def create_reference(cls, id: int, name: str, url: str) -> Reference:
        return Reference(id=id, name=name, url=url)

    @classmethod
    def create_custommetadata(cls, key: str, val: str) -> CustomMetaData:
        return CustomMetaData(key=key, val=val)

    @classmethod
    def create_analysis(
        cls,
        id,
        title: Content,
        intro: Content,
        desc: Content,
        risk: Risk,
        cvss_v3: CVSSv3,
        business_implication: Content,
        correct_implementation: Content,
        incorrect_implementation: Content,
        question: Content,
        success_message: Content,
        regulatory: Regulatory,
        vulnerability_references: Content,
        findings: List[Content] = [],
        tags: List[Tag] = [],
        attachments: List[Attachment] = [],
    ) -> Analysis:
        return Analysis(
            id=id,
            title=title,
            intro=intro,
            desc=desc,
            risk=risk,
            cvss_v3=cvss_v3,
            business_implication=business_implication,
            correct_implementation=correct_implementation,
            incorrect_implementation=incorrect_implementation,
            question=question,
            success_message=success_message,
            regulatory=regulatory,
            vulnerability_references=vulnerability_references,
            findings=findings,
            tags=tags,
            attachments=attachments,
        )

    @classmethod
    def create_content(
        cls, text: str = "", html: str = "", markdown: str = ""
    ) -> Content:
        return Content(text=text, html=html, markdown=markdown)

    @classmethod
    def create_risk(cls, **kwargs) -> Risk:
        return Analysis.create_risk(**kwargs)

    @classmethod
    def create_regulatory(cls, **kwargs) -> Regulatory:
        return Analysis.create_regulatory(**kwargs)

    @classmethod
    def parse_cvssv3_vector(cls, **kwargs) -> CVSSv3:
        return CVSSv3.parse_vector(**kwargs)

    @classmethod
    def get_risk_color(cls, risk: str) -> str:
        return cls.RISK_COLOR.get(risk.lower(), "")

    def _count_severity(self, label: str) -> int:
        count = 0
        for a in self.analyses:
            if a.risk and (a.risk.computed_value_label.lower() == label):
                count += 1
        return count

    def _percent_severity(self, count: int) -> float:
        if not len(self.analyses):
            return 0.0
        return round((count / len(self.analyses)) * 100, 2)

    @property
    def critical_count(self) -> int:
        return self._count_severity("critical")

    @property
    def high_count(self) -> int:
        return self._count_severity("high")

    @property
    def medium_count(self) -> int:
        return self._count_severity("medium")

    @property
    def low_count(self) -> int:
        return self._count_severity("low")

    @property
    def passed_count(self) -> int:
        return self._count_severity("passed")

    @property
    def untested_count(self) -> int:
        return self._count_severity("untested")

    @property
    def critical_percent(self) -> float:
        return self._percent_severity(self.critical_count)

    @property
    def high_percent(self) -> float:
        return self._percent_severity(self.high_count)

    @property
    def medium_percent(self) -> float:
        return self._percent_severity(self.medium_count)

    @property
    def low_percent(self) -> float:
        return self._percent_severity(self.low_count)

    @property
    def passed_percent(self) -> float:
        return self._percent_severity(self.passed_count)

    @property
    def untested_percent(self) -> float:
        return self._percent_severity(self.untested_count)

    @property
    def svg_chart(self) -> str:
        tpl = (
            '<circle cx="21" cy="21" r="15.91549430918954" stroke-width="8" '
            'stroke="{}" stroke-dasharray="{} {}" stroke-dashoffset="-{}" '
            'fill="transparent"></circle>'
        )
        sector = ""
        offset = 0
        p = self.critical_percent
        sector += tpl.format(self.COLOR_CRITICAL, p, round(100 - p, 2), offset)
        offset += p
        p = self.high_percent
        sector += tpl.format(self.COLOR_HIGH, p, round(100 - p, 2), offset)
        offset += p
        p = self.medium_percent
        sector += tpl.format(self.COLOR_MEDIUM, p, round(100 - p, 2), offset)
        offset += p
        p = self.low_percent
        sector += tpl.format(self.COLOR_LOW, p, round(100 - p, 2), offset)
        offset += p
        p = self.passed_percent
        sector += tpl.format(self.COLOR_PASSED, p, round(100 - p, 2), offset)
        offset += p
        p = self.untested_percent
        sector += tpl.format(self.COLOR_UNTESTED, p, round(100 - p, 2), offset)
        return (
            "data:image/svg+xml;utf8,"
            '<svg xmlns="http://www.w3.org/2000/svg" '
            'xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" '
            'width="216px" height="216px" viewBox="0 0 42 42">{}</svg>'
        ).format(quote(sector))

    @property
    def custom_meta_names(self) -> List[str]:
        return [
            cmd.val
            for cmd in self.custom_meta_data
            if cmd.key == "name" and cmd.val != ""
        ]

    @property
    def _scan_types_visible(self):
        scan_types = set()
        if self.is_included_static_scan:
            scan_types.add(AnalysisTypeEnum.STATIC.value.lower())
        if self.is_included_dynamic_scan:
            scan_types.add(AnalysisTypeEnum.DYNAMIC.value.lower())
        if self.is_included_api_scan:
            scan_types.add(AnalysisTypeEnum.API.value.lower())
        if self.is_included_manual_scan:
            scan_types.add(AnalysisTypeEnum.MANUAL.value.lower())
        return scan_types

    def _is_visible_scan_type(self, analysis):
        tags = {t.val.lower() for t in analysis.tags}
        include_tags = tags.intersection(self._scan_types_visible)
        if not include_tags:
            return False
        if include_tags:
            for t in analysis.tags:
                if t.val.lower() not in include_tags:
                    analysis.tags.remove(t)
        return analysis

    @property
    def viewable_analyses(self) -> List[Analysis]:
        return [a for a in self.analyses if self._is_visible_scan_type(a)]
