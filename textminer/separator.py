import re

def words(txt):
    match = re.findall(r"\b[\d]*[A-Za-z-]+\b", txt)
    if match:
        return match


def phone_number(txt):
    match = re.search(r"\(?(\d{3})\)?[- \.]?(\d{3})[-\.]?(\d{4})", txt)
    if match:
        area, prefix, last_four = match.groups()
        seven_dig = prefix + "-" + last_four
        phone_dict = {}
        phone_dict["area_code"] = area
        phone_dict["number"] = seven_dig
        return phone_dict


def zipcode(txt):
    match = re.search(r"^(?P<zip>\d{5})(-(?P<plus4>\d{4}))?$", txt)
    if match:
        return match.groupdict()


def date(txt):
    match =  re.search("""(?P<first>\d{1,})     # Find 1 or more digits
                          [/-]                  # Then find / or -
                          (?P<second>\d{1,2})   # Then find 1 or 2 digits
                          [/-]                  # Then find / or -
                          (?P<third>\d{1,})$    # Then find 1 or more digits
                       """, txt, re.VERBOSE)
    if match:
        date_dict = match.groupdict()
        dates = {}
        if len(date_dict['first']) == 4:
            dates['year'] = int(date_dict['first'])
            dates['month'] = int(date_dict['second'])
            dates['day'] = int(date_dict['third'])
        else:
            dates['month'] = int(date_dict['first'])
            dates['day'] = int(date_dict['second'])
            dates['year'] = int(date_dict['third'])
        return dates


def money(txt):
    match = re.search(r"^(\$)((?:\d{1,3}(?:,\d{3})*)|(?:\d+))(\.\d{2})?$", txt)
    if match:
        c_dict = {}
        curr, dollars, cents = match.groups()
        dollars = dollars.replace(",", "")
        c_dict['currency'] = curr
        c_dict['amount'] = int(dollars)
        if cents:
            cents = float(cents)
            c_dict['amount'] += cents
            return c_dict
        return c_dict


def dates(txt):
    match =  re.search("""(?P<first>\d{1,})     # Find 1 or more digits
                          [/-]                  # Then find / or -
                          (?P<second>\d{1,2})   # Then find 1 or 2 digits
                          [/-]                  # Then find / or -
                          (?P<third>\d{1,})$    # Then find 1 or more digits
                       """, txt, re.VERBOSE)
    if match:
        date_dict = match.groupdict()
        dates = {}
        if len(date_dict['first']) == 4:
            dates['year'] = int(date_dict['first'])
            dates['month'] = int(date_dict['second'])
            dates['day'] = int(date_dict['third'])
        else:
            dates['month'] = int(date_dict['first'])
            dates['day'] = int(date_dict['second'])
            dates['year'] = int(date_dict['third'])
        return dates


def hard_date(txt):
    match = re.search(r"(?:(?:(?:^(\d{4}) (\w{3,}) (\d{2})))|(?:(?:^(\w{3})\. (\d{1,2}), (\d{4}))))", txt)
    if match:
        year1, month1, day1, month2, day2, year2 = match.groups()
        date_dict = {'month': None, 'day': None, 'year': None}
        if year1:
            date_dict['year'] = int(year1)
            date_dict['day'] = int(day1)
            if month1 == 'Jan' or 'January':
                #can do the rest of the months to pass all months
                date_dict['month'] = 1
            return date_dict
        else:
            date_dict['year'] = int(year2)
            date_dict['day'] = int(day2)
            if month2 == 'Jan' or 'January':
                #can do the rest of the months to pass all months
                date_dict['month'] = 1
            return date_dict