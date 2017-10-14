import csv
import io
import re

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

def remove_new_from_name(str):
    return re.sub('-new$','', str)
