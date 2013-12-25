import os
import shutil
import time
from unittest import TestCase

import sublime_info

from sublime_plugin_tests_base import Base

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
        # Clean up the tmp files if they exist
        if os.path.exists('/tmp/hi'):
            os.unlink('/tmp/hi')
        if os.path.exists('/tmp/valid_ready'):
            os.unlink('/tmp/valid_ready')

        # Install test-files/valid into sublime_info.plugin_directory
        plugin_dir = os.path.join(sublime_info.get_package_directory(), 'valid')
        if os.path.exists(plugin_dir):
            shutil.rmtree(plugin_dir)
        shutil.copytree(__dir__ + '/test_files/valid/', plugin_dir)

        # TODO: Run an action on the plugin with an assertion inside (as we would in a normal test)
        base = Base(auto_kill_sublime=os.environ.get('SUBLIME_AUTO_KILL'))
        result = base.run_test("""
import os
import time
import sublime

def run():
    while (not os.path.exists('/tmp/valid_ready') or os.stat('/tmp/valid_ready').st_size == 0):
        time.sleep(0.1)
    sublime.active_window().run_command('sublime_plugin_tests_base_valid')
""")

        # Assert result is passing
        print result
        self.assertEqual(result['success'], True)

        # Wait for /tmp/hi to exist (async troubles)
        while (not os.path.exists('/tmp/hi') or os.stat('/tmp/hi').st_size == 0):
            time.sleep(0.1)

        # Clean up the files
        shutil.rmtree(plugin_dir)
        os.unlink('/tmp/hi')
        os.unlink('/tmp/valid_ready')

    def test_failing_plugin(self):
        # TODO: Install test-files/failing into sublime_info.plugin_directory
        # TODO: Run an action on the plugin with an assertion inside (as we would in a normal test)
        # TODO: Assert result is failure and error occurred
        pass
