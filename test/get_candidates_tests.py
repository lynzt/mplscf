import unittest
import sys

import scripts.get_candidates as get_candidates
import fixtures.candidates_html as candidates_html

class CandidatesTests(unittest.TestCase):
    def test_scrape_candidates(self):
        html = candidates_html.get_html();
        # result = get_candidates.scrape_candidates(html)
        # print (result)

# docker run -it --rm --name ptrack-scripts -v "$PWD":/usr/src/app --link postgres-ptrack:postgres python/ptrack python -m unittest discover -s test -p "*_tests.py"
