# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import random


class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("calculator game for kids")
		self.setGeometry(0, 0, 600, 400)
		self.UiComponents()
		self.show()

	def UiComponents(self):

		self.title = QLabel('Calculator game for kids', self)
		self.title.setGeometry(250,10,1000,20)
		
		self.n1 = QLabel(' ',self)
		self.n1.setGeometry(250,30,1000,20)
		self.n2 = QLabel(' ',self)
		self.n2.setGeometry(275,30,1000,20)
		self.n3 = QLabel(' ',self)
		self.n3.setGeometry(300,30,1000,20)
		self.n4 = QLabel(' ',self)
		self.n4.setGeometry(325,30,1000,20)
		self.n5 = QLineEdit(self)
		self.n5.setGeometry(350,30,50,20)

		self.btn1 = QPushButton("start / next",self)
		self.btn1.setGeometry(207,50,200,50)
		self.btn1.clicked.connect(self.start)
		self.btn2 = QPushButton("check",self)
		self.btn2.setGeometry(207,110,200,50)
		self.btn2.clicked.connect(self.test)

	def start(self):
		x = random.randint(0,100)
		y = random.randint(0,100)

		self.n1.setText(str(x))
		self.n3.setText(str(y))
		self.n2.setText('+')
		self.n4.setText('=')
	def test(self):
		#find a way to link var in def start to test
		print("test")

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
