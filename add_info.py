import datetime
import sublime, sublime_plugin

class AddPythonHeaderCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet",
             {
               "contents":
                "# Copyright (C) 2016-2017 ISCAS""\n"
                "# Author:      Frank""\n"
                "# DateTime:    "  "%s"  %datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +"\n"
                "# Contact: zhaoyyuu@gmail.com""\n"
                "# Description: ${1:Description}""\n"
            }
        )

class AddPhpHeaderCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet",
            {
               "contents":"/**""\n"
                "* Copyright (C) 2016-2017 ISCAS""\n"
                "* Author:      Frank""\n"
                "* DateTime:    "  "%s"  %datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +"\n"
                "* Contact: zhaoyyuu@gmail.com""\n"
                "* Description: ${1:Description}""\n"
                "**/""\n"
            }
        )


