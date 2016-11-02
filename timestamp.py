import datetime
import sublime
import sublime_plugin


class UtctimestampCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        timestamp_format = '%Y-%m-%d %H:%M:%S'
        timestamp_str = datetime.datetime.utcnow().strftime(timestamp_format)

        for region in self.view.sel():
            if region.empty():
                self.view.insert(edit, region.a, timestamp_str)
            else:
                self.view.replace(edit, region, timestamp_str)

        sublime.set_timeout(lambda: sublime.status_message(
            'UTC Timestamp inserted.'), 0)


class DatestampCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        date_format = '%B %-d, %Y'
        datestamp_str = datetime.date.today().strftime(date_format)

        for region in self.view.sel():
            if region.empty():
                self.view.insert(edit, region.a, datestamp_str)
            else:
                self.view.replace(edit, region, datestamp_str)

        sublime.set_timeout(
            lambda: sublime.status_message('Datestamp inserted.'), 0)
