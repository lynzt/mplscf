import unittest
import sys

import scripts.get_candidate_docs as get_candidate_docs
import fixtures.candidates.documents_html as documents_html

class CandidateDocsTests(unittest.TestCase):
    def test_scrape_candidate_docs(self):
        html = documents_html.get_html();
        result = get_candidate_docs.scrape_candidate_docs(html)
        print (result)

# docker run -it --rm --name ptrack-scripts -v "$PWD":/usr/src/app --link postgres-ptrack:postgres python/ptrack python -m unittest discover -s test -p "*_tests.py"
