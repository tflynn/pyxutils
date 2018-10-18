import unittest

from pyxutils import paths


class Testpyxutils1(unittest.TestCase):

    def test_1_001_guess_package(self):
        current_package = paths.guess_package()
        self.assertEqual(current_package, 'tests_1')



