#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: report.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2017-03-15
"""

from ak_vendor.utils import dict2obj


entries = {
    "a": 1,
    "b": {
        "c": {
            "d": 2,
            "e": [{"a": 1}],
        }
    }
}

obj = dict2obj(entries)
print(obj.a)
print(obj.b.c.d)
print(obj.b.c.e[0].a)
