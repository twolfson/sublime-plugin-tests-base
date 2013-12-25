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
    def test_valid_plugin(self):
        # Run an action on the plugin
        base = Base(auto_kill_sublime=os.environ.get('SUBLIME_AUTO_KILL'))
        result = base.run_test()

        # Assert result is passing
        self.assertEqual(result['success'], True)

    def test_failing_plugin(self):
        # Run a failing action on the plugin
        base = Base(auto_kill_sublime=os.environ.get('SUBLIME_AUTO_KILL'))
        result = base.run_test("""
import sublime

def run():
    assert sublime == None
""")

        # Assert result is failure and error occurred
        self.assertIn('AssertionError', result['meta_info'])
        self.assertEqual(result['success'], False)
