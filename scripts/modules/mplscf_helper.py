import csv
import io
import re
from decimal import Decimal

class MyDialect(csv.Dialect):
    strict = True
    skipinitialspace = True
    quoting = csv.QUOTE_ALL
    delimiter = ','
    quotechar = '"'
    lineterminator = '\n'

def read_csv_result(csv_file):
    b = io.StringIO(csv_file)
    return csv.reader(b,MyDialect())


def split_candidate_name_party(str):
    result = str.rsplit('-', 1)
    if len(result) == 1:
        return {'name': result[0].strip(), 'party': ''}
    else:
        return {'name': result[0].strip(), 'party': result[1].strip()}

def convert_mmddyy_to_yyyymmdd(date_str, delimiter):
    regex = r'^\d{1,2}' + delimiter + r'\d{1,2}' + delimiter + r'\d{2}$'
    if re.match(regex, date_str):
        date_list = date_str.split(delimiter)
        return '2017-%s-%s' % (date_list[0].zfill(2), date_list[1].zfill(2))
    return date_str

def remove_new_from_name(str):
    return re.sub('-new$','', str)

def convert_money_to_decimal(money):
    return Decimal(re.sub(r'[^\d\-.]', '', money))


def replace_space_with_underscore(str):
    return "_".join(str.split())
