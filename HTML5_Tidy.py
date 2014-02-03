import os
import re
import subprocess
import threading
import sys
import sublime
import sublime_plugin

class html5_tidy(sublime_plugin.TextCommand):
    def run(self, edit):
        # fetch the settings dictionary
        settings = sublime.load_settings('HTML5_Tidy.sublime-settings')

        if self.view.is_dirty():
            if settings.get("save_before_tidy") == True:
                self.view.run_command("save")
                # save the current buffer
        
        # the tidy command
        commandName = settings.get("cmd")
        # things like -m or -indent
        switches = "-"+ ''.join(settings.get('switches'))
        # additional options like --show-only-body 1
        config_options = ' '.join(["--" + key + " " + str(value) for key, value in settings.get('config').items()])
        # the current buffer file name
        fileName = self.view.file_name()

        tidyCommand = " ".join([commandName, switches, config_options, fileName])

        cmd = ShellCommand()
        result = cmd.execute(tidyCommand)

        messages = []

        if settings.get("output_to_console") == True:
            for line in result.splitlines():
                print(line)

# snagged this from PHPcs
class ShellCommand():
    """Base class for shelling out a command to the terminal"""
    def execute(self, cmd):
        data = None

        info = None

        if os.name == 'nt':
            info = subprocess.STARTUPINFO()
            info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            info.wShowWindow = subprocess.SW_HIDE

        home = os.path.expanduser("~")
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, startupinfo=info, cwd=home)

        if proc.stdout:
            data = proc.communicate()[0]

        return data.decode()
