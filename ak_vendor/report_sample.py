import json
from os.path import dirname, abspath
from django import template
from django.conf import settings
from django.template import Template, Context
from django.template.engine import Engine
from django.core.wsgi import get_wsgi_application
from ak_vendor.report import Report

settings.configure()
application = get_wsgi_application()

CUR_DIR = dirname(abspath(__file__))
template.Library()


class ReportHTMLExporter:
    def __init__(self, report):
        self.report = report

    def to_html(self):
        tpl = open("{}/report/report_template.html".format(CUR_DIR)).read()
        template = Template(
            tpl, engine=Engine(libraries={"i18n": "django.templatetags.i18n"})
        )
        context = Context({"report": self.report})
        content = template.render(context)
        return content

    def to_html_file(self, path=""):
        with open("{}/output.html".format(path), "w") as file:
            tpl = self.to_html()
            file.write(tpl)


data = json.load(open("{}/report_sample1.json".format(CUR_DIR)))
report_obj = Report.from_json(data)
ReportHTMLExporter(report_obj).to_html_file(CUR_DIR)
