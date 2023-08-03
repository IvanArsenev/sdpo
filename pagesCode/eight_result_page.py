from PyQt6 import QtCore, QtGui, QtWidgets

class result_page(object):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(800, 480)
		Form.setMinimumSize(QtCore.QSize(800, 480))
		Form.setMaximumSize(QtCore.QSize(800, 480))
		self.background = QtWidgets.QGraphicsView(parent=Form)
		self.background.setGeometry(QtCore.QRect(0, 0, 800, 480))
		self.background.setStyleSheet("border: 0;")
		self.background.setObjectName("background")
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
		self.text2 = QtWidgets.QLabel(parent=Form)
		self.text2.setGeometry(QtCore.QRect(30, 77, 721, 31))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(13)
		self.text2.setFont(font)
		self.text2.setStyleSheet("color: #8D8D8D;")
		self.text2.setObjectName("text2")
		self.view_type_text = QtWidgets.QLabel(parent=Form)
		self.view_type_text.setGeometry(QtCore.QRect(30, 127, 111, 31))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(13)
		self.view_type_text.setFont(font)
		self.view_type_text.setStyleSheet("color: #8D8D8D;")
		self.view_type_text.setObjectName("view_type_text")
		self.report_heal_text = QtWidgets.QLabel(parent=Form)
		self.report_heal_text.setGeometry(QtCore.QRect(30, 161, 181, 31))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(13)
		self.report_heal_text.setFont(font)
		self.report_heal_text.setStyleSheet("color: #8D8D8D;")
		self.report_heal_text.setObjectName("report_heal_text")
		self.alcohol_text = QtWidgets.QLabel(parent=Form)
		self.alcohol_text.setGeometry(QtCore.QRect(30, 195, 231, 31))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(13)
		self.alcohol_text.setFont(font)
		self.alcohol_text.setStyleSheet("color: #8D8D8D;")
		self.alcohol_text.setObjectName("alcohol_text")
		self.s_pressure_text = QtWidgets.QLabel(parent=Form)
		self.s_pressure_text.setGeometry(QtCore.QRect(30, 229, 221, 31))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(13)
		self.s_pressure_text.setFont(font)
		self.s_pressure_text.setStyleSheet("color: #8D8D8D;")
		self.s_pressure_text.setObjectName("s_pressure_text")
		self.d_pressure_text = QtWidgets.QLabel(parent=Form)
		self.d_pressure_text.setGeometry(QtCore.QRect(30, 263, 231, 31))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(13)
		self.d_pressure_text.setFont(font)
		self.d_pressure_text.setStyleSheet("color: #8D8D8D;")
		self.d_pressure_text.setObjectName("d_pressure_text")
		self.pulse_text = QtWidgets.QLabel(parent=Form)
		self.pulse_text.setGeometry(QtCore.QRect(30, 297, 61, 31))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(13)
		self.pulse_text.setFont(font)
		self.pulse_text.setStyleSheet("color: #8D8D8D;")
		self.pulse_text.setObjectName("pulse_text")
		self.temperature_text = QtWidgets.QLabel(parent=Form)
		self.temperature_text.setGeometry(QtCore.QRect(30, 331, 161, 31))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(13)
		self.temperature_text.setFont(font)
		self.temperature_text.setStyleSheet("color: #8D8D8D;")
		self.temperature_text.setObjectName("temperature_text")
		self.view_type_input = QtWidgets.QLabel(parent=Form)
		self.view_type_input.setGeometry(QtCore.QRect(620, 127, 151, 31))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(13)
		self.view_type_input.setFont(font)
		self.view_type_input.setStyleSheet("color: #2E2E2E")
		self.view_type_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
		self.view_type_input.setObjectName("view_type_input")
		self.reports_heal_input = QtWidgets.QLabel(parent=Form)
		self.reports_heal_input.setGeometry(QtCore.QRect(620, 161, 151, 31))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(13)
		self.reports_heal_input.setFont(font)
		self.reports_heal_input.setStyleSheet("color: #49C21E")
		self.reports_heal_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
		self.reports_heal_input.setObjectName("reports_heal_input")
		self.alcho = QtWidgets.QLabel(parent=Form)
		self.alcho.setGeometry(QtCore.QRect(620, 195, 151, 31))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(13)
		self.alcho.setFont(font)
		self.alcho.setStyleSheet("color: #49C21E")
		self.alcho.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
		self.alcho.setObjectName("alcho")
		self.s_pressure_input = QtWidgets.QLabel(parent=Form)
		self.s_pressure_input.setGeometry(QtCore.QRect(620, 229, 151, 31))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(13)
		self.s_pressure_input.setFont(font)
		self.s_pressure_input.setStyleSheet("color: #49C21E")
		self.s_pressure_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
		self.s_pressure_input.setObjectName("s_pressure_input")
		self.d_pressure_input = QtWidgets.QLabel(parent=Form)
		self.d_pressure_input.setGeometry(QtCore.QRect(620, 263, 151, 31))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(13)
		self.d_pressure_input.setFont(font)
		self.d_pressure_input.setStyleSheet("color: #49C21E")
		self.d_pressure_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
		self.d_pressure_input.setObjectName("d_pressure_input")
		self.pulse_input = QtWidgets.QLabel(parent=Form)
		self.pulse_input.setGeometry(QtCore.QRect(620, 297, 151, 31))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(13)
		self.pulse_input.setFont(font)
		self.pulse_input.setStyleSheet("color: #49C21E")
		self.pulse_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
		self.pulse_input.setObjectName("pulse_input")
		self.temperature_input = QtWidgets.QLabel(parent=Form)
		self.temperature_input.setGeometry(QtCore.QRect(620, 331, 151, 31))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(13)
		self.temperature_input.setFont(font)
		self.temperature_input.setStyleSheet("color: #49C21E")
		self.temperature_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
		self.temperature_input.setObjectName("temperature_input")
		self.decline_button = QtWidgets.QPushButton(parent=Form)
		self.decline_button.setGeometry(QtCore.QRect(65, 381, 243, 66))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(16)
		self.decline_button.setFont(font)
		self.decline_button.setStyleSheet("color: #A6111B;\nbackground: #FFE0E3;\nborder-radius: 16px;")
		self.decline_button.setObjectName("decline_button")
		self.accept_button = QtWidgets.QPushButton(parent=Form)
		self.accept_button.setGeometry(QtCore.QRect(487, 381, 243, 66))
		font = QtGui.QFont()
		font.setFamily("Inter")
		font.setPointSize(16)
		font.setBold(False)
		font.setWeight(50)
		self.accept_button.setFont(font)
		self.accept_button.setStyleSheet("border-radius: 16;\nbackground-color:#A6111B;\ncolor: white;")
		self.accept_button.setObjectName("accept_button")

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
		self.text.setText(_translate("Form", "Подтверждение результатов"))
		self.text2.setText(_translate("Form", "Подтвердите результаты, полученные в ходе прохождения медицинского осмотра"))
		self.view_type_text.setText(_translate("Form", "Тип осмотра"))
		self.report_heal_text.setText(_translate("Form", "Жалобы на здоровье"))
		self.alcohol_text.setText(_translate("Form", "Уровень алкоголя в крови"))
		self.s_pressure_text.setText(_translate("Form", "Систолическое давление"))
		self.d_pressure_text.setText(_translate("Form", "Диастолическое давление"))
		self.pulse_text.setText(_translate("Form", "Пульс"))
		self.temperature_text.setText(_translate("Form", "Температура тела"))
		self.view_type_input.setText(_translate("Form", "Предсменный"))
		self.reports_heal_input.setText(_translate("Form", "Нет"))
		self.alcho.setText(_translate("Form", "0,2 ‰"))
		self.s_pressure_input.setText(_translate("Form", "117 мм рт. ст."))
		self.d_pressure_input.setText(_translate("Form", "85 мм рт. ст."))
		self.pulse_input.setText(_translate("Form", "75 уд/мин"))
		self.temperature_input.setText(_translate("Form", "36,5 C°"))
		self.decline_button.setText(_translate("Form", "Нет"))
		self.accept_button.setText(_translate("Form", "Подписать"))