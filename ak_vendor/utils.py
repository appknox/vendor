#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: utils.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2017-03-15
"""


class EmptyClass(object):
    """
    Just an empty class with nothing to see
    """
    pass


def dict2obj(d):
    if type(d) == list:
        d = [dict2obj(i) for i in d]
    try:
        d = dict(d)
    except (TypeError, ValueError):
        return d
    obj = EmptyClass()
    for k, v in d.items():
        obj.__dict__[k] = dict2obj(v)
    return obj
