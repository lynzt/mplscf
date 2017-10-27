import sys
import re
import requests

from utils import utils
from people_names import people_names
from bs4 import BeautifulSoup

import modules.mplscf_helper as mplscf_helper
import modules.psql.candidates as candidates_model

'''
get all active candidates
    load candidates table and get candidate_id (used for getting reports)
'''

def scrape_candidates(html):
    soup = BeautifulSoup(html, "html.parser")

    candidates_tables = get_candidates_table(soup)
    candidates_rows = get_candidates_rows(candidates_tables)
    row_counter = 0
    for row in candidates_rows:
        row_counter+=1
        # if row_counter > 10:
        #     sys.exit(0)
        if row_counter == 1:
            continue # skip header row...

        candidates_data = get_candidates_data(row)
        process_candidate_data(row_counter, candidates_data)

def get_candidates_table(soup):
    return soup.find('table', attrs={'id': 'table'})

def get_candidates_rows(soup):
    return soup.findAll('tr')

def get_candidates_data(soup):
    return soup.findAll(['td', 'th'])


def process_candidate_data(counter, candidate_data):
    candidate_id = get_candidate_id(candidate_data)
    candidate = build_candidate(candidate_id, candidate_data)

    if candidate:
        print ("counter: %s | %s" % (counter, candidate['slug_name']))
        candidates_model.upsert_candidates(candidate)


def get_candidate_id(candidate_data):
    onclick_str = candidate_data[0].find('a')['onclick']
    regex = re.compile('document\.getElementById\(\'ids\'\).value=\'(\d+)\'')
    match_obj = regex.search(onclick_str)
    if match_obj:
        return match_obj.group(1)
    else:
        return None


def build_candidate(candidate_id, candidate_data):
    name, committee, registration_date, termination_date, location, office, district, ytd_revenues, ytd_expenses, cash_balance = [(c.text).strip() for c in candidate_data]
    if name == 'Candidate name':
        return None

    candidate_name = people_names.split_name(name, 'lfm')
    candidate = {
        "cfrs_id": candidate_id,
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
        "ytd_revenues": mplscf_helper.convert_money_to_decimal(ytd_revenues),
        "ytd_expenses": mplscf_helper.convert_money_to_decimal(ytd_expenses),
        "cash_balance": mplscf_helper.convert_money_to_decimal(cash_balance),
        "created_at": "now()",
        "updated_at": "now()"
    }
    return candidate


def main(args):
    cmd = ['ocrmypdf',  '--deskew', '--clean', '--remove-background', filename, filename]



    logging.info(cmd)
    proc = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = proc.stdout.read()
    if proc.returncode == 6:
        print("Skipped document because it already contained text")
    elif proc.returncode == 0:
        print("OCR complete")
    logging.info(result)

    # all active candidates
    url = 'http://www16.co.hennepin.mn.us/cfrs/search.do?searchBy=candidate&ps=181&pn=0&alpha=&filterBy=active&city=&office=&district=#'
    r = requests.get(url)
    html = r.text

    scrape_candidates(html)



if __name__ == '__main__':
    main(sys.argv)

# docker run -it --rm --name mncf-scripts --env-file ./dev/dev.env -v "$PWD":/usr/src/app --link postgres-mncf:postgres python/mncf-scripts python ./scripts/get_candidates.py
