
import unittest

from pyutils import paths


class TestPyUtils(unittest.TestCase):

    def test_001_guess_package(self):
        current_package = paths.guess_package()
        self.assertEqual(current_package, 'tests')

