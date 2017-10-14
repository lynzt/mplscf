import sys
import re
import time
import requests

import modules.mncf_helper as mncf_helper
from utils import utils
from people_names import people_names
from bs4 import BeautifulSoup

import modules.psql.candidates as candidates_model

def scrape_candidates(html):
    soup = BeautifulSoup(html, "html.parser")

    candidates_tables = get_candidates_tables(soup)

    for table in candidates_tables:
        row_counter = 0
        candidates_rows = get_candidates_rows(table)
        for row in candidates_rows:
            row_counter+=1
            candidates_data = get_candidates_data(row)
            # if row_counter > 10:
            #     sys.exit(0)
            process_candidate_data(candidates_data)

def get_candidates_tables(soup):
    return soup.findAll('table')

def get_candidates_rows(soup):
    return soup.findAll('tr')

def get_candidates_data(soup):
    return soup.findAll('td')


def process_candidate_data(candidate_data):
    candidate = build_candidate(candidate_data)
    if candidate:
        print ("candidate: %s" % candidate['slug_name'])
        candidates_model.upsert_candidates(candidate)


def build_candidate(candidate_data):
    name, committee, registration_id, office, district, eis_stmt, term_date, last_filed, campaign_reports = [(c.text).strip() for c in candidate_data]
    if name == 'Candidate - Party':
        return None

    name_party = mncf_helper.split_candidate_name_party(name)
    candidate_name = people_names.split_name(name_party['name'], 'lfm')
    candidate = {
        "first_name": candidate_name['first_name'],
        "middle_name": candidate_name['middle_name'],
        "last_name": candidate_name['last_name'],
        "slug_name": candidate_name['slug_name'],
        "party": name_party['party'],
        "committee_name": committee,
        "committee_slug_name": utils.slugify_string(committee),
        "registration_id": registration_id,
        "office": office,
        "district": district,
        "created_at": "now()",
        "updated_at": "now()"
    }
    return candidate


def main(args):

    candidates_url = 'http://www.cfboard.state.mn.us/campfin/candatoz.html'
    r = requests.get(candidates_url)
    html = r.text

    scrape_candidates(html)



if __name__ == '__main__':
    main(sys.argv)

# docker run -it --rm --name mncf-scripts --env-file ./dev/dev.env -v "$PWD":/usr/src/app --link postgres-mncf:postgres python/mncf-scripts python ./scripts/get_candidates.py
