import re

def binary(txt):
    return re.match(r"[01]+", txt)


def binary_even(txt):
    return re.match(r"[01]+0$", txt)


def hex(txt):
    return re.match(r"\A[0-9a-fA-F]+\Z", txt)


def word(txt):
    return re.match(r"\A[\d]*[A-Za-z-]+\Z", txt)


def words(txt, count=0):
    if count == 0:
        return re.match(r"\A[\d]*[A-Za-z-\s]+\Z", txt)
    else:
        word_list = txt.split()
        if len(word_list) != count:
            return False
        else:
            return re.match(r"\A[\d]*[A-Za-z-\s]+\Z", txt)


def phone_number(txt):
    return re.match(r"\(?\d{3}\)?[- \.]?\d{3}[-\.]?\d{4}", txt)


def money(txt):

    return re.match(r"""\$              # Find dollar sign
                        ((\d{1,3}       # Find at least one digit and
                        (,\d{3})*)      # If comma find 3 digits, do this zero or more times
                        |               # OR
                        (\d+))          # Find a bunch of digits
                        (\.\d{2})?$     # Maybe find a period, if so, needs 2 digits after
                    """, txt, re.VERBOSE)


def zipcode(txt):
    return re.match(r"""(\d{5}$)            # Find 5 digits
                        |                   # OR
                        (\d{5}-\d{4}$)      # Find 5 digits, then dash, then 4 digits
                    """, txt, re.VERBOSE)


def date(txt):
    return re.match("""\d{1,}     # Find 1 or more digits
                       [/-]       # Then find / or -
                       \d{1,2}    # Then find 1 or 2 digits
                       [/-]       # Then find / or -
                       \d{1,}$    # Then find 1 or more digits
                    """, txt, re.VERBOSE)
