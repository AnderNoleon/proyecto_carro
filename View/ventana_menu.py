import sys
import os
from datetime import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5 import uic, QtCore, QtWidgets


class Main_window(QMainWindow):
    def __init__(self) -> None:
        super(Main_window, self).__init__()
        uic.loadUi("View/programa.ui", self)


