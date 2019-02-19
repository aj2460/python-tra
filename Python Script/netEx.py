import sys
#import functions_classes
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.createUI()

def createUI(self):
    self.setWindowTitle('Equipment Manager 0.1')
    self.tabWidget = QTabWidget()
    #New Data
    self.newDataWidget = QWidget()
    self.newDataLayout = QVBoxLayout()
    self.newFormLayout = QFormLayout()
    self.newConfirmButton = QPushButton('Confirm',self)
    self.newDataLayout.addLayout(self.newFormLayout)
    self.newDataLayout.addWidget(self.newConfirmButton)
    self.newDataWidget.setLayout(self.newDataLayout)
    self.tabWidget.addTab(self.newDataWidget, 'New Data')
    #Update Data
    self.updateDataWidget = QWidget()
    self.updateDataLayout = QVBoxLayout()
    self.updateDataWidget.setLayout(self.updateDataLayout)
    self.tabWidget.addTab(self.updateDataWidget, 'Update Data')
    #Query
    self.queryWidget = QWidget()
    self.queryLayout = QVBoxLayout()
    self.queryWidget.setLayout(self.queryLayout)
    self.tabWidget.addTab(self.queryWidget, 'Query')
    #Main Layout
    '''
    self.mainLayout = QVBoxLayout()
    self.mainLayout.addWidget(self.tabWidget)
    self.setLayout(self.mainLayout)

    '''
    self.setCentralWidget(self.tabWidget)


def main():
    mainWindow = MainWindow()
    mainWindow.show()
    mainWindow.raise_()
    application.exec_()