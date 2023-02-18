import os
import sys
import importlib
from qgis.PyQt.QtWidgets import QMessageBox


def check(required_packages):
    # Check if required packages are installed
    missing_packages = []
    for package in required_packages:
        try:
            importlib.import_module(package)
        except ImportError:
            missing_packages.append(package)

    # If any required packages are missing, prompt user to install them
    if missing_packages:
        message = "The following Python packages are required to use the plugin QChatGPT:\n\n"
        message += "\n".join(missing_packages)
        message += "\n\nWould you like to install them now?"

        reply = QMessageBox.question(None, 'Missing Dependencies', message,
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.No:
            return

        for package in missing_packages:
            update = False
            try:
                os.system('"' + os.path.join(sys.prefix, 'scripts', 'pip') + f'" install {package}')
                update = True
            finally:
                if not update:
                    try:
                        importlib.import_module(package)
                        import subprocess
                        subprocess.check_call(['python3', '-m', 'pip', 'install', package])
                    except:
                        importlib.import_module(package)
