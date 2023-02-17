import os, sys, importlib
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
        message = "The following Python packages are required to use this plugin:\n\n"
        message += "\n".join(missing_packages)
        message += "\n\nWould you like to install them now?"    

        reply = QMessageBox.question(None, 'Missing Dependencies', message,
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)  

        if reply == QMessageBox.No:
            return

        for package in missing_packages:
            os.system('"' + os.path.join(sys.prefix, 'scripts', 'pip.exe') + '" install openai')