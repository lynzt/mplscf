import sys
import re
import time
import requests

import modules.mplscf_helper as mplscf_helper
from utils import utils
from people_names import people_names
from bs4 import BeautifulSoup

# import modules.psql.candidates as candidates_model

def scrape_candidate_docs(html):
    soup = BeautifulSoup(html, "html.parser")

    candidates_tables = get_candidates_table(soup)
    candidates_rows = get_candidates_rows(candidates_tables)
    row_counter = 0
    for row in candidates_rows:
        row_counter+=1
        candidates_data = get_candidates_data(row)
        if row_counter > 10:
            sys.exit(0)
        process_candidate_data(candidates_data)

def get_candidates_table(soup):
    return soup.find('table', attrs={'id': 'table'})

def get_candidates_rows(soup):
    return soup.findAll('tr')

def get_candidates_data(soup):
    return soup.findAll(['td', 'th'])


def process_candidate_data(candidate_data):
    candidate = build_candidate(candidate_data)
    print ("candidate...")
    print (candidate)

    # if candidate:
    #     print ("candidate: %s" % candidate['slug_name'])
    #     candidates_model.upsert_candidates(candidate)


def build_candidate(candidate_data):
    name, committee, registration_date, termination_date, location, office, district, ytd_revenues, ytd_expenses, cash_balance = [(c.text).strip() for c in candidate_data]
    if name == 'Candidate name':
        return None

    candidate_name = people_names.split_name(name, 'lfm')
    candidate = {
        "first_name": candidate_name['first_name'],
        "middle_name": candidate_name['middle_name'],
        "last_name": candidate_name['last_name'],
        "slug_name": candidate_name['slug_name'],
        "committee_name": committee,
        "committee_slug_name": utils.slugify_string(committee),
        "registration_date": registration_date,
        "termination_date": termination_date,
        "location": location,
        "office": office,
        "district": district,
        "ytd_revenues": ytd_revenues,
        "ytd_expenses": ytd_expenses,
        "cash_balance": cash_balance,
        "created_at": "now()",
        "updated_at": "now()"
    }
    return candidate


def get_candidate_ids():
    # return [746, 935]
    return [746]

def main(args):
    cfrs_ids = get_candidate_ids()

    for id in cfrs_ids:
        print (id)

        url = 'http://www16.co.hennepin.mn.us/cfrs/getreports.do'
        print (url)
        r = requests.post(url, data = {'ids': id})
        html = r.text
        print (html)

        scrape_candidate_docs(html)



if __name__ == '__main__':
    main(sys.argv)

# docker run -it --rm --name mncf-scripts --env-file ./dev/dev.env -v "$PWD":/usr/src/app --link postgres-mncf:postgres python/mncf-scripts python ./scripts/get_candidates.py
