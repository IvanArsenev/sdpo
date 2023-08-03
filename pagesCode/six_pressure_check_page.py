from PyQt6 import QtCore, QtGui, QtWidgets

class pressure_check_page(object):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(800, 480)
		Form.setMinimumSize(QtCore.QSize(800, 480))
		Form.setMaximumSize(QtCore.QSize(800, 480))
		self.background = QtWidgets.QGraphicsView(parent=Form)
		self.background.setGeometry(QtCore.QRect(0, 0, 800, 480))
		self.background.setStyleSheet("border: 0;")
		self.background.setObjectName("background")
		self.step_text = QtWidgets.QLabel(parent=Form)
		self.step_text.setGeometry(QtCore.QRect(688, 30, 61, 31))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(28)
		self.step_text.setFont(font)
		self.step_text.setStyleSheet("color: #A6111B")
		self.step_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
		self.step_text.setObjectName("step_text")
		self.text2 = QtWidgets.QLabel(parent=Form)
		self.text2.setGeometry(QtCore.QRect(124, 320, 551, 101))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(16)
		self.text2.setFont(font)
		self.text2.setStyleSheet("color: #4D4D4D")
		self.text2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
		self.text2.setObjectName("text2")
		self.text = QtWidgets.QLabel(parent=Form)
		self.text.setGeometry(QtCore.QRect(30, 30, 491, 41))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(24)
		self.text.setFont(font)
		self.text.setStyleSheet("")
		self.text.setLineWidth(0)
		self.text.setMidLineWidth(0)
		self.text.setTextFormat(QtCore.Qt.TextFormat.AutoText)
		self.text.setIndent(-1)
		self.text.setObjectName("text")
		self.image = QtWidgets.QPushButton(parent=Form)
		self.image.setGeometry(QtCore.QRect(324, 140, 151, 141))
		font = QtGui.QFont()
		font.setPointSize(40)
		self.image.setFont(font)
		self.image.setStyleSheet("background-color: white;\nborder: 0;")
		self.image.setText("")
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("D:/Work/SDPO/design/img/davl.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
		self.image.setIcon(icon)
		self.image.setIconSize(QtCore.QSize(150, 200))
		self.image.setObjectName("image")

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
		self.step_text.setText(_translate("Form", "4/5"))
		self.text2.setText(_translate("Form", "Наденьте манжету стрелочкой вверх, сядьте ровно,\nнажмите кнопку СТАРТ.\n\nНе разговаривайте и не двигайтесь при замере."))
		self.text.setText(_translate("Form", "Измерение давления и пульса"))
