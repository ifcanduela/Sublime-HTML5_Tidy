# HTML5 Tidy

A quick-and-dirty **Sublime Text 3** plugin to run HTML5 Tidy on a file.

## Installation

1. *Git*: Clone the repo into your packages folder
2. *Archive*: copy the downloaded file into you packages folder, changing the extension to `.sublime-package`

## Configuration

The config file has three keys to configure Tidy:

- `cmd`: The name of the command to execute. Usually just `tidy`, if it's present in the `PATH`.
- `switches`: List of command switches. `['m', 'q']` is translated to `-mq` (or `-m -q`)
- `settings`: Set any tidy config settings here. Use `0` and `1` for boolean values and strings for the rest.

The plugin has only a few configuration settings:


- `output_to_console`: The output of the Tidy command will be printed to the Sublime console.
- `save_before_tidy`: Force the current buffer to be saved to disk before running Tidy on it.