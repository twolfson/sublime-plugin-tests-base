import sublime_plugin

with open('/tmp/valid_ready', 'w') as f:
    f.write('OK!')

class SublimePluginTestsBaseValidCommand(sublime_plugin.WindowCommand):
    def run(self):
        with open('/tmp/hi', 'w') as f:
            f.write('Hello World!')
