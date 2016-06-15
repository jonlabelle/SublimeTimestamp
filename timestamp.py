import datetime
import sublime
import sublime_plugin


class TimestampCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        timestamp_format = 'UTC %Y-%m-%d %H:%M:%S'
        timestamp_str = datetime.datetime.utcnow().strftime(timestamp_format)

        for region in self.view.sel():
            if region.empty():
                self.view.insert(edit, region.a, timestamp_str)
            else:
                self.view.replace(edit, region, timestamp_str)

        sublime.set_timeout(
            lambda: sublime.status_message('UTC Timestamp inserted.'), 0)
