import sys
import re
import time
import requests

from utils import utils
from bs4 import BeautifulSoup

import modules.psql.political_committees as political_committees_model
import modules.psql.alternate_names as alternate_names_model
# import modules.psql.political_party_units as political_party_units_model


def scrape_page(html, party, year):
    soup = BeautifulSoup(html, "html.parser")
    tables = get_tables(soup)
    table_counter = 0
    for table in tables:
        table_counter+=1
        if table_counter < 4:
            continue
        row_counter = 0
        rows = get_rows(table)
        for row in rows:
            row_counter+=1
            data = get_data(row)
            # if row_counter > 10:
            #     continue
            process_data(data, party, year)

def get_tables(soup):
    return soup.findAll('table')

def get_rows(soup):
    return soup.findAll('tr')

def get_data(soup):
    return soup.findAll('td')


def process_data(data, party, year):
    record_obj = build_record(data, party, year)
    if record_obj and record_obj['name'] != 'Committee':
        print ("year: %s | name: %s " % (year, record_obj['name']))
        result = political_committees_model.touch_political_committee(record_obj)
        if result['slug_name'] != record_obj['slug_name']:
            alternate_names_model.touch_alternate_name(record_obj)

def build_record(data, party, year):
    # 2006 no reports...
    if int(year) > 2006:
        committee, address, telephone, registration_id, registration_date, term_date, reports = [(c.text).strip() for c in data]
    else:
        committee, address, telephone, registration_id, registration_date, term_date = [(c.text).strip() for c in data]
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

    pages_to_scrape = [
        {'year':'2016', 'm': 'apr 04', 'url': 'https://web.archive.org/web/20160404112756/http://www.cfboard.state.mn.us/campfin/pcfatoz.html', 'party':''},
        {'year':'2015', 'm': 'may 24', 'url': 'https://web.archive.org/web/20150524091118/http://www.cfboard.state.mn.us/campfin/pcfatoz.html', 'party':''},
        {'year':'2014', 'm': 'may 08', 'url': 'https://web.archive.org/web/20140508022548/http://www.cfboard.state.mn.us/campfin/pcfatoz.html', 'party':''},
        {'year':'2013', 'm': 'may 03', 'url': 'https://web.archive.org/web/20130503144622/http://www.cfboard.state.mn.us/campfin/pcfatoz.html', 'party':''},
        {'year':'2012', 'm': 'nov 04', 'url': 'https://web.archive.org/web/20121104205208/http://www.cfboard.state.mn.us/campfin/pcfatoz.html', 'party':''},
        {'year':'2011', 'm': 'aug 21', 'url': 'https://web.archive.org/web/20110821014942/http://www.cfboard.state.mn.us/campfin/pcfatoz.html', 'party':''},
        {'year':'2010', 'm': 'may 27', 'url': 'https://web.archive.org/web/20100527154013/http://www.cfboard.state.mn.us/campfin/pcfatoz.html', 'party':''},
        {'year':'2009', 'm': 'may 24', 'url': 'https://web.archive.org/web/20090524061459/http://www.cfboard.state.mn.us/campfin/pcfatoz.html', 'party':''},
        {'year':'2008', 'm': 'mar 17', 'url': 'https://web.archive.org/web/20080317133140/http://www.cfboard.state.mn.us/campfin/pcfatoz.html', 'party':''},
        {'year':'2007', 'm': 'aug 23', 'url': 'https://web.archive.org/web/20070823030557/http://www.cfboard.state.mn.us/campfin/pcfatoz.html', 'party':''},
        {'year':'2006', 'm': 'apr 27', 'url': 'https://web.archive.org/web/20060427064942/http://www.cfboard.state.mn.us/campfin/pcfatoz.html', 'party':''},
        {'year':'2005', 'm': 'feb 10', 'url': 'https://web.archive.org/web/20050210035907/http://www.cfboard.state.mn.us/campfin/pcfatoz.html', 'party':''},
        {'year':'2005', 'm': 'feb 10', 'url': 'https://web.archive.org/web/20050210035907/http://www.cfboard.state.mn.us/campfin/pcfatoz.html', 'party':''},
        {'year':'2004', 'm': 'feb 10', 'url': 'https://web.archive.org/web/20040801000000*/http://www.cfboard.state.mn.us/campfin/pcfatoz.html', 'party':''}
    ]

    # pages_to_scrape = [pc, ppu]
    for page in pages_to_scrape:
        r = requests.get(page['url'])
        html = r.text
        scrape_page(html, page['party'], page['year'])

if __name__ == '__main__':
    main(sys.argv)

# docker run -it --rm --name mncf-scripts --env-file ./dev/dev.env -v "$PWD":/usr/src/app --link postgres-mncf:postgres python/mncf-scripts python ./scripts/get_political_groups.py
