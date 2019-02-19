import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon 


class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(300,200,300,600)
		self.setWindowTitle('Icon')
		self.setWindowIcon(QIcon('pyqt.png'))

		self.show()





if __name__=='__main__':
	app=QApplication(sys.argv)
	ex=Example()

	sys.exit(app.exec_())
