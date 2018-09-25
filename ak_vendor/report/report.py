import attr
import enum
from cvss import CVSS3
from typing import List

ATTACHMENT_IMAGE_FORMATS = ['png', 'jpg', 'jpeg', 'bmp', 'svg', 'gif']


class AttackVectorEnum(enum.Enum):
    N = 'NETWORK'
    A = 'ADJACENT_NETWORK'
    L = 'LOCAL'
    P = 'PHYSICAL'


class AttackComplexityEnum(enum.Enum):
    H = 'HIGH'
    L = 'LOW'


class PrivilegesRequiredEnum(enum.Enum):
    H = 'HIGH'
    L = 'LOW'
    N = 'NONE'


class UserInteractionEnum(enum.Enum):
    N = 'NONE'
    R = 'REQUIRED'


class ScopeEnum(enum.Enum):
    U = 'UNCHANGED'
    C = 'CHANGED'


class ConfidentialityImpactEnum(enum.Enum):
    H = 'HIGH'
    L = 'LOW'
    N = 'NONE'


class IntegrityImpactEnum(enum.Enum):
    H = 'HIGH'
    L = 'LOW'
    N = 'NONE'


class AvailabilityImpactEnum(enum.Enum):
    H = 'HIGH'
    L = 'LOW'
    N = 'NONE'


@attr.s
class Platform:
    name = attr.ib(type=str)
    icon = attr.ib(type=str)


@attr.s
class Application:
    name = attr.ib(type=str)
    icon = attr.ib(type=str)
    version = attr.ib(type=str)
    version_code = attr.ib(type=str)
    sha1 = attr.ib(type=str)
    md5 = attr.ib(type=str)


@attr.s
class Company:
    name = attr.ib(type=str)
    logo = attr.ib(type=str)
    hide = attr.ib(type=bool)


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
    text = attr.ib(type=str)
    html = attr.ib(type=str)
    markdown = attr.ib(type=str)


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
        default=AttackVectorEnum.P.value
    )
    attack_complexity = attr.ib(
        type=str,
        validator=attr.validators.in_([e.value for e in AttackComplexityEnum]),
        default=AttackComplexityEnum.H.value
    )
    privileges_required = attr.ib(
        type=str,
        validator=attr.validators.in_(
            [e.value for e in PrivilegesRequiredEnum]
        ),
        default=PrivilegesRequiredEnum.H.value
    )
    user_interaction = attr.ib(
        type=str,
        validator=attr.validators.in_([e.value for e in UserInteractionEnum]),
        default=UserInteractionEnum.R.value
    )
    scope = attr.ib(
        type=str,
        validator=attr.validators.in_([e.value for e in ScopeEnum]),
        default=ScopeEnum.U.value
    )
    confidentiality_impact = attr.ib(
        type=str,
        validator=attr.validators.in_(
            [e.value for e in ConfidentialityImpactEnum]
        ),
        default=ConfidentialityImpactEnum.N.value
    )
    integrity_impact = attr.ib(
        type=str,
        validator=attr.validators.in_([e.value for e in IntegrityImpactEnum]),
        default=IntegrityImpactEnum.N.value
    )
    availability_impact = attr.ib(
        type=str,
        validator=attr.validators.in_(
            [e.value for e in AvailabilityImpactEnum]
        ),
        default=AvailabilityImpactEnum.N.value
    )

    @classmethod
    def parse_vector(cls, vector_string):
        if not vector_string:
            return None
        cvssv3 = CVSS3(vector_string)
        (
            base_severity, temporal_severity, environmental_severity
        ) = cvssv3.severities()
        return CVSSv3(
            version='3',
            vector_string=vector_string,
            base_score=str(cvssv3.base_score),
            base_severity=base_severity,
            attack_vector=(
                AttackVectorEnum[cvssv3.metrics.get('AV')].value
            ),
            attack_complexity=(
                AttackComplexityEnum[cvssv3.metrics.get('AC')].value
            ),
            privileges_required=(
                PrivilegesRequiredEnum[cvssv3.metrics.get('PR')].value
            ),
            user_interaction=(
                UserInteractionEnum[cvssv3.metrics.get('UI')].value
            ),
            scope=(
                ScopeEnum[cvssv3.metrics.get('S')].value
            ),
            confidentiality_impact=(
                ConfidentialityImpactEnum[cvssv3.metrics.get('C')].value
            ),
            integrity_impact=(
                IntegrityImpactEnum[cvssv3.metrics.get('I')].value
            ),
            availability_impact=(
                AvailabilityImpactEnum[cvssv3.metrics.get('A')].value
            ),
        )


@attr.s
class Risk:
    value = attr.ib(type=int)
    value_label = attr.ib(type=str)
    value_color = attr.ib(type=str)
    computed_value = attr.ib(type=int)
    computed_value_label = attr.ib(type=str)
    computed_value_color = attr.ib(type=str)
    is_overridden = attr.ib(type=bool)
    override_comment = attr.ib(type=str)


@attr.s
class OWASP:
    code = attr.ib(type=str)
    year = attr.ib(type=int)
    title = attr.ib(type=str)


@attr.s
class PCIDSS:
    code = attr.ib(type=str)
    title = attr.ib(type=str)
    description = attr.ib(type=str)


@attr.s
class Regulatory:
    owasp = attr.ib(factory=list, type=List[dict])
    pcidss = attr.ib(factory=list, type=List[dict])

    @classmethod
    def create_owasp(cls, code: str, year: int, title: str):
        return OWASP(code=code, year=year, title=title)

    @classmethod
    def create_pcidss(cls, code: str, title: str, description: str):
        return PCIDSS(code=code, title=title, description=description)

    def add_owasp(self, owasp: OWASP) -> OWASP:
        self.owasp.append(owasp)
        return self.owasp

    def add_pcidss(self, pcidss: PCIDSS) -> PCIDSS:
        self.pcidss.append(pcidss)
        return self.pcidss


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
    intro = attr.ib(type=Content)
    desc = attr.ib(type=Content)
    risk = attr.ib(type=Risk)
    cvss_v3 = attr.ib(type=CVSSv3)
    business_implication = attr.ib(type=Content)
    correct_implementation = attr.ib(type=Content)
    incorrect_implementation = attr.ib(type=Content)
    regulatory = attr.ib(type=Regulatory)
    vulnerability_references = attr.ib(type=Content)
    findings = attr.ib(factory=list, type=List[Content])
    tags = attr.ib(factory=list, type=List[Tag])
    attachments = attr.ib(factory=list, type=List[Attachment])

    @classmethod
    def create_regulatory(cls, owasp: List[dict]=[], pcidss: List[dict]=[]):
        return Regulatory(owasp=owasp, pcidss=pcidss)

    @classmethod
    def create_attachment(cls, id: str, name: str, extension: str, url: str):
        return Attachment(id=id, name=name, extension=extension, url=url)

    @classmethod
    def create_finding(cls, title: Content, description: Content):
        return Finding(title=title, description=description)

    @classmethod
    def create_tag(cls, val: str):
        return Tag(val=val)

    @classmethod
    def create_risk(
        cls, value: int, value_label: str, value_color: str,
        computed_value: int, computed_value_label: str,
        computed_value_color: str, is_overridden: bool, override_comment: str
    ):
        return Risk(
            value=value,
            value_label=value_label,
            value_color=value_color,
            computed_value=computed_value,
            computed_value_label=computed_value_label,
            computed_value_color=computed_value_color,
            is_overridden=is_overridden,
            override_comment=override_comment
        )

    def add_finding(self, finding: Finding) -> Finding:
        self.findings.append(finding)
        return self.findings

    def add_tag(self, tag: Tag) -> Tag:
        self.tags.append(tag)
        return self.tags

    def add_attachment(self, attachment: Attachment) -> Attachment:
        if attachment.extension.lower() not in ATTACHMENT_IMAGE_FORMATS:
            return False
        self.attachments.append(attachment)
        return self.attachments


@attr.s
class Report:
    COLOR_CRITICAL = '#EF4836'
    COLOR_HIGH = '#FF8C00'
    COLOR_MEDIUM = '#F5D76E'
    COLOR_LOW = '#2CC2F8'
    COLOR_PASSED = '#80C081'
    COLOR_UNTESTED = '#6B6B6B'
    RISK_COLOR = {
        'critical': COLOR_CRITICAL,
        'high': COLOR_HIGH,
        'medium': COLOR_MEDIUM,
        'low': COLOR_LOW,
        'passed': COLOR_PASSED,
        'untested': COLOR_UNTESTED,
    }
    package_name = attr.ib(type=str)
    platform = attr.ib(type=Platform)
    application = attr.ib(type=Application)
    created_on = attr.ib(type=str)
    prepared_for = attr.ib(type=Company)
    prepared_by = attr.ib(type=Company)
    powered_by = attr.ib(type=Company)
    show_copyright = attr.ib(type=bool)
    is_partnered = attr.ib(type=bool)
    rating = attr.ib(type=int)
    references = attr.ib(factory=list, type=List[Reference])
    custom_meta_data = attr.ib(factory=list, type=List[CustomMetaData])
    analyses = attr.ib(factory=list, type=List[Analysis])

    def to_json(self):
        return attr.asdict(self)

    def add_analysis(self, analysis: Analysis) -> Analysis:
        self.analyses.append(analysis)

    def add_reference(self, reference: Reference) -> Reference:
        self.references.append(reference)

    def add_custom_metadata(
        self, customdata: CustomMetaData
    ) -> CustomMetaData:
        self.custom_meta_data.append(customdata)

    @classmethod
    def create_platform(cls, name: str, icon: str):
        return Platform(name=name, icon=icon)

    @classmethod
    def create_application(
        cls, name: str, icon: str, version: str, version_code: str,
        sha1: str, md5: str
    ):
        return Application(
            name=name, icon=icon, version=version, version_code=version_code,
            sha1=sha1, md5=md5
        )

    @classmethod
    def create_company(cls, name, logo, hide):
        return Company(name=name, logo=logo, hide=hide)

    @classmethod
    def create_reference(cls, id: int, name: str, url: str):
        return Reference(id=id, name=name, url=url)

    @classmethod
    def create_custommetadata(cls, key: str, val: str):
        return CustomMetaData(key=key, val=val)

    @classmethod
    def create_analysis(
        cls, id, title: Content, intro: Content, desc: Content,
        risk: Risk, cvss_v3: CVSSv3, business_implication: Content,
        correct_implementation: Content, incorrect_implementation: Content,
        regulatory: Regulatory, vulnerability_references: Content,
        findings: List[Content]=[], tags: List[Tag]=[],
        attachments: List[Attachment]=[]
    ):
        return Analysis(
            id, title, intro, desc, risk, cvss_v3, business_implication,
            correct_implementation, incorrect_implementation, regulatory,
            vulnerability_references, findings, tags, attachments
        )

    @classmethod
    def create_content(cls, text: str, html: str, markdown: str):
        return Content(text=text, html=html, markdown=markdown)

    @classmethod
    def create_risk(cls, **kwargs):
        return Analysis.create_risk(**kwargs)

    @classmethod
    def create_regulatory(cls, **kwargs):
        return Analysis.create_regulatory(**kwargs)

    @classmethod
    def parse_cvssv3_vector(cls, **kwargs):
        return CVSSv3.parse_vector(**kwargs)

    @classmethod
    def get_risk_color(cls, risk):
        return cls.RISK_COLOR.get(risk, '')

    def _count_severity(self, label):
        return len(
            list(filter(
                lambda x: x.risk.computed_value_label.lower() == label,
                self.analyses
            ))
        )

    def _percent_severity(self, count):
        return round((count / len(self.analyses)) * 100, 2)

    @property
    def critical_count(self):
        return self._count_severity('critical')

    @property
    def high_count(self):
        return self._count_severity('high')

    @property
    def medium_count(self):
        return self._count_severity('medium')

    @property
    def low_count(self):
        return self._count_severity('low')

    @property
    def passed_count(self):
        return self._count_severity('passed')

    @property
    def untested_count(self):
        return self._count_severity('untested')

    @property
    def critical_percent(self):
        return self._percent_severity(self.critical_count)

    @property
    def high_percent(self):
        return self._percent_severity(self.high_count)

    @property
    def medium_percent(self):
        return self._percent_severity(self.medium_count)

    @property
    def low_percent(self):
        return self._percent_severity(self.low_count)

    @property
    def passed_percent(self):
        return self._percent_severity(self.passed_count)

    @property
    def untested_percent(self):
        return self._percent_severity(self.untested_count)

    @property
    def svg_chart(self):
        tpl = (
            '<circle cx="21" cy="21" r="15.91549430918954" stroke-width="8" '
            'stroke="{}" stroke-dasharray="{} {}" stroke-dashoffset="-{}" '
            'fill="transparent"></circle>'
        )
        sector = ''
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
            'data:image/svg+xml;utf8,'
            '<svg xmlns="http://www.w3.org/2000/svg" '
            'xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" '
            'width="216px" height="216px" viewBox="0 0 42 42">{}</svg>'
        ).format(sector)
