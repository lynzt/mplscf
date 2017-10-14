import sys
import requests

from utils import utils

import modules.psql.candidates as candidates_model
import modules.psql.political_party_units as political_party_units_model
import modules.psql.political_committees as political_committees_model

def parse_prior_data(json, type):
    # row_counter = 0
    for data in json['items']:
        # row_counter+=1
        # if row_counter > 5:
        #     continue
        print ("rid: %s | type: %s | name: %s" % (data['id'], type, data['text']))
        update_tables(data, type)


def update_tables(data, type):
    if type == 'candidate':
        data_obj = build_candidate(data)
        candidates_model.touch_candidate(data_obj)
    elif type == 'party unit':
        data_obj = build_political_group(data)
        political_party_units_model.touch_political_party_unit(data_obj)
    elif type == 'political committee':
        data_obj = build_political_group(data)
        political_committees_model.touch_political_committee(data_obj)

def build_candidate(data):
    return {
        "committee_name": data['text'],
        "committee_slug_name": utils.slugify_string(data['text']),
        "registration_id": data['id']
    }

def build_political_group(data):
    return {
        "name": data['text'],
        "slug_name": utils.slugify_string(data['text']),
        "registration_id": data['id']
    }

def main(args):
    prior_urls = [
        {'type': 'candidate', 'url': 'http://reports.cfb.mn.gov/dataViewer/Main.php?do=ajaxResultAction&searchParam=&searchYear=&searchType=ajaxReturnPCCRegNumberJSON&searchTopItem=Select%20Candidate&submitType=json&search=&max=4000'},
        {'type': 'party unit', 'url': 'http://reports.cfb.mn.gov/dataViewer/Main.php?do=ajaxResultAction&searchParam=&searchYear=&searchType=ajaxReturnPTURegNumberJSON&searchTopItem=Select%20Political%20Party%20Unit&submitType=json&search=&max=4000'}
        # {'type': 'political committee', 'url': 'http://reports.cfb.mn.gov/dataViewer/Main.php?do=ajaxResultAction&searchParam=&searchYear=&searchType=ajaxReturnPCFRegNumberJSON&searchTopItem=Select%20Political%20Committee&submitType=json&search=&max=4000'}
    ]

    for data in prior_urls:
        r = requests.get(data['url'])
        parse_prior_data(r.json(), data['type'])

if __name__ == '__main__':
    main(sys.argv)

# docker run -it --rm --name mncf-scripts --env-file ./dev/dev.env -v "$PWD":/usr/src/app --link postgres-mncf:postgres python/mncf-scripts python ./scripts/get_committees.py
