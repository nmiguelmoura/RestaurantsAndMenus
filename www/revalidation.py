import re

class Re_Validation:
    def __init__(self):
        pass

    def validate_restaurant_name(self, name):
        NAME_RE = re.compile(r"^[a-zA-Z0-9_-]{1,80}$")
        response = NAME_RE.match(name)
        print "##############"
        print response
