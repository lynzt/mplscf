import unittest
import os
import re

import scripts.modules.mncf_helper as mncf_helper
# import fixtures.contributions_for_omar as contributions_for_omar

class UtilsTests(unittest.TestCase):
    def test_split_candidate_name_party(self):
        name_party = mncf_helper.split_candidate_name_party('Thao, Kaying')
        self.assertEqual(name_party['name'], 'Thao, Kaying')
        self.assertEqual(name_party['party'], '')

        name_party = mncf_helper.split_candidate_name_party('Thao, Kaying - DFL')
        self.assertEqual(name_party['name'], 'Thao, Kaying')
        self.assertEqual(name_party['party'], 'DFL')

    def test_read_csv_result(self):
        csv_data = mncf_helper.read_csv_result('''"11-03-2016","Individual","Abdalla, Abdulkadir D","Fridley","MN","Self employed Business Owner","No","","250.00",
        "02-18-2016","Individual","Abdi, Cawo M","Minneapolis","MN","U of M","No","","300.00",''')
        for rows in csv_data:
            self.assertEqual(len(rows), 10)

    def test_remove_new_from_name(self):
        self.assertEqual(mncf_helper.remove_new_from_name('52nd-senate-district-dfl-new'), '52nd-senate-district-dfl')
        self.assertEqual(mncf_helper.remove_new_from_name('no-new-at-end'), 'no-new-at-end')
        self.assertEqual(mncf_helper.remove_new_from_name('no-new-at-endnew'), 'no-new-at-endnew')

# docker run -it --rm --name mncf-scripts --env-file ./dev/dev.env -v "$PWD":/usr/src/app python/mncf-scripts python -m unittest discover -s tests -p "*_tests.py"
