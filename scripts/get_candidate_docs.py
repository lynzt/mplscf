import sys
import os
import requests
import urllib.request

import modules.mplscf_helper as mplscf_helper
from file_utils import file_utils
from bs4 import BeautifulSoup

import modules.psql.candidates as candidates_model
import modules.psql.documents as documents_model
pdf_dif = './scripts/pdfs/'

'''
get candidate documents
    candidates to get from query (location, office, district, etc)
    download pdf
    store download details in downloads table
'''

def scrape_candidate_docs(candidate, html, download_pdf = False):
    soup = BeautifulSoup(html, "html.parser")
    doc_links = get_reports_links(soup)
    dir_path = determine_dir_path(candidate)
    file_utils.touch_directory(dir_path)
    file_utils.touch_directory(dir_path)

    for link in doc_links:
        href = link['href']
        name = determine_filename(link.get_text())
        if name == 'adobe_acrobat®_reader': # skip link for adobe reader
            continue
        print ("\tdocument: %s" % (name))
        if download_pdf:
            get_candidate_doc(href, dir_path, name)
        document = build_document(candidate['id'], name, href, dir_path)
        documents_model.touch_documents(document);

def get_reports_links(soup):
    return soup.find('form').findAll('a')

def determine_filename(name):
    return mplscf_helper.replace_space_with_underscore(name).lower()

def determine_dir_path(candidate):
    print (candidate['slug_name'])
    candidate_name = '%s_%s_%s' % (candidate['last_name'], candidate['first_name'], candidate['cfrs_id'])
    return pdf_dif + candidate_name.lower()

def get_candidate_doc(href, dir_path, filename):
    filename_with_path = '%s/%s.pdf' % (dir_path, filename)
    url = 'http://www16.co.hennepin.mn.us/cfrs/%s' % (href)
    urllib.request.urlretrieve(url, filename_with_path)


def build_document(candidate_id, name, href, file_path):
    return {
        "candidate_id": candidate_id,
        "name": name,
        "href": href,
        "file_path": file_path,
        "created_at": "now()",
        "updated_at": "now()"
    }

def create_candidate_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

def get_candidate_ids(params, candidates_filter=[]):
    candidates = candidates_model.get_candidates_by_location(params)
    candidates = list(filter(lambda x: x['ytd_revenues'] > 0 or x['ytd_expenses'] > 0, candidates))

    if len(candidates_filter) > 0:
        return list(filter(lambda x: x['cfrs_id'] in candidates_filter, candidates))
    else:
        return candidates

def main(args):
    candidates = get_candidate_ids({'location': 'minneapolis', 'office': 'mayor'})
    # candidates = get_candidate_ids({'location': 'minneapolis'}, [746, 935])

    for candidate in candidates:
        url = 'http://www16.co.hennepin.mn.us/cfrs/getreports.do'
        r = requests.post(url, data = {'ids': candidate['cfrs_id']})
        html = r.text
        # scrape_candidate_docs(candidate, html)
        scrape_candidate_docs(candidate, html, True)

if __name__ == '__main__':
    main(sys.argv)

# docker run -it --rm --name mplscf-scripts --env-file ./dev/dev.env -v "$PWD":/usr/src/app --link postgres-mplscf:postgres python/mplscf-scripts python3 ./scripts/get_candidate_docs.py
