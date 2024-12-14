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

    If the script fails to find the Qt plugin path, make sure your environment variables are set correctly:

    CHECK PATH TO YOUR ANACONDA BEFORE THIS
    
    Find PATH in environment variables and add this lines to start:

       C:\ProgramData\Anaconda3\envs\ann_tool\Lib\site-packages\PyQt5\Qt5\bin
       C:\ProgramData\Anaconda3\envs\ann_tool\Lib\site-packages\PyQt5\Qt5\plugins
       C:\ProgramData\Anaconda3\envs\ann_tool\Lib\site-packages\PyQt5\Qt5\plugins\platforms

    If you already have QT_PLUGIN_PATH add to start:

      C:\ProgramData\Anaconda3\envs\ann_tool\Lib\site-packages\PyQt5\Qt5\plugins
    
    Ensure that PyQt5 is installed properly and that your Python environment is correctly configured.

    how you can set it up if you're using a pure Python installation (without Anaconda):
    
      1. Check if PyQt5 is installed correctly
      
      Run the following command to ensure PyQt5 is installed:
      
      pip show PyQt5
      
      If PyQt5 is not installed, install it using:
      
      pip install PyQt5
      
      2. Find the path to the Qt plugins
      
      To find the plugin path for your PyQt5 installation, you can use the following Python code:

   ```python
   import os
   import sys
   import site
      
   # Print PyQt5 installation path
   pyqt_path = site.getsitepackages()[0]  # Get path to site-packages
   qt_plugins_path = os.path.join(pyqt_path, "PyQt5", "Qt", "plugins", "platforms")

   print(f"Qt plugins path: {qt_plugins_path}")

      Or use ready [code](https://github.com/nazarhktwitch/PyQT5-Path-Finder)


      3. Add the plugin path to the environment variable
      
      Once you have the path to the plugins, you need to add it to the QT_QPA_PLATFORM_PLUGIN_PATH environment variable.
      
      For Windows:
      
          Open Command Prompt.
      
          Run the following command to set the environment variable temporarily:
      
          set QT_QPA_PLATFORM_PLUGIN_PATH=C:\path\to\PyQt5\Qt5\plugins\platforms
      
          Replace C:\path\to\PyQt5\Qt5\plugins\platforms with the path you found in the previous step.
      
      For Linux/macOS:
      
      Run the following command in the terminal:
      
      export QT_QPA_PLATFORM_PLUGIN_PATH=/path/to/PyQt5/Qt5/plugins/platforms
      
      You can also add this line to your configuration file, such as .bashrc or .zshrc, to make it persistent.

      4. Setting the path via Python (if you don’t want to modify environment variables manually)
      
      In your script, you can programmatically set the environment variable before running your application:
      
      import os
      
      qt_plugins_path = "C:\\path\\to\\PyQt5\\Qt5\\plugins\\platforms"  # Set your plugins path
      os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = qt_plugins_path
      
      This can be added at the beginning of your script to automatically set the path when the script runs.

      5. Reinstall PyQt5
      
      If PyQt5 is still not working, try reinstalling it:
      
      pip uninstall PyQt5
      pip install PyQt5
      
      6. Verification
      
      After setting the path, ensure the plugin issue is resolved by running your application. If the plugin path is correctly set, the program should run without any issues.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/nazarhktwitch/PyQT5-Fixer/blob/main/LICENSE) file for details.
