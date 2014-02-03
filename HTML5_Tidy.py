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

        if self.view.is_dirty() and settings.get("save_before_tidy") == True:
            # save the current buffer
            self.view.run_command("save")
        
        # the tidy command
        command_name = settings.get("cmd")
        # things like -m or -indent
        switches = "-"+ ''.join(settings.get('switches'))
        # additional options like --show-only-body 1
        config_options = ' '.join(["--" + key + " " + str(value) for key, value in settings.get('config').items()])
        # the current buffer file name
        file_name = self.view.file_name()

        tidy_command = " ".join([command_name, switches, config_options, file_name])

        cmd = ShellCommand()
        result = cmd.execute(tidy_command)

        if settings.get("output_to_console") == True:
            for line in result.splitlines():
                print(line)

# snagged this from PHPcs plugin
class ShellCommand():
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
