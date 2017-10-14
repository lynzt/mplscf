import sys
import re
import time
import requests
import getopt

import modules.mncf_helper as mncf_helper
from people_names import people_names
from utils import utils
from bs4 import BeautifulSoup

import modules.psql.candidates as candidates_model
import modules.psql.individuals as individuals_model
import modules.psql.political_committees as political_committees_model
import modules.psql.political_party_units as political_party_units_model
import modules.psql.contributions as contributions_model
import modules.psql.alternate_names as alternate_names_model

def processData(candidate_rid, text):
    f1 = open('scripts/logs/get_contribution_to_candidate/missing_slug_name.csv', 'a')

    csv_file = mncf_helper.read_csv_result(text)
    counter = 0;
    for rows in csv_file:
        counter += 1
        if counter <= 7:
            continue
        contribution = build_contribution(rows, candidate_rid)
        msg = "candidate_rid: %s | name: %s | slug: %s | type: %s | date: %s | amount: %s" % (candidate_rid, contribution['name'], contribution['slug_name'], contribution['source_type'], contribution['date'], contribution['amount'])
        print (msg)
        result = check_name_in_db(contribution)

        if not result:
            result = check_alternate_names(contribution)

        if not result:
            modify_if_new_name(contribution)
            result = check_name_in_db(contribution)

        if result:
            contribution['source_id'] = result['id']
            contribution['candidate_rid'] = candidate_rid
            contributions_model.upsert_contributions(contribution)
        else:
            f1.write("%s\n" % (msg))

    candidates_model.update_last_pulled_at({'candidate_rid': candidate_rid})

def modify_if_new_name(contribution):
    modified_slug_name = mncf_helper.remove_new_from_name(contribution['slug_name'])
    contribution['committee_slug_name'] = modified_slug_name
    contribution['slug_name'] = modified_slug_name


def check_alternate_names(contribution):
    result = alternate_names_model.get_alternate_name_by_slug(contribution)
    return result

def check_name_in_db(contribution):
    if contribution['source_type'] == 'Individual':
        result = individuals_model.touch_individual(contribution)
    elif contribution['source_type'] == 'Lobbyist':
        result = individuals_model.touch_individual(contribution)
    elif contribution['source_type'] == 'Political Committee':
        result = political_committees_model.get_political_committee_by_slug_name(contribution)
    elif contribution['source_type'] == 'Political Party':
        result = political_party_units_model.get_political_party_unit_by_slug_name(contribution)
    elif contribution['source_type'] == 'Candidate Committee':
        contribution['committee_slug_name'] = contribution['slug_name']
        result = candidates_model.get_candidate_by_candidate_slug_name(contribution)
    elif contribution['source_type'] == 'Self':
        result = individuals_model.touch_individual(contribution)
    else:
        result = None
    return result

def build_contribution(rows, candidate_rid):
    date, type, contrib_name, city, state, employer, in_kind, in_kind_description, amount, empty = [(col).strip() for col in rows]
    contribution = {
        "name": contrib_name,
        "slug_name": utils.slugify_string(contrib_name),
        "date": date,
        "city": city,
        "state": state,
        "employer": employer,
        "source_type": type,
        "target_id": candidate_rid,
        "in_kind": in_kind,
        "in_kind_description": in_kind_description,
        "amount": float(amount.replace(',', '')),
        "created_at": "now()",
        "updated_at": "now()",
        "last_pulled_at": "now()"
    }

    get_name_parts(type, contrib_name, contribution)
    determine_is_lobbyist(type, contribution)
    return contribution

def determine_is_lobbyist(type, contribution):
    if type == 'Lobbyist':
        contribution['is_lobbyist'] = True
    else:
        contribution['is_lobbyist'] = False

def get_name_parts(type, name, contribution):
    print (name)
    if type == 'Individual' or type == 'Lobbyist' or type == 'Self':
        name = people_names.split_name(name, 'lfm', True)
        contribution["first_name"] = name['first_name']
        contribution["middle_name"] = name['middle_name']
        contribution["last_name"] = name['last_name']
        contribution["slug_name"] = name['slug_name']

def get_candidates_to_pull(limit):
    rids = []
    candidates = candidates_model.get_candidates_to_check_contributions(limit)
    for candidate in candidates:
        rids.append(candidate['registration_id'])
    print (rids)
    return rids

def main():
    optlist, args = getopt.getopt(sys.argv[1:], 'r:l:')
    rids = None

    for o, a in optlist:
        if o in ("-r"):
            rids = list(map(int, a.split(',')))
            break;
        elif o in '-l':
            rids = get_candidates_to_pull({'limit': a})

    if not rids:
        rids = get_candidates_to_pull({'limit': 5})
    print ("rids: %s" % rids)
    # sys.exit(0)

    for candidate_rid in rids:
        print ("\n*** candidate_rid: %s" % candidate_rid)
        url = 'http://reports.cfb.mn.gov/dataViewer/Main.php?do=csvFile'
        data = {"CandID": candidate_rid,
                    "Retrieve CSV File": "Download",
                    "contype": "999",
                    "dataGridColumns": '[{"field":"FormatDonationDate","caption":"Date","size":"50"},{"field":"DonorType","caption":"Donor Type","size":"60"},{"field":"DonorName","caption":"Donor Name","size":"100"},{"field":"City","caption":"City","size":"80"},{"field":"State","caption":"State","size":"30"},{"field":"Employer","caption":"Employer","size":"100"},{"field":"InkindTransaction","caption":"InKind","size":"30"},{"field":"InKindDescriptionText","caption":"InKind Description","size":"80"},{"field":"ContributionAmount","caption":"Amount","size":"60","style":"text-align: right"}]',
                    "district": "",
                    "office": "",
                    "party": "",
                    "searchType": "1",
                    "selectCrit": "indCriteria",
                    "sortNumber": "1",
                    "submitType": "csv",
                    "year": ""}
        r = requests.post(url, data)
        processData(candidate_rid, r.text)

if __name__ == '__main__':
    main()

# docker run -it --rm --name mncf-scripts --env-file ./dev/dev.env -v "$PWD":/usr/src/app --link postgres-mncf:postgres python/mncf-scripts python ./scripts/get_contribution_to_candidate.py
