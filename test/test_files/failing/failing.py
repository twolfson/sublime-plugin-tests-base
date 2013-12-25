import sublime_plugin

with open('/tmp/failing_ready', 'w') as f:
    f.write('OK!')

class SublimePluginTestsBaseFailingCommand(sublime_plugin.WindowCommand):
    def run(self):
        raise Exception('Fail whale')
