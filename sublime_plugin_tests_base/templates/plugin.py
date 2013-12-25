import code
import os
import sublime
import sublime_plugin
import sys
import traceback

# Set up constants
__dir__ = os.path.dirname(os.path.abspath(__file__))


# TODO: Figure out where to put this
class PluginTestsReplaceAllCommand(sublime_plugin.TextCommand):
    def run(self, edit, content=''):
        view = self.view
        view.replace(edit, sublime.Region(0, view.size()), content)


def run():
    # Placeholder for success and error info
    success = True
    err = None

    # Attempt to perform actions and catch *any* exception
    try:
        # DEV: Due to `import` not immediately picking up changes, we use `execfile` to run what is on disk
        filepath = __dir__ + '/plugin_action.py'
        # TODO: Use folder name as namespace, not hard-coded value
        namespace = 'sublime-harness-tmp'
        is_sublime_2k = sublime.version() < '3000'
        plugin_dict = {
            '__dir__': __dir__,
            '__file__': filepath,
            '__name__': 'plugin_action' if is_sublime_2k else '%s.plugin_action' % namespace,
            '__package__': None if is_sublime_2k else namespace,
            '__builtins__': __builtins__,
        }

        # DEV: In Python 2.x, use execfile. In 3.x, use compile + exec.
        # if getattr(__builtins__, 'execfile', None):
        if is_sublime_2k:
            execfile(filepath, plugin_dict, plugin_dict)
        else:
            f = open(filepath)
            script = f.read()
            interpretter = code.InteractiveInterpreter(plugin_dict)
            interpretter.runcode(compile(script, filepath, 'exec'))
        plugin_dict['run']()
    except Exception:
    # If an error occurs, record it
        success = False
        exc_type, exc_value, exc_traceback = sys.exc_info()
        err = ''.join(traceback.format_exception(exc_type,
                                                 exc_value,
                                                 exc_traceback))
    finally:
    # Always...
        # Write out success/failure and any meta data
        output = 'SUCCESS' if success else 'FAILURE'
        if err:
            output += '\n%s' % err
        f = open('{{output_file}}', 'w')
        f.write(output)
        f.close()

        {% if auto_kill_sublime %}
        # Automatically exit out of Sublime
        # DEV: If `sublime_text` is not currently running, then we need to automatically kill the process
        sublime.run_command('exit')
        {% endif %}
