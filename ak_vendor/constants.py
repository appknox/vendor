#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: constants.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-11-07
"""

from os.path import dirname, abspath

RISK_ENUM_UNKNOWN = -1
RISK_ENUM_PASSED = 0
RISK_ENUM_LOW = 1
RISK_ENUM_MEDIUM = 2
RISK_ENUM_HIGH = 3
RISK_ENUM_CRITICAL = 4

VENDOR_DIR = dirname(abspath(__file__))
REPORT_PATH = "%s/report.html" % VENDOR_DIR
OUTPUT_PATH = "%s/output.html" % VENDOR_DIR
