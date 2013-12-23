from unittest import TestCase
from sublime_plugin_tests_base import sublime_plugin_tests_base


class TestRunFunction(TestCase):
    def test_run_exists(self):
        self.assertTrue(bool(sublime_plugin_tests_base.run))
