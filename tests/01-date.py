import unittest

from unittest.mock import patch
from unittest.mock import Mock
from unittest.mock import MagicMock

import os,sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../lib"))

import logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger()

from zigicalendar.date import Date

class TestDate(unittest.TestCase):


    def test_dateCreate(self):
        self.assertEqual(Date(1615371300,'UTC').minutes(),26922855)

    def test_fromISO8601(self):
        self.assertEqual(Date.fromISO8601('2021-03-10T10:15:13+00:00').minutes(),26922855)

    def test_dateDays(self):
        """ Number of days since 1970 """
        self.assertEqual(Date(1615371300,'UTC').days(),18696)

    def test_dateDay(self):
        """ Start of the day """
        self.assertEqual(Date(1615371300,'UTC').day().minutes(),26922240)

    def test_dateNight(self):
        """ End of the day """
        self.assertEqual(Date(1615371300,'UTC').day().minutes(),26922240)

    def test_dateCompare(self):
        """ Compare dates """
        self.assertGreater(Date(1615381300,'UTC'), Date(1615371300,'UTC'))


if __name__ == '__main__':
    unittest.main();