import sys
import re
import requests
import datetime

from utils import utils
from people_names import people_names
from gsheets_readonly import gsheets_readonly
from bs4 import BeautifulSoup

import modules.mplscf_helper as mplscf_helper
import modules.psql.candidates as candidates_model
import modules.psql.individuals as individuals_model
import modules.psql.contributions as contributions_model

'''
load candidate ind contributions
'''
dir_base = 'scripts/csv/'


def process_contributions(reader):
    counter = 0
    individual_contributions = {

    }
    contributions = {}
    last_ind = None
    for row in reader:
        print ("\n\n")
        counter+=1
        if counter == 1:
            headers = gsheets_readonly.get_headers(row)
            continue

        row_results = gsheets_readonly.get_row_data(row, headers)

        if row_results['empty_row']:
            print ("***** empty row... skipping")
            continue

        row_data = row_results['data']
        print (row_data)
        results = process_row(row_data, last_ind, contributions)


        if isinstance(results, list):
            for result in results:
                last_ind = validate_and_append_individual_dict(result, contributions)
        elif isinstance(results, dict):
            last_ind = validate_and_append_individual_dict(results, contributions)


        # if counter > 5:
        #     break

    output_csv_file(contributions)


def output_csv_file(contributions):
    f1 = open(dir_base + 'contributions.csv', 'w')
    st = ''
    for key, values in contributions.items():
        for d in values:
            f1.write(",".join(d.values()) + "\n")

    f1.close()

def validate_and_append_individual_dict(result, contributions):
    valid = validate_values(result)
    individual = build_individual(result)
    slug_name = individual['slug_name']
    if slug_name in contributions:
        contributions[slug_name].append(individual)
    else:
        contributions[slug_name] = [individual]

    return individual

def validate_values(result):
    valid = True
    if not is_valid_date(result['date']):
        valid = False

    if not is_valid_contribution(result['amount']):
        valid = False

    if 'in_kind' in result and not is_valid_contribution(result['in_kind']):
        valid = False


def process_row(row_data, last_ind, contributions):
    row_data = clean_fields(row_data)

    if 'last_name' in row_data:
        row_data['name'] = '%s %s' % (row_data['first_name'], row_data['last_name'])

    if row_data['name'] == '' and 'employer' in row_data and row_data['employer'] != '':
        update_employer_name(row_data, last_ind, contributions)

    if row_data['date'] == '':
        return None

    if row_data['amount'] == '':
        row_data['amount'] = '$0.00'

    if 'in_kind' in row_data and row_data['in_kind'] == '':
        row_data['in_kind'] = '$0.00'

    if '&' in row_data['name'] and 'employer' in row_data and row_data['employer'] != '':
        row_data = split_name_and_employer(row_data)

    return row_data


def update_employer_name(row_data, last_ind, contributions):
    employer = '%s %s' % (last_ind['employer'], row_data['employer'])
    ind_contras = contributions[last_ind['slug_name']]
    for ind in ind_contras:
        ind['employer'] = employer

def clean_fields(row):
    regex = r'^\s?[„,•._-]+\s?|\s?[„,•._-]+\s?$'
    return { key: re.sub(regex, '', val) for key, val in row.items() }

def is_valid_contribution(contribution):
    if contribution != 0:
        contribution = int(mplscf_helper.convert_money_to_decimal(contribution))
        return True if contribution > 0 and contribution <= 1000 else False
    #
    # if in_kind != '':
    #     in_kind = int(mplscf_helper.convert_money_to_decimal(in_kind))
    #     return True if in_kind > 0 and in_kind <= 1000 else False

    return False

def is_valid_date(date):
    year_str = (date.rsplit('/', 1))[1] # get year format '17' || 2017
    if len(year_str) > 2:
        return test_date(date, '%m/%d/%Y')
    else:
        return test_date(date, '%m/%d/%y')


def test_date(date, regex):
    try:
        datetime.datetime.strptime(date, regex).date()
        return True
    except ValueError:
        return False

def split_name_and_employer(row_data):
    regex_name = re.compile('(\w+) & (\w+) (\w+)')
    name_obj = regex_name.search(row_data['name'])
    regex_employer = re.compile('(.+)\s*\/\s*(.+)')
    employer_obj = regex_employer.search(row_data['employer'])


    if name_obj and employer_obj:
        obj1 = row_data
        obj2 = row_data

        name1 = '%s %s' % (name_obj.group(1), name_obj.group(3))
        name2 = '%s %s' % (name_obj.group(2), name_obj.group(3))
        employer1 = employer_obj.group(1)
        employer2 = employer_obj.group(2)
        amount = int(mplscf_helper.convert_money_to_decimal(row_data['amount'])) / 2

        obj1['name'] = name1
        obj1['employer'] = employer1
        obj1['amount'] = amount
        obj2['name'] = name2
        obj2['employer'] = employer2
        obj2['amount'] = amount
        return [ obj1, obj2]

def build_individual(row_data):
    print (row_data)
    ind_name = people_names.split_name(row_data['name'], 'fml')
    print ("name: %s" % ind_name['slug_name'])
    if ind_name['slug_name'] == '':
        ind_name['slug_name'] = 'unknown'

    individual = {
        'first_name': ind_name['first_name'],
        'middle_name': ind_name['middle_name'],
        'last_name': ind_name['last_name'],
        'slug_name': ind_name['slug_name'],
        'address1': save_if_value('address1', row_data),
        'address2': save_if_value('address2', row_data),
        'city': save_if_value('city', row_data),
        'state': save_if_value('state', row_data),
        'zip': save_if_value('zip', row_data),
        'employer': save_if_value('employer', row_data),
        'date': mplscf_helper.convert_mmddyy_to_yyyymmdd(row_data['date'], '/'),
        'in_kind': mplscf_helper.convert_dec_to_string(save_if_value('in_kind', row_data)),
        'in_kind_description': save_if_value('in_kind_description', row_data),
        'amount': mplscf_helper.convert_dec_to_string(row_data['amount'])
    }
    return individual


def save_if_value(field, row_data):
    return row_data[field] if field in row_data else ''


def main(args):
    # sheet_id = '1lohaanU1mZLGUQtQQA1qf6SykFnl8n2j3W8StNzwrsg' # dehn
    # sheet_id = '1V_8Zbja8reS308qgagijrevVaGWdJVC52rTJxORNqLQ' # frey
    # sheet_id = '1WJSDKibltHFlqwU0cb-k7LtzXw0sYESksFUasD0Y30o' # levy pounds
    # sheet_id = '1O26noy7lbO43XuvbV8zPKoI17dl6pb5B9eSMlbTTfLc' # flowers
    # sheet_id = '1yX_1QMHNru2b34W6jOc-MtDzLfPj9pIyUvfIFb7wIm8' # hodges
    sheet_id = '13RF7MDMmKrEzGlpJ9gNL7ORmR-IddJ7U9vccsRYlFHw' # hoch



    reader = gsheets_readonly.get_gSheet(sheet_id)

    process_contributions(reader)



if __name__ == '__main__':
    main(sys.argv)

# docker run -it --rm --name mncf-scripts --env-file ./dev/dev.env -v "$PWD":/usr/src/app --link postgres-mncf:postgres python/mncf-scripts python ./scripts/get_candidates.py
