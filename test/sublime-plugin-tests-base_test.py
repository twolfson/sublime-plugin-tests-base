import os
import shutil
from unittest import TestCase

import sublime_info

from sublime_plugin_tests_base import sublime_plugin_tests_base

# Set up constants
__dir__ = os.path.dirname(os.path.abspath(__file__))

# Outline tests
"""
A valid Sublime Text plugin
    run via the `sublime-plugin-tests-base`
        runs its content

A failing Sublime Text plugin
    run via the `sublime-plugin-tests-base`
        catches and returns the error

# TODO: Tests for test utilities (e.g. split selection)
# TODO: Technically, those should be their own Python module but we need a good system to package them in tests first.
"""


class TestSublimeTestsBase(TestCase):
    def test_valid_plugin(self):
        # Clean up the tmp file if it exists
        if os.path.exists('/tmp/hi'):
            os.unlink('/tmp/hi')

        # Install test-files/valid into sublime_info.plugin_directory
        plugin_dir = os.path.join(sublime_info.get_package_directory(), 'valid')
        if os.path.exists(plugin_dir):
            shutil.rmtree(plugin_dir)
        shutil.copytree(__dir__ + '/test_files/valid/', plugin_dir)

        # TODO: Run an action on the plugin with an assertion inside (as we would in a normal test)

        # Clean up the files
        # os.unlink('/tmp/hi')
        shutil.rmtree(plugin_dir)

        # TODO: Assert result is passing
        self.assertTrue(bool(sublime_plugin_tests_base))

    def test_failing_plugin(self):
        # TODO: Install test-files/failing into sublime_info.plugin_directory
        # TODO: Run an action on the plugin with an assertion inside (as we would in a normal test)
        # TODO: Assert result is failure and error occurred
        self.assertTrue(bool(sublime_plugin_tests_base))
