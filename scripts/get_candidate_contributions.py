import sys
import re
import requests

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

def process_contributions(reader, candidate_id):
    counter = 0
    last_ind = None
    for row in reader:
        counter+=1
        if counter == 1:
            headers = gsheets_readonly.get_headers(row)
            continue

        row_results = gsheets_readonly.get_row_data(row, headers)
        if row_results['empty_row']:
            print ("***** skipping row")
            continue

        row_data = row_results['data']
        last_ind = process_individual(row_data, last_ind, candidate_id)

        # if counter > 30:
        #     sys.exit(0)

    # date	name	employer	description_in_kind	previous_total	contribution	contribution_in_kind	ytd
def process_individual(row_data, last_ind, candidate_id):
    print ("\n\nprocess_individual...")
    print (row_data)
    print (last_ind)

    if row_data['name'] == '' and row_data['employer'] != '':
        individual = update_employer_name(row_data, last_ind['source_id'])

    if row_data['date'] == '':
        return last_ind

    individual = build_individual(row_data)
    if row_data['name'] == '':
        individual['slug_name'] = last_ind['slug_name']

    individual_db = individuals_model.touch_individual(individual)
    individual['source_id'] = individual_db['id']
    individual['target_id'] = candidate_id
    contributions_model.upsert_contributions(individual)

    return individual

def update_employer_name(row_data, last_ind_id):
    individual_db = individuals_model.get_individual_by_id({'id': last_ind_id})
    if not is_value_present(row_data, individual_db):
        append_employer_name(row_data, last_ind_id)


def is_value_present(row_data, individual_db):
    # individual_db = individuals_model.get_individual_by_id({'id': last_ind_id})
    my_regex = re.escape(row_data['employer'])

    if re.search(my_regex, individual_db['employer'], re.IGNORECASE):
        return True
    else:
        return False


def append_employer_name(row_data, last_ind_id):
    individuals_model.get_update_append_employer({'field': 'employer', 'value': ' ' + row_data['employer'], 'id': last_ind_id})


def build_individual(row_data):
    ind_name = people_names.split_name(row_data['name'], 'fml')
    individual = {
        'first_name': ind_name['first_name'],
        'middle_name': ind_name['middle_name'],
        'last_name': ind_name['last_name'],
        'slug_name': ind_name['slug_name'],
        'address1': None,
        'address2': None,
        'city': None,
        'state': None,
        'zip': None,
        'employer': row_data['employer'],
        'date': mplscf_helper.convert_mmddyy_to_yyyymmdd(row_data['date'], '/'),
        'in_kind': row_data['in_kind'],
        'in_kind_description': row_data['in_kind_description'],
        'amount': mplscf_helper.convert_money_to_decimal(row_data['amount'])
    }
    return individual



def main(args):
    sheet_id = '1lohaanU1mZLGUQtQQA1qf6SykFnl8n2j3W8StNzwrsg'
    candidate_id = 32
    reader = gsheets_readonly.get_gSheet(sheet_id)

    process_contributions(reader, candidate_id)



if __name__ == '__main__':
    main(sys.argv)

# docker run -it --rm --name mncf-scripts --env-file ./dev/dev.env -v "$PWD":/usr/src/app --link postgres-mncf:postgres python/mncf-scripts python ./scripts/get_candidates.py
