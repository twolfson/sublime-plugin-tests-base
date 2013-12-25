import sublime_plugin


class SublimePluginTestsBaseValidCommand(sublime_plugin.WindowCommand):
    def run(self):
        with open('/tmp/hi', 'w') as f:
            f.write('Hello World!')
