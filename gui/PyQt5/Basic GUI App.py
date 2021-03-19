#!python

# Basic GUI App

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys

def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(1000,1000,1000,1000,) 
    win.setWindowTitle("My first window!") 
    
    label = QLabel(win)
    label.setText("my first label")
    label.move(100, 250)  

    win.show()
    sys.exit(app.exec_())

main()  # make sure to call the function

win.setGeometry(1000,1000,1000,1000,) # sets the windows x, y, width, height
win.setWindowTitle("My first window!")  # setting the window title
	
label = QLabel(win)
label.setText("my first label")
label.move(150, 150)  # x, y from top left hand corner.
# If we want to see the label now we will need to show the window.

jkwin.show()
