from os import environ
from datetime import datetime

from django import template
from django.conf import settings
from django.template import Template, Context
from django.template.engine import Engine

from ak_vendor.utils import dict2obj
from ak_vendor.seed import file_data, whitelabel_data
from ak_vendor.constants import REPORT_PATH, OUTPUT_PATH
from ak_vendor.enums import RiskEnum

settings.configure(DEBUG=False)
register = template.Library()
file = dict2obj(file_data)
whitelabel = dict2obj(whitelabel_data)
pwd = environ['PWD']
content = ""


with open(REPORT_PATH, "r") as input_file:
    """
    WARNING: DO NOT MODIFY TEMPLATE STRING
    """
    template_string = input_file.read()
    ts_list = template_string.split('{% trans "')
    ts_1 = ts_list[0]
    ts_rest = [ts.replace('" %}', '', 1) for ts in ts_list[1:]]
    ts_rest.insert(0, ts_1)
    template_compiled = "".join(ts_rest)
    template = Template(template_compiled, engine=Engine())
    context = Context(dict(
        file=file, whitelabel=whitelabel, RiskEnum=RiskEnum, chart_url="Some URL",
        rating=50.5, date=str(datetime.now())))
    content = template.render(context)

with open(REPORT_PATH, "w") as report_file:
    report_file.write("{% load i18n %}\n" + template_string)

with open(OUTPUT_PATH, "w") as output_file:
    output_file.write(content)
