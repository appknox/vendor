import json
import os

data = json.load(
    open(os.path.join(os.path.dirname(__file__), 'owasp.json'))
)
