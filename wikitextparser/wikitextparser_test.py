"""Run all tests *_test.py modules."""


import unittest

import wikitextparser as wtp


class Tag(unittest.TestCase):

    """Test the Tag class."""

    @unittest.expectedFailure
    def test_basic(self):
        t = wtp.Tag('<ref>text</ref>')


if __name__ == '__main__':
    tests = unittest.defaultTestLoader.discover('.', '*_test.py')
    runner = unittest.runner.TextTestRunner()
    runner.run(tests)
