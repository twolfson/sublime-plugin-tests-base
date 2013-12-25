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
    def __init__(self, auto_kill_sublime=False):
        self.auto_kill_sublime = auto_kill_sublime
        self.harness = Harness()

    @property
    def directory(self):
        return self.harness.directory

    def _ensure_directory(self):
        # If the plugin test directory does not exist, create it
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def _ensure_utils(self):
        # Ensure the plugin test directory exists
        self._ensure_directory()

        # TODO: Use similar copy model minus the exception
        # TODO: If we overwrite utils, be sure to wait so that changes for import get picked up
        if not os.path.exists(self.directory + '/utils'):
            shutil.copytree(__dir__ + '/utils', self.directory + '/utils')

    def run_test(self, action_str):
        # Guarantee there is an output directory and launcher
        self._ensure_utils()

        # Reserve an output file
        output_file = tempfile.mkstemp()[1]

        # Template plugin
        f = open(__dir__ + '/templates/plugin.py')
        runner_template = Template(f.read())
        plugin_runner = runner_template.render(output_file=output_file,
                                               auto_kill_sublime=self.auto_kill_sublime)
        f.close()

        # Output test to directory
        f = open(self.directory + '/plugin_action.py', 'w')
        f.write(action_str)
        f.close()

        # Run script
        self.harness.run(plugin_runner)

        # Wait for the output file to exist
        # TODO: Introduce timeout
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
