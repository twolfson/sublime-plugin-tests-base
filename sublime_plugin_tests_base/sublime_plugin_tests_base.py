# Load in core dependencies
import os
import shutil
import subprocess
import time
import tempfile

# Load in 3rd party dependencies
from jinja2 import Template
from sublime_harness import Harness

# Set up local dependencies
from .logger import Logger
logger = Logger()

# Set up constants
__dir__ = os.path.dirname(os.path.abspath(__file__))


class Base(object):
    def _ensure_plugin_test_dir(self):
        # If the plugin test directory does not exist, create it
        if not os.path.exists(self._plugin_test_dir):
            os.makedirs(self._plugin_test_dir)

    def _ensure_utils(self):
        # Ensure the plugin test directory exists
        self._ensure_plugin_test_dir()

        # TODO: Use similar copy model minus the exception
        # TODO: If we overwrite utils, be sure to wait so that changes for import get picked up
        if not os.path.exists(self._plugin_test_dir + '/utils'):
            shutil.copytree(__dir__ + '/utils', self._plugin_test_dir + '/utils')

    def __init__(self, auto_kill_sublime=False):
        self.auto_kill_sublime = auto_kill_sublime

    def run_test(self, test_str):
        # Guarantee there is an output directory and launcher
        self._ensure_utils()

        # Reserve an output file
        output_file = tempfile.mkstemp()[1]

        # Template plugin
        plugin_runner = None
        f = open(__dir__ + '/templates/plugin_runner.py')
        runner_template = Template(f.read())
        plugin_runner = runner_template.render(output_file=output_file,
                                               auto_kill_sublime=self.auto_kill_sublime)
        f.close()

        # Output plugin_runner to directory
        f = open(self._plugin_test_dir + '/plugin_runner.py', 'w')
        f.write(plugin_runner)
        f.close()

        # Output test to directory
        f = open(self._plugin_test_dir + '/plugin.py', 'w')
        f.write(test_str)
        f.close()

        # TODO: Run script

        # Wait for the output file to exist
        while (not os.path.exists(output_file) or os.stat(output_file).st_size == 0):
            logger.debug('Waiting for %s to exist / have size' % output_file)
            time.sleep(0.1)

        # TODO: Wait for sublime to close?

        # Read in the output
        with open(output_file) as f:
            # Read, parse, and return the result
            result = f.read()
            result_lines = result.split('\n')
            return {
                'raw_result': result,
                'success': result_lines[0] == 'SUCCESS',
                'meta_info': '\n'.join(result_lines[1:])
            }
