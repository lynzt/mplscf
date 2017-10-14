import sys
import re
import time
import requests

from utils import utils
from bs4 import BeautifulSoup

import modules.psql.political_committees as political_committees_model
import modules.psql.political_party_units as political_party_units_model


def scrape_page(html, party):
    soup = BeautifulSoup(html, "html.parser")
    tables = get_tables(soup)

    for table in tables:
        row_counter = 0
        rows = get_rows(table)
        for row in rows:
            row_counter+=1
            data = get_data(row)
            # if row_counter > 2:
            #     continue
            process_data(data, party)

def get_tables(soup):
    return soup.findAll('table')

def get_rows(soup):
    return soup.findAll('tr')

def get_data(soup):
    return soup.findAll('td')


def process_data(data, party):
    record_obj = build_record(data, party)
    if record_obj and record_obj['name'] != 'Committee':
        print ("record_obj['name']: %s | party: %s" % (record_obj['name'], party))
        if party == '':
            political_committees_model.touch_political_committee(record_obj)
        else:
            political_party_units_model.touch_political_party_unit(record_obj)


def build_record(data, party):
    committee, address, telephone, registration_id, registration_date, term_date, reports = [(c.text).strip() for c in data]
    result = {
        "name": committee,
        "slug_name": utils.slugify_string(committee),
        "registration_id": registration_id,
        "party": party,
        "created_at": "now()",
        "updated_at": "now()"
    }
    return result


def main(args):

    ppu = [{'url':'http://www.cfboard.state.mn.us/campfin/ppuDFL.html', 'party': 'dfl'},
        {'url': 'http://www.cfboard.state.mn.us/campfin/ppuRPM.html', 'party': 'rpm'},
        {'url': 'http://www.cfboard.state.mn.us/campfin/ppuIPM.html', 'party': 'ipm'},
        {'url': 'http://www.cfboard.state.mn.us/campfin/ppuGRP.html', 'party': 'grp'},
        {'url': 'http://www.cfboard.state.mn.us/campfin/ppuGPM.html', 'party': 'gpm'},
        {'url': 'http://www.cfboard.state.mn.us/campfin/ppuLPM.html', 'party': 'lpm'}
    ]

    pc = [{'url': 'http://www.cfboard.state.mn.us/campfin/pcfatoz.html', 'party': ''}]

    pages_to_scrape = [pc, ppu]
    for page in pages_to_scrape:
        for result in page:
            r = requests.get(result['url'])
            html = r.text
            scrape_page(html, result['party'])

if __name__ == '__main__':
    main(sys.argv)

# docker run -it --rm --name mncf-scripts --env-file ./dev/dev.env -v "$PWD":/usr/src/app --link postgres-mncf:postgres python/mncf-scripts python ./scripts/get_political_groups.py
