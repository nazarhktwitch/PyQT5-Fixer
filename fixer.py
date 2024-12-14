import os
import sys
import subprocess
import logging
from datetime import datetime
import time
import argparse

# Функция для установки зависимостей через pip
def install_pypi_package(package_name):
    """Installs a package using pip."""
    log_progress(f"Installing package: {package_name}")
    
    # Показ прогресса установки пакета
    progress_bar(0, 100, f"Installing {package_name}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
    progress_bar(100, 100, f"Installing {package_name}... Done.")

# Функция для установки переменной окружения для плагинов Qt (Windows)
def set_qt_plugin_path_windows():
    """Sets the environment variable for Qt plugins (Windows)."""
    qt_plugins_path = os.path.join(
        sys.prefix, "Lib", "site-packages", "PyQt5", "Qt", "plugins", "platforms"
    )
    if os.path.exists(qt_plugins_path):
        os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = qt_plugins_path
        log_progress("Adding Qt plugin path to environment variables...")
        return True
    else:
        log_error("Qt plugin path not found.")
        return False

# Функция для установки переменной окружения для плагинов Qt (Linux)
def set_qt_plugin_path_linux():
    """Sets the environment variable for Qt plugins (Linux)."""
    qt_plugins_path = os.path.join(
        sys.prefix, "lib", "python" + sys.version[:3], "site-packages", "PyQt5", "Qt", "plugins", "platforms"
    )
    if os.path.exists(qt_plugins_path):
        os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = qt_plugins_path
        log_progress("Adding Qt plugin path to environment variables...")
        return True
    else:
        log_error("Qt plugin path not found.")
        return False

# Функция для переустановки PyQt5
def reinstall_pqt5():
    """Reinstalls PyQt5 to fix plugin-related issues."""
    log_progress("Uninstalling PyQt5...")
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", "PyQt5"])
    log_progress("Reinstalling PyQt5...")
    install_pypi_package("PyQt5")
    
    log_progress("Uninstalling qtwidgets...")
    subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", "qtwidgets"])
    log_progress("Reinstalling qtwidgets...")
    install_pypi_package("qtwidgets")

# Функция для создания логов
def create_log():
    """Creates a log file in the logs directory."""
    script_dir = os.path.dirname(os.path.realpath(__file__))  # Get the directory of the script
    logs_dir = os.path.join(script_dir, "logs")  # Path to logs directory
    
    # Создаем папку logs, если она не существует
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    log_filename = f"PyQT5-Fixer_log_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.txt"
    log_filepath = os.path.join(logs_dir, log_filename)

    logging.basicConfig(filename=log_filepath, level=logging.INFO, format='%(asctime)s - %(message)s')
    return log_filepath

# Функция для записи прогресса в лог
def log_progress(message):
    """Logs the progress of the actions."""
    print(f"[Progress] {message}")
    logging.info(message)

# Функция для записи ошибок в лог
def log_error(message):
    """Logs errors."""
    print(f"[Error] {message}")
    logging.error(message)

# Функция для вывода прогресс-бара
def progress_bar(current, total, message):
    """Displays a progress bar in the terminal."""
    bar_length = 40
    progress = current / total
    arrow = '=' * int(progress * bar_length)
    spaces = ' ' * (bar_length - len(arrow))
    percent = int(progress * 100)
    
    sys.stdout.write(f"\r[{arrow}{spaces}] {percent}% - {message}")
    sys.stdout.flush()

    if current == total:
        print()

# Основная функция для починки PyQt5 (Windows)
def fix_pqt5_windows():
    """Fixes PyQt5 issues on Windows."""
    log_progress("Checking PyQt5 installation...")
    if not os.path.exists(os.path.join(sys.prefix, "Lib", "site-packages", "PyQt5")):
        install_pypi_package("PyQt5")
        install_pypy_package("qtwidgets")

    if not set_qt_plugin_path_windows():
        log_error("Failed to set Qt plugin path.")
        return

    try:
        subprocess.check_call([sys.executable, "-m", "pip", "show", "PyQt5"])
        log_progress("PyQt5 is installed correctly.")
    except subprocess.CalledProcessError:
        reinstall_pqt5()

    log_progress("PyQt5 has been fixed successfully!")

# Основная функция для починки PyQt5 (Linux)
def fix_pqt5_linux():
    """Fixes PyQt5 issues on Linux."""
    log_progress("Checking PyQt5 installation...")
    if not os.path.exists(os.path.join(sys.prefix, "lib", "python" + sys.version[:3], "site-packages", "PyQt5")):
        install_pypi_package("PyQt5")
        install_pypy_package("qtwidgets")

    if not set_qt_plugin_path_linux():
        log_error("Failed to set Qt plugin path.")
        return

    try:
        subprocess.check_call([sys.executable, "-m", "pip", "show", "PyQt5"])
        log_progress("PyQt5 is installed correctly.")
    except subprocess.CalledProcessError:
        reinstall_pqt5()

    log_progress("PyQt5 has been fixed successfully!")

# Функция для отображения гайда
def show_guide():
    """Displays the guide with instructions."""
    guide_text = """
    1. If you encounter an error with the Qt platform plugin (e.g., "Could not find the Qt platform plugin 'windows'"),
       use the "Fix PyQt5" option.
    2. The script will check for PyQt5 and configure the correct plugin path.
    3. If the issue persists, PyQt5 will be reinstalled.
    4. For more detailed instructions, check this guide.
    """
    print(guide_text)
    log_progress("Displayed guide to user.")

# Основная функция для обработки аргументов командной строки
def main():
    parser = argparse.ArgumentParser(description="PyQt5 Fixer Script")
    parser.add_argument('--fix', action='store_true', help='Fix PyQt5 on Windows')
    parser.add_argument('--fix_linux', action='store_true', help='Fix PyQt5 on Linux')
    parser.add_argument('--guide', action='store_true', help='Display the guide for PyQt5 fixing')

    args = parser.parse_args()

    log_filepath = create_log()  # Create a log file in the logs directory
    log_progress(f"Log file created: {log_filepath}")

    if args.guide:
        show_guide()
        return

    if args.fix:
        log_progress("Starting PyQt5 fix for Windows...")
        fix_pqt5_windows()
    elif args.fix_linux:
        log_progress("Starting PyQt5 fix for Linux...")
        fix_pqt5_linux()
    else:
        log_error("No valid option selected. Use --fix for Windows or --fix_linux for Linux.")

if __name__ == "__main__":
    main()