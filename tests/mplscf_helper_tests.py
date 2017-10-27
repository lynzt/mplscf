import unittest
import os
import re
from decimal import Decimal

import scripts.modules.mplscf_helper as mplscf_helper

class MplscfHelperTests(unittest.TestCase):
    def test_convert_money_to_decimal(self):
        self.assertEqual(mplscf_helper.convert_money_to_decimal('$0.00'), Decimal('0'))
        self.assertEqual(mplscf_helper.convert_money_to_decimal('$100'), Decimal('100'))
        self.assertEqual(mplscf_helper.convert_money_to_decimal('$100,000'), Decimal('100000'))
        self.assertEqual(mplscf_helper.convert_money_to_decimal('$1,422.86'), Decimal('1422.86'))
        self.assertEqual(mplscf_helper.convert_money_to_decimal('1000'), Decimal('1000'))

    def test_expand_date(self):
        self.assertEqual(mplscf_helper.convert_mmddyy_to_yyyymmdd('7/25/17', '/'), '2017-07-25')
        self.assertEqual(mplscf_helper.convert_mmddyy_to_yyyymmdd('2/2/17', '/'), '2017-02-02')
        self.assertEqual(mplscf_helper.convert_mmddyy_to_yyyymmdd('3-4-17', '-'), '2017-03-04')
        self.assertEqual(mplscf_helper.convert_mmddyy_to_yyyymmdd('2017-10-05', '-'), '2017-10-05')


# docker run -it --rm --name mncf-scripts --env-file ./dev/dev.env -v "$PWD":/usr/src/app python/mncf-scripts python3 -m unittest discover -s tests -p "*_tests.py"
