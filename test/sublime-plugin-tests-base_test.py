import os
from unittest import TestCase

import sublime_info

from sublime_plugin_tests_base import Base

# Set up constants
__dir__ = os.path.dirname(os.path.abspath(__file__))

# Outline tests
"""
A Sublime Text plugin
    run against a passing test
        tells us the test passed
    run against a failing test
        tells us the test failed
        gives us a relevant error

# TODO: Tests for test utilities (e.g. split selection)
# TODO: Technically, those should be their own Python module but we need a good system to package them in tests first.
"""


class TestSublimeTestsBase(TestCase):
    def test_passing_test(self):
        # Run a passing test
        base = Base(auto_kill_sublime=os.environ.get('SUBLIME_AUTO_KILL'))
        f = open(__dir__ + '/test_files/valid.py')
        valid_py = f.read()
        f.close()
        result = base.run_test(valid_py)

        # Assert the test passed as expected
        self.assertEqual(result['success'], True)

    def test_failing_test(self):
        # Run a failing test
        base = Base(auto_kill_sublime=os.environ.get('SUBLIME_AUTO_KILL'))
        f = open(__dir__ + '/test_files/failing.py')
        failing_py = f.read()
        f.close()
        result = base.run_test(failing_py)

        # Assert the test failed as expected is passing
        self.assertIn('AssertionError', result['meta_info'])
        self.assertEqual(result['success'], False)
