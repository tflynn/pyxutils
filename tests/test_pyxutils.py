
import os
from os import path

import unittest

from pyxutils import paths


class Testpyxutils(unittest.TestCase):

    def test_001_guess_package(self):
        current_package = paths.guess_package()
        self.assertEqual(current_package, 'tests')

    def test_002_package_dir(self):
        # Cheat a little since tests are always run on source copy from the package root
        current_dir = os.getcwd()
        if current_dir.endswith('tests'):
            # PyCharm runs nose from the directory containing the tests
            actual_package_dir = current_dir
        else:
            # Run manually, nose runs the tests from the root
            actual_package_dir = path.join(current_dir, 'tests')

        computed_package_dir = paths.get_package_path(package_name='tests')
        self.assertEqual(actual_package_dir,computed_package_dir)
