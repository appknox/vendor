#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: enums.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-11-07
"""

from orm_choices import choices_with_unknown as choices

from ak_vendor.constants import RISK_ENUM_NONE, RISK_ENUM_LOW, \
    RISK_ENUM_MEDIUM, RISK_ENUM_HIGH


@choices
class ProductEnum:
    class Meta:
        APPKNOX = [0, 'Appknox']
        DEVKNOX = [1, 'Devknox']


@choices
class PlatformEnum:
    '''
    Platform Type Enum
    WARNING: This should be same as Moriarty's enum
    '''
    class Meta:
        ANDROID = [0, 'Android']
        IOS = [1, 'iOS']
        WINDOWS = [2, 'Windows']


@choices
class DeviceTypeEnum:
    """
    Device type enum
    """
    class Meta:
        NO_PREFERENCE = [0, 'No Preference']
        PHONE_REQUIRED = [1, 'Phone Required']
        TABLET_REQUIRED = [2, 'Tablet Required']


@choices
class DynamicStatusEnum:
    '''
    The Dynamic scanning status
    '''
    class Meta:
        NONE = [0, 'None']
        BOOTING = [1, 'Booting']
        READY = [2, 'Ready']
        SHUTTING_DOWN = [3, 'Shutting Down']
        DOWNLOADING = [4, 'Downloading Package']
        INSTALLING = [5, 'Installing Package']
        LAUNCHING = [6, 'Launching App']
        HOOKING = [7, 'Doing Magic']


@choices
class RiskEnum:
    '''
    The risk level that is associated with an analysis
    '''
    class Meta:
        NONE = [RISK_ENUM_NONE, 'None']
        LOW = [RISK_ENUM_LOW, 'Low']
        MEDIUM = [RISK_ENUM_MEDIUM, 'Medium']
        HIGH = [RISK_ENUM_HIGH, 'High']


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


@choices
class UserTypeEnum:
    '''
    Use Types
    '''
    class Meta:
        APPKNOX = [1, 'Appknox']
        DEVKNOX = [2, 'Devknox']
