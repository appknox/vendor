#! /bin/bash
#
# report.sh
# Copyright (C) 2017 dhilipsiva <dhilipsiva@gmail.com>
#
# Distributed under terms of the MIT license.
#

set -x
python ak_vendor/report.py
open ak_vendor/output.html
weasyprint ak_vendor/output.html ak_vendor/report.pdf
# open ak_vendor/report.pdf
