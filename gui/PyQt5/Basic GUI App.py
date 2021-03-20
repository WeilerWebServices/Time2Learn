#!python

# Basic GUI App

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys

def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,300,300) 
    win.setWindowTitle("My first window!") 
    
    label = QLabel(win)
    label.setText("my first label")
    label.move(50, 50)  

    win.show()
    sys.exit(app.exec_())

main()  # make sure to call the function

win.setGeometry(200,200,300,300) # sets the windows x, y, width, height
win.setWindowTitle("My first window!")  # setting the window title
	
label = QLabel(win)
label.setText("my first label")
label.move(50, 50)  # x, y from top left hand corner.
# If we want to see the label now we will need to show the window.

win.show()
