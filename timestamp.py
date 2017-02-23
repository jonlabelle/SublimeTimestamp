from datetime import date, datetime
from re import sub

import sublime
import sublime_plugin


class UtctimestampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view

        timestamp_format = '%Y-%m-%d %H:%M:%S'
        timestamp_str = datetime.utcnow().strftime(timestamp_format)

        for region in view.sel():
            if region.empty():
                view.insert(edit, region.a, timestamp_str)
            else:
                view.replace(edit, region, timestamp_str)

        sublime.set_timeout(lambda: sublime.status_message(
            'UTC Timestamp inserted.'), 0)


class DatestampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view

        date_format = '%B %d, %Y'
        datestamp_str = date.today().strftime(date_format)
        datestamp_str = sub('^0|(?<= )0', '', datestamp_str)

        for region in view.sel():
            if region.empty():
                view.insert(edit, region.a, datestamp_str)
            else:
                view.replace(edit, region, datestamp_str)

        sublime.set_timeout(lambda: sublime.status_message(
            'Datestamp inserted.'), 0)
