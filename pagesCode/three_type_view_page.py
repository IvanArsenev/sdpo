from PyQt6 import QtCore, QtGui, QtWidgets

class type_view_page(object):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(800, 480)
		Form.setMinimumSize(QtCore.QSize(800, 480))
		Form.setMaximumSize(QtCore.QSize(800, 480))
		self.text = QtWidgets.QLabel(parent=Form)
		self.text.setGeometry(QtCore.QRect(30, 30, 201, 41))
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
		self.text2 = QtWidgets.QLabel(parent=Form)
		self.text2.setGeometry(QtCore.QRect(30, 77, 491, 31))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(13)
		self.text2.setFont(font)
		self.text2.setStyleSheet("color: #8D8D8D;")
		self.text2.setObjectName("text2")
		self.step_text = QtWidgets.QLabel(parent=Form)
		self.step_text.setGeometry(QtCore.QRect(695, 30, 61, 31))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(28)
		self.step_text.setFont(font)
		self.step_text.setStyleSheet("color: #A6111B")
		self.step_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
		self.step_text.setObjectName("step_text")
		self.background = QtWidgets.QGraphicsView(parent=Form)
		self.background.setGeometry(QtCore.QRect(0, 0, 800, 480))
		self.background.setStyleSheet("border: 0;")
		self.background.setObjectName("background")
		self.before_day_button = QtWidgets.QPushButton(parent=Form)
		self.before_day_button.setGeometry(QtCore.QRect(30, 145, 362, 87))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(16)
		font.setBold(False)
		font.setWeight(50)
		self.before_day_button.setFont(font)
		self.before_day_button.setStyleSheet("border-radius: 16;\nbackground-color: rgb(228, 228, 228)")
		self.before_day_button.setObjectName("before_day_button")
		self.back_button = QtWidgets.QPushButton(parent=Form)
		self.back_button.setGeometry(QtCore.QRect(303, 384, 193, 66))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(16)
		self.back_button.setFont(font)
		self.back_button.setStyleSheet("color: #A6111B;\nbackground: #FFE0E3;\nborder-radius: 16px;")
		self.back_button.setObjectName("back_button")
		self.after_day_button = QtWidgets.QPushButton(parent=Form)
		self.after_day_button.setGeometry(QtCore.QRect(408, 145, 362, 87))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(16)
		font.setBold(False)
		font.setWeight(50)
		self.after_day_button.setFont(font)
		self.after_day_button.setStyleSheet("border-radius: 16;\nbackground-color: rgb(228, 228, 228)")
		self.after_day_button.setObjectName("after_day_button")
		self.before_raid_button = QtWidgets.QPushButton(parent=Form)
		self.before_raid_button.setGeometry(QtCore.QRect(30, 248, 362, 87))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(16)
		font.setBold(False)
		font.setWeight(50)
		self.before_raid_button.setFont(font)
		self.before_raid_button.setStyleSheet("border-radius: 16;\nbackground-color: rgb(228, 228, 228)")
		self.before_raid_button.setObjectName("before_raid_button")
		self.after_raid_button = QtWidgets.QPushButton(parent=Form)
		self.after_raid_button.setGeometry(QtCore.QRect(408, 248, 362, 87))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(16)
		font.setBold(False)
		font.setWeight(50)
		self.after_raid_button.setFont(font)
		self.after_raid_button.setStyleSheet("border-radius: 16;\nbackground-color: rgb(228, 228, 228)")
		self.after_raid_button.setObjectName("after_raid_button")
		self.background.raise_()
		self.text.raise_()
		self.text2.raise_()
		self.step_text.raise_()
		self.before_day_button.raise_()
		self.back_button.raise_()
		self.after_day_button.raise_()
		self.before_raid_button.raise_()
		self.after_raid_button.raise_()

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
		self.text.setText(_translate("Form", "Тип осмотра"))
		self.text2.setText(_translate("Form", "Выберите тип осмотра, который вам необходимо пройти"))
		self.step_text.setText(_translate("Form", "1/5"))
		self.before_day_button.setText(_translate("Form", "Предсменный "))
		self.back_button.setText(_translate("Form", "Назад"))
		self.after_day_button.setText(_translate("Form", "Послесменный"))
		self.before_raid_button.setText(_translate("Form", "Предрейсовый"))
		self.after_raid_button.setText(_translate("Form", "Послерейсовый "))