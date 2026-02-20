import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
import sys
import time
def window():
    app = QApplication(sys.argv)
    win = QWidget()
    win.setWindowTitle("PyQt5 App")
    win.setGeometry(100, 100, 300, 200)
    
    button1 = QPushButton("Click Me")
    if button1.clicked.connect(lambda: print("Button Clicked!")):
        label = QtWidgets.QLabel("Button was clicked!", win)
    win.show()
    time.sleep(5)
    sys.exit(app.exec_())
window()