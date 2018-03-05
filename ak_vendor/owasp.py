import json
import os


class OWASP():
    def __init__(self, id, code, description, year):
        self.pk = id
        self.id = id
        self.code = code
        self.description = description
        self.year = year


json_data = json.load(
    open(os.path.join(os.path.dirname(__file__), 'owasp.json'))
)
data = {d['id']: OWASP(**d) for d in json_data}
