from os import environ
from datetime import datetime

from django import template
from django.conf import settings
from django.template import Template, Context
from django.template.engine import Engine

from ak_vendor.utils import dict2obj
from ak_vendor.seed import file_data
from ak_vendor.constants import REPORT_PATH, OUTPUT_PATH
from ak_vendor.enums import RiskEnum

settings.configure(DEBUG=False)
register = template.Library()
file = dict2obj(file_data)
pwd = environ['PWD']
content = ""


with open(REPORT_PATH, "r") as input_file:
    template_string = input_file.read()
    template = Template(template_string, engine=Engine())
    context = Context(dict(
        file=file, RiskEnum=RiskEnum, chart_url="Some URL", rating=50.5,
        date=str(datetime.now())))
    content = template.render(context)

with open(OUTPUT_PATH, "w") as output_file:
    output_file.write(content)
