import re

def phone_numbers(txt):
    return re.findall(r"\(?\d{3}\)?[- \.]?\d{3}[-\.]?\d{4}", txt)
