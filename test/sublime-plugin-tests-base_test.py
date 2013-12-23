from unittest import TestCase
from sublime_plugin_tests_base import sublime_plugin_tests_base

"""
A valid Sublime Text plugin
    run via the `sublime-plugin-tests-base`
        runs its content

A failing Sublime Text plugin
    run via the `sublime-plugin-tests-base`
        catches and returns the error
"""

class TestRunFunction(TestCase):
    def test_run_exists(self):
        self.assertTrue(bool(sublime_plugin_tests_base.run))
