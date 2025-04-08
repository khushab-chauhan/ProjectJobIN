import re

def email_varify(email_):
    pattern = r'^[a-zA-Z0-9]+@[A-Za-z]+\.[A-Za-z]{3,6}+$'

    return re.match(pattern,email_) is not None



