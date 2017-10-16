import unittest
import os
import re
from decimal import Decimal

import scripts.modules.mplscf_helper as mplscf_helper
# import fixtures.contributions_for_omar as contributions_for_omar

class MplscfHelperTests(unittest.TestCase):
    def test_convert_money_to_decimal(self):
        self.assertEqual(mplscf_helper.convert_money_to_decimal('$0.00'), Decimal('0'))
        self.assertEqual(mplscf_helper.convert_money_to_decimal('$100'), Decimal('100'))
        self.assertEqual(mplscf_helper.convert_money_to_decimal('$100,000'), Decimal('100000'))
        self.assertEqual(mplscf_helper.convert_money_to_decimal('$1,422.86'), Decimal('1422.86'))

# docker run -it --rm --name mncf-scripts --env-file ./dev/dev.env -v "$PWD":/usr/src/app python/mncf-scripts python -m unittest discover -s tests -p "*_tests.py"
