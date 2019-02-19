#8593 893 211 voda
import sys
import os

from PyQt5.QtWidgets import (QWidget,QApplication,
	QListView,QVBoxLayout)
from PyQt5.QtGui import QStandardItemModel,QStandardItem

class Example(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		lv=QListView()
		lv.setWindowTitle('Directory List')

		model=QStandardItemModel(lv)

		for i in os.listdir():
			item=QStandardItem(i)
			item.setCheckable(True)
			model.appendRow(item)
		lv.setModel(model)


		vbox=QVBoxLayout()
		vbox.addWidget(lv)

		self.setLayout(vbox)

		self.setGeometry(300,300,250,450)
		self.setWindowTitle('List View')
		self.show()
if __name__ == '__main__':
	app=QApplication(sys.argv)
	ex=Example()
	sys.exit(app.exec_())