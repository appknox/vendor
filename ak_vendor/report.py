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

from os import environ

from django.conf import settings
from django.template import Template, Context
from django.template.engine import Engine

from ak_vendor.utils import dict2obj
from ak_vendor.seed import file_data
from ak_vendor.constants import REPORT_PATH, OUTPUT_PATH

settings.configure(DEBUG=False)
file = dict2obj(file_data)
pwd = environ['PWD']
content = ""

with open(REPORT_PATH, "r") as input_file:
    template_string = input_file.read()
    template = Template(template_string, engine=Engine())
    context = Context({"file": file})
    content = template.render(context)

with open(OUTPUT_PATH, "w") as output_file:
    output_file.write(content)
