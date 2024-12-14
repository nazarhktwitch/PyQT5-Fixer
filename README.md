# PyQt5-Fixer

A Python script to help fix issues with PyQt5 and its Qt platform plugins, designed for both Windows and Linux users. This script checks the PyQt5 installation, sets the correct Qt plugin paths, and can reinstall necessary packages.

## Features

- Fix PyQt5 installation issues.
- Set Qt platform plugin paths automatically.
- Reinstall PyQt5 and related packages (`qtwidgets`).
- Displays helpful guide and instructions.

## Requirements

- Python 3.x
- `pip` (Python package manager)
- `subprocess`, `os`, `argparse`, `logging` (standard Python libraries)
- `tqdm`

## Installation

1. Clone this repository or download the script file.
   
   ```bash
   git clone https://github.com/yourusername/PyQt5-Fixer.git
   cd PyQt5-Fixer

    Make sure you have Python and pip installed. If not, install them.

    Install any necessary dependencies (if applicable).

    pip install -r requirements.txt

    Or manually:

    pip install tqdm>=4.67.1


## Usage

You can run the script with the following options:

### Fix PyQt5 (Windows)

To fix PyQt5 on Windows (set Qt plugin paths and reinstall packages):

python pyqt5_fixer.py --fix

### Fix PyQt5 (Linux)

To fix PyQt5 on Linux (set Qt plugin paths and reinstall packages):

python pyqt5_fixer.py --fix_linux

## Display Guide

If you are unsure about the process, you can display the guide with instructions:

python pyqt5_fixer.py --guide

## How It Works

    Fixing PyQt5 on Windows (--fix):
        Checks for PyQt5 installation.
        Sets the correct Qt plugin path for Windows.
        If the installation is incorrect, it will reinstall PyQt5 and qtwidgets.

    Fixing PyQt5 on Linux (--fix_linux):
        Checks for PyQt5 installation.
        Sets the correct Qt plugin path for Linux.
        If the installation is incorrect, it will reinstall PyQt5 and qtwidgets.

    Guide (--guide):
        Displays detailed instructions for fixing common PyQt5 issues.

## Logs

All actions are logged in a log file stored in the logs folder. The log file is named PyQT5-Fixer_log_YYYY-MM-DD_HH-MM.txt for easy tracking.

Example log output:

[Progress] Log file created: logs/PyQT5-Fixer_log_2024-12-14_17-10.txt

[Progress] Starting PyQt5 fix...

[Progress] Checking PyQt5 installation...

[Error] Qt plugin path not found.

[Progress] Adding Qt plugin path to environment variables...

[Progress] PyQt5 has been fixed successfully!

## Troubleshooting

    If the script fails to find the Qt plugin path, make sure your environment variables are set correctly.
    Ensure that PyQt5 is installed properly and that your Python environment is correctly configured.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/nazarhktwitch/PyQT5-Fixer/blob/main/LICENSE) file for details.
