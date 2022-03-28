import os
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow

from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 

import sys

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    app = appctxt.app
    app.setQuitOnLastWindowClosed(False)
  
    # Adding an icon
    icon = QIcon( os.path.dirname(__file__) + "/../icons/base/32.png")
    
    # Adding item on the menu bar
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)
    
    # Creating the options
    menu = QMenu()
    option1 = QAction("Geeks for Geeks")
    option2 = QAction("GFG")
    menu.addAction(option1)
    menu.addAction(option2)
    
    # To quit the app
    quit = QAction("Quit")
    quit.triggered.connect(app.quit)
    menu.addAction(quit)
    
    # Adding options to the System Tray
    tray.setContextMenu(menu)
    #window = QMainWindow()
    #window.resize(250, 150)
    #window.show()

    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)