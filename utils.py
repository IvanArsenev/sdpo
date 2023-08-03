from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QIcon, QPixmap
from PIL import ImageQt, Image

from PyQt6.QtCore import QCoreApplication

from crm.normal_result import get_normal_results
from crm.get_user import get_user_login, get_user_number
from crm.send_med import send_med_to_crm, send_car_to_crm

from modules.temperature import temperature_detecter
from modules.alcohol import alcohol_detecter
from modules.pressure import pressure_detecter
from modules.card import add_card
from modules.camera import make_photo
from modules.audio import play_m
from modules.printer import print_qr
from modules.get_car_list import get_cars
from modules.get_car_photo_one import get_photo_one
from modules.get_car_photo_two import get_photo_two

minTemp, maxTemp = get_normal_results()[0], get_normal_results()[1]
maxAlco = get_normal_results()[2]
minSisPl, maxSisPl = get_normal_results()[3], get_normal_results()[4]
minDiaPl, maxDiaPl = get_normal_results()[5], get_normal_results()[6]
minPulse, maxPulse = get_normal_results()[7], get_normal_results()[8]

class Utils():

	def __init__(self):
		self.choosen_car = 0
		self.request = 0
		self.medType = ''
		self.healReport = 'Нет'
		self.alcoDes = ''
		self.pressureDesFrs = ''
		self.pressureDesSec = ''
		self.tempDes = ''
		self.plsDes = ''
		self.base = []
		self.cars_base = []
		self.cars_base_count = 0
		self.car_name_data = ''
		self.car_num_data = ''
		self.car_colors_data = ''
		self.car_counts_data = ''
		self.med_data = []
		self.car_page = 0

	def qt_init(self, qt_self, *args, **kwargs):
		self.qt_self = qt_self
	
	# ============================================================================================================================================================================	
	# 									░█████╗░██╗░░░██╗████████╗██╗░░██╗░█████╗░██████╗░██╗███████╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
	# 									██╔══██╗██║░░░██║╚══██╔══╝██║░░██║██╔══██╗██╔══██╗██║╚════██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
	# 									███████║██║░░░██║░░░██║░░░███████║██║░░██║██████╔╝██║░░███╔═╝███████║░░░██║░░░██║██║░░██║██╔██╗██║
	# 									██╔══██║██║░░░██║░░░██║░░░██╔══██║██║░░██║██╔══██╗██║██╔══╝░░██╔══██║░░░██║░░░██║██║░░██║██║╚████║
	# 									██║░░██║╚██████╔╝░░░██║░░░██║░░██║╚█████╔╝██║░░██║██║███████╗██║░░██║░░░██║░░░██║╚█████╔╝██║░╚███║
	# 									╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝
	# 																		██████╗░░█████╗░░██████╗░███████╗
	# 																		██╔══██╗██╔══██╗██╔════╝░██╔════╝
	# 																		██████╔╝███████║██║░░██╗░█████╗░░
	# 																		██╔═══╝░██╔══██║██║░░╚██╗██╔══╝░░
	# 																		██║░░░░░██║░░██║╚██████╔╝███████╗
	# 																		╚═╝░░░░░╚═╝░░╚═╝░╚═════╝░╚══════╝
	# ============================================================================================================================================================================

	def go_authorization_page(self):
		self.choosen_car = 0
		self.request = 0
		self.medType = ''
		self.healReport = 'Нет'
		self.alcoDes = ''
		self.pressureDesFrs = ''
		self.pressureDesSec = ''
		self.tempDes = ''
		self.plsDes = ''
		self.base = []
		self.cars_base = []
		self.cars_base_count = 0
		self.car_name_data = ''
		self.car_num_data = ''
		self.car_colors_data = ''
		self.car_counts_data = ''
		self.med_data = []
		self.car_page = 0

		self.qt_self.stack.setCurrentWidget(self.qt_self.authorization)
		num_field = self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "num_field")
		num_field.setStyleSheet(f"background: #FFFFFF;\n\nborder: 1px solid #CDCDCD;\nborder-radius: 16px;\n\nfont-family: \'Inter\';\nfont-style: normal;\nfont-weight: 400;\nfont-size: 22px;\n\ncolor: #8D8D8D;\n")
		num_field.setText('Логин/Номер телефона')

	# ============================================================================================================================================================================
	# 													██╗███╗░░██╗███████╗░█████╗░  ██████╗░░█████╗░░██████╗░███████╗
	# 													██║████╗░██║██╔════╝██╔══██╗  ██╔══██╗██╔══██╗██╔════╝░██╔════╝
	# 													██║██╔██╗██║█████╗░░██║░░██║  ██████╔╝███████║██║░░██╗░█████╗░░
	# 													██║██║╚████║██╔══╝░░██║░░██║  ██╔═══╝░██╔══██║██║░░╚██╗██╔══╝░░
	# 													██║██║░╚███║██║░░░░░╚█████╔╝  ██║░░░░░██║░░██║╚██████╔╝███████╗
	# 													╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░  ╚═╝░░░░░╚═╝░░╚═╝░╚═════╝░╚══════╝
	# ============================================================================================================================================================================

	def go_info_page(self):
		self.qt_self.stack.setCurrentWidget(self.qt_self.info)

	# ============================================================================================================================================================================	
	# 						███╗░░░███╗░█████╗░██╗░░██╗███████╗  ██████╗░███████╗░██████╗░██╗░░░██╗███████╗░██████╗████████╗  ████████╗░█████╗░
	# 						████╗░████║██╔══██╗██║░██╔╝██╔════╝  ██╔══██╗██╔════╝██╔═══██╗██║░░░██║██╔════╝██╔════╝╚══██╔══╝  ╚══██╔══╝██╔══██╗
	# 						██╔████╔██║███████║█████═╝░█████╗░░  ██████╔╝█████╗░░██║██╗██║██║░░░██║█████╗░░╚█████╗░░░░██║░░░  ░░░██║░░░██║░░██║
	# 						██║╚██╔╝██║██╔══██║██╔═██╗░██╔══╝░░  ██╔══██╗██╔══╝░░╚██████╔╝██║░░░██║██╔══╝░░░╚═══██╗░░░██║░░░  ░░░██║░░░██║░░██║
	# 						██║░╚═╝░██║██║░░██║██║░╚██╗███████╗  ██║░░██║███████╗░╚═██╔═╝░╚██████╔╝███████╗██████╔╝░░░██║░░░  ░░░██║░░░╚█████╔╝
	# 						╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝  ╚═╝░░╚═╝╚══════╝░░░╚═╝░░░░╚═════╝░╚══════╝╚═════╝░░░░╚═╝░░░  ░░░╚═╝░░░░╚════╝░
	# 															░█████╗░██████╗░███╗░░░███╗
	# 															██╔══██╗██╔══██╗████╗░████║
	# 															██║░░╚═╝██████╔╝██╔████╔██║
	# 															██║░░██╗██╔══██╗██║╚██╔╝██║
	# 															╚█████╔╝██║░░██║██║░╚═╝░██║
	# 															░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝
	# ============================================================================================================================================================================	

	def make_request(self):
		widget = self.qt_self.stack.currentWidget()
		error_text = widget.findChild(QtWidgets.QLabel, "error_text")
		try:

			self.request = int(widget.findChild(QtWidgets.QLabel, "num_field").text())

			if str(self.request)[:2] == '79' or str(self.request)[:2] == '89':
				self.request%=10000000000
				if get_user_number(self.request):
					
					user_data = get_user_number(self.request)
					self.sgo_info_page()
					widget = self.qt_self.stack.currentWidget()
					widget.findChild(QtWidgets.QPushButton, "next_step_button").setText("Сделать фото")
					name = widget.findChild(QtWidgets.QLabel, "name_field")
					date = widget.findChild(QtWidgets.QLabel, "date_field")
					number = widget.findChild(QtWidgets.QLabel, "number_field")
					name.setText(f"{user_data[0]}")
					date.setText(f"{user_data[1]}")
					number.setText(f"+7 {str(user_data[2])[3:]}")
				else:
					error_text.setText("Пользователь не найден")

					if str(user_data[4]) == '0':
						skud_button = widget.findChild(QtWidgets.QPushButton, "skud_button")
						skud_button.setText('Привязать карту СКУД')
						skud_button.setStyleSheet("color: #A6111B;\nbackground: #FFE0E3;\nborder-radius: 16px;")
					else:
						skud_button = widget.findChild(QtWidgets.QPushButton, "skud_button")
						skud_button.setText('Карта привязана')
						skud_button.setStyleSheet("color: #11A631;\nbackground: #F4FFF6;\nborder-radius: 16px;")

					if user_data[3] != None:
						qimg = ImageQt.ImageQt(user_data[3])
						photo_button = self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "photo_button")
						photo_button.setIcon(QIcon(QPixmap.fromImage(qimg)))
						photo_button.setIconSize(QtCore.QSize(224, 208))
					else:
						qimg = ImageQt.ImageQt(Image.open('./pagesCode/img/photo.png'))
						photo_button = self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "photo_button")
						photo_button.setIcon(QIcon(QPixmap.fromImage(qimg)))
						photo_button.setIconSize(QtCore.QSize(66, 60))
						
			else:
				if get_user_login(self.request):
					user_data = get_user_login(self.request)
					self.go_info_page()
					widget = self.qt_self.stack.currentWidget()
					widget.findChild(QtWidgets.QPushButton, "next_step_button").setText("Сделать фото")
					name = widget.findChild(QtWidgets.QLabel, "name_field")
					date = widget.findChild(QtWidgets.QLabel, "date_field")
					number = widget.findChild(QtWidgets.QLabel, "number_field")
					name.setText(f"{user_data[0]}")
					date.setText(f"{user_data[1]}")
					number.setText(f"+7 {str(user_data[2])[3:]}")

					if str(user_data[4]) == '0':
						skud_button = widget.findChild(QtWidgets.QPushButton, "skud_button")
						skud_button.setText('Привязать карту СКУД')
						skud_button.setStyleSheet("color: #A6111B;\nbackground: #FFE0E3;\nborder-radius: 16px;")
					else:
						skud_button = widget.findChild(QtWidgets.QPushButton, "skud_button")
						skud_button.setText('Карта привязана')
						skud_button.setStyleSheet("color: #11A631;\nbackground: #F4FFF6;\nborder-radius: 16px;")

					if user_data[3] != None:
						self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "next_step_button").setText("Это действительно я")
						qimg = ImageQt.ImageQt(user_data[3])
						photo_button = self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "photo_button")
						photo_button.setIcon(QIcon(QPixmap.fromImage(qimg)))
						photo_button.setIconSize(QtCore.QSize(224, 208))
					else:
						qimg = ImageQt.ImageQt(Image.open('./pagesCode/img/photo.png'))
						photo_button = self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "photo_button")
						photo_button.setIcon(QIcon(QPixmap.fromImage(qimg)))
						photo_button.setIconSize(QtCore.QSize(66, 60))
						
				else:
					error_text.setText("Пользователь не найден")
		except:
			error_text.setText("Ошибка!")

	# ============================================================================================================================================================================	
	#														
	# 														░█████╗░██████╗░██████╗░  ░█████╗░░█████╗░██████╗░██████╗░
	# 														██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗
	# 														███████║██║░░██║██║░░██║  ██║░░╚═╝███████║██████╔╝██║░░██║
	# 														██╔══██║██║░░██║██║░░██║  ██║░░██╗██╔══██║██╔══██╗██║░░██║
	# 														██║░░██║██████╔╝██████╔╝  ╚█████╔╝██║░░██║██║░░██║██████╔╝
	# 														╚═╝░░╚═╝╚═════╝░╚═════╝░  ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░
	# ============================================================================================================================================================================	

	def add_skud_card(self):
		add_card()
		QCoreApplication.processEvents()
		skud_button = self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "skud_button")
		skud_button.setText('Карта привязана')
		skud_button.setStyleSheet("color: #11A631;\nbackground: #F4FFF6;\nborder-radius: 16px;")

	# ============================================================================================================================================================================	
	# 													███╗░░░███╗░█████╗░██╗░░██╗███████╗  ██████╗░██╗░░██╗░█████╗░████████╗░█████╗░
	# 													████╗░████║██╔══██╗██║░██╔╝██╔════╝  ██╔══██╗██║░░██║██╔══██╗╚══██╔══╝██╔══██╗
	# 													██╔████╔██║███████║█████═╝░█████╗░░  ██████╔╝███████║██║░░██║░░░██║░░░██║░░██║
	# 													██║╚██╔╝██║██╔══██║██╔═██╗░██╔══╝░░  ██╔═══╝░██╔══██║██║░░██║░░░██║░░░██║░░██║
	# 													██║░╚═╝░██║██║░░██║██║░╚██╗███████╗  ██║░░░░░██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝
	# 													╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░
	# ============================================================================================================================================================================	

	def make_photo_b(self):
		pass
		# img = make_photo()
		# qimg = ImageQt.ImageQt(img)
		# photo_button = self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "photo_button")
		# photo_button.setIcon(QIcon(QPixmap.fromImage(qimg)))
		# photo_button.setIconSize(QtCore.QSize(202, 202))
		# self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "next_step_button").setText("Это действительно я")
		# QCoreApplication.processEvents()

	# ============================================================================================================================================================================														
	#															░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗██╗███╗░░██╗░██████╗░
	#															██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██║████╗░██║██╔════╝░
	#															██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░██║██╔██╗██║██║░░██╗░
	#															██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██║██║╚████║██║░░╚██╗
	#															╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗██║██║░╚███║╚██████╔╝
	#															░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░
	# ============================================================================================================================================================================	

	def go_first_step(self):
		if self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "next_step_button").text() == 'Сделать фото':
			img = make_photo()
			qimg = ImageQt.ImageQt(img)
			photo_button = self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "photo_button")
			photo_button.setIcon(QIcon(QPixmap.fromImage(qimg)))
			photo_button.setIconSize(QtCore.QSize(202, 202))
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "next_step_button").setText("Это действительно я")
		else:
			self.qt_self.stack.setCurrentWidget(self.qt_self.type_view)
		QCoreApplication.processEvents()

	# ============================================================================================================================================================================
	# 																████████╗██╗░░░██╗██████╗░███████╗  ░█████╗░███████╗
	# 																╚══██╔══╝╚██╗░██╔╝██╔══██╗██╔════╝  ██╔══██╗██╔════╝
	# 																░░░██║░░░░╚████╔╝░██████╔╝█████╗░░  ██║░░██║█████╗░░
	# 																░░░██║░░░░░╚██╔╝░░██╔═══╝░██╔══╝░░  ██║░░██║██╔══╝░░
	# 																░░░██║░░░░░░██║░░░██║░░░░░███████╗  ╚█████╔╝██║░░░░░
	# 																░░░╚═╝░░░░░░╚═╝░░░╚═╝░░░░░╚══════╝  ░╚════╝░╚═╝░░░░░
	# 													██╗███╗░░██╗░██████╗██████╗░███████╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
	# 													██║████╗░██║██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
	# 													██║██╔██╗██║╚█████╗░██████╔╝█████╗░░██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║
	# 													██║██║╚████║░╚═══██╗██╔═══╝░██╔══╝░░██║░░██╗░░░██║░░░██║██║░░██║██║╚████║
	# 													██║██║░╚███║██████╔╝██║░░░░░███████╗╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║
	# 													╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░░░░╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝
	# ============================================================================================================================================================================


	def go_type_view_page(self):
		self.qt_self.stack.setCurrentWidget(self.qt_self.type_view)

	def go_typeEx_page_before_day(self):
		self.medType = 'Предсменный'
		self.qt_self.stack.setCurrentWidget(self.qt_self.second_step)

	def go_typeEx_page_after_day(self):
		self.medType = 'Послесменный'
		self.qt_self.stack.setCurrentWidget(self.qt_self.second_step)

	def go_typeEx_page_before_raid(self):
		self.medType = 'Предрейсовый'
		self.qt_self.stack.setCurrentWidget(self.qt_self.second_step)

	def go_typeEx_page_after_raid(self):
		self.medType = 'Послерейсовый'
		self.qt_self.stack.setCurrentWidget(self.qt_self.second_step)

	# ============================================================================================================================================================================
	# 																	██████╗░███████╗██████╗░░█████╗░██████╗░████████╗
	# 																	██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
	# 																	██████╔╝█████╗░░██████╔╝██║░░██║██████╔╝░░░██║░░░
	# 																	██╔══██╗██╔══╝░░██╔═══╝░██║░░██║██╔══██╗░░░██║░░░
	# 																	██║░░██║███████╗██║░░░░░╚█████╔╝██║░░██║░░░██║░░░
	# 																	╚═╝░░╚═╝╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
	# ============================================================================================================================================================================

	def report_page(self):
		self.qt_self.stack.setCurrentWidget(self.qt_self.type_report)

	def go_alco_page_backache(self):
		self.healReport = 'Боль в спине'
		self.get_checking()

	def go_alco_page_stomackache(self):
		self.healReport = 'Боль в животе'
		self.get_checking()

	def go_alco_page_eyeache(self):
		self.healReport = 'Боль в глазах'
		self.get_checking()

	def go_alco_page_handache(self):
		self.healReport = 'Боль в руках'
		self.get_checking()

	def go_alco_page_headache(self):
		self.healReport = 'Головная боль'
		self.get_checking()

	def go_alco_page_teethache(self):
		self.healReport = 'Зубная боль'
		self.get_checking()

	def go_alco_page_other(self):
		self.healReport = 'Другое'
		self.get_checking()

	# ============================================================================================================================================================================
	# 															░██████╗░███████╗████████╗  ██████╗░░█████╗░████████╗░█████╗░
	# 															██╔════╝░██╔════╝╚══██╔══╝  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗
	# 															██║░░██╗░█████╗░░░░░██║░░░  ██║░░██║███████║░░░██║░░░███████║
	# 															██║░░╚██╗██╔══╝░░░░░██║░░░  ██║░░██║██╔══██║░░░██║░░░██╔══██║
	# 															╚██████╔╝███████╗░░░██║░░░  ██████╔╝██║░░██║░░░██║░░░██║░░██║
	# 															░╚═════╝░╚══════╝░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝
	# ============================================================================================================================================================================
	def get_checking(self):

		self.qt_self.stack.setCurrentWidget(self.qt_self.alcohol_check)
		QCoreApplication.processEvents()
		self.alcoDes = alcohol_detecter()
		

		self.qt_self.stack.setCurrentWidget(self.qt_self.pressure_check)
		QCoreApplication.processEvents()
		pressure_values = pressure_detecter()
		self.pressureDesFrs = pressure_values[0]
		self.pressureDesSec = pressure_values[1]
		self.plsDes = pressure_values[2]
		

		self.qt_self.stack.setCurrentWidget(self.qt_self.temperature_check)
		QCoreApplication.processEvents()
		self.tempDes = temperature_detecter()
		

		self.accept_res()

	# ============================================================================================================================================================================
	# 													██████╗░███████╗░██████╗██╗░░░██╗██╗░░░░░████████╗░██████╗
	# 													██╔══██╗██╔════╝██╔════╝██║░░░██║██║░░░░░╚══██╔══╝██╔════╝
	# 													██████╔╝█████╗░░╚█████╗░██║░░░██║██║░░░░░░░░██║░░░╚█████╗░
	# 													██╔══██╗██╔══╝░░░╚═══██╗██║░░░██║██║░░░░░░░░██║░░░░╚═══██╗
	# 													██║░░██║███████╗██████╔╝╚██████╔╝███████╗░░░██║░░░██████╔╝
	# 													╚═╝░░╚═╝╚══════╝╚═════╝░░╚═════╝░╚══════╝░░░╚═╝░░░╚═════╝░
	# ============================================================================================================================================================================

	def accept_res(self):
		self.qt_self.stack.setCurrentWidget(self.qt_self.result)
		widget = self.qt_self.stack.currentWidget()
		tpe = widget.findChild(QtWidgets.QLabel, "view_type_input")
		hlRep = widget.findChild(QtWidgets.QLabel, "reports_heal_input")
		alRep = widget.findChild(QtWidgets.QLabel, "alcho")
		spRep = widget.findChild(QtWidgets.QLabel, "s_pressure_input")
		dpRep = widget.findChild(QtWidgets.QLabel, "d_pressure_input")
		plsRep = widget.findChild(QtWidgets.QLabel, "pulse_input")
		tpRep = widget.findChild(QtWidgets.QLabel, "temperature_input")

		if self.healReport!='Нет':
			self.base.append(['Жалобы на здоровье', self.healReport])
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, f"reports_heal_input").setStyleSheet(f"color: #DE1E1E;")
		else:
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, f"reports_heal_input").setStyleSheet(f"color: #49C21E;")
		if float(self.tempDes)<minTemp or float(self.tempDes)>maxTemp:
			self.base.append(['Температура', self.tempDes])
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, f"temperature_input").setStyleSheet(f"color: #DE1E1E;")
		else:
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, f"temperature_input").setStyleSheet(f"color: #49C21E;")

		if float(self.alcoDes)>maxAlco:
			self.base.append(['Уровень алкоголя в крови', self.alcoDes])
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, f"alcho").setStyleSheet(f"color: #DE1E1E;")
		else:
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, f"alcho").setStyleSheet(f"color: #49C21E;")

		if float(self.pressureDesFrs)>maxSisPl or float(self.pressureDesFrs)<minSisPl:
			self.base.append(['Систолическое давление', self.pressureDesFrs])
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, f"s_pressure_input").setStyleSheet(f"color: #DE1E1E;")
		else:
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, f"s_pressure_input").setStyleSheet(f"color: #49C21E;")

		if float(self.pressureDesSec)>maxDiaPl or float(self.pressureDesSec)<minDiaPl:
			self.base.append(['Диастолическое давление', self.pressureDesSec])
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, f"d_pressure_input").setStyleSheet(f"color: #DE1E1E;")
		else:
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, f"d_pressure_input").setStyleSheet(f"color: #49C21E;")

		if float(self.plsDes)>maxPulse or float(self.plsDes)<minPulse:
			self.base.append(['Пульс', self.plsDes])
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, f"pulse_input").setStyleSheet(f"color: #DE1E1E;")
		else:
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, f"pulse_input").setStyleSheet(f"color: #49C21E;")

			
		tpe.setText(f"{self.medType}")
		self.med_data.append(f"{self.medType}")
		hlRep.setText(f"{self.healReport}")
		self.med_data.append(f"{self.healReport}")
		alRep.setText(f"{self.alcoDes} ‰")
		self.med_data.append(f"{self.alcoDes}")
		spRep.setText(f"{self.pressureDesFrs} мм рт. ст.")
		self.med_data.append(f"{self.pressureDesFrs}")
		dpRep.setText(f"{self.pressureDesSec} мм рт. ст.")
		self.med_data.append(f"{self.pressureDesSec}")
		plsRep.setText(f"{self.plsDes} уд/мин")
		self.med_data.append(f"{self.plsDes}")
		tpRep.setText(f"{self.tempDes} C°")
		self.med_data.append(f"{self.tempDes}")

	# ============================================================================================================================================================================
	# 							██████╗░███████╗░██████╗██╗░░░██╗██╗░░░░░████████╗░██████╗  ██████╗░░█████╗░░██████╗░███████╗
	# 							██╔══██╗██╔════╝██╔════╝██║░░░██║██║░░░░░╚══██╔══╝██╔════╝  ██╔══██╗██╔══██╗██╔════╝░██╔════╝
	# 							██████╔╝█████╗░░╚█████╗░██║░░░██║██║░░░░░░░░██║░░░╚█████╗░  ██████╔╝███████║██║░░██╗░█████╗░░
	# 							██╔══██╗██╔══╝░░░╚═══██╗██║░░░██║██║░░░░░░░░██║░░░░╚═══██╗  ██╔═══╝░██╔══██║██║░░╚██╗██╔══╝░░
	# 							██║░░██║███████╗██████╔╝╚██████╔╝███████╗░░░██║░░░██████╔╝  ██║░░░░░██║░░██║╚██████╔╝███████╗
	# 							╚═╝░░╚═╝╚══════╝╚═════╝░░╚═════╝░╚══════╝░░░╚═╝░░░╚═════╝░  ╚═╝░░░░░╚═╝░░╚═╝░╚═════╝░╚══════╝
	# ============================================================================================================================================================================

	def go_last_med_page(self):
		if len(self.base)>0:
			self.qt_self.stack.setCurrentWidget(self.qt_self.result_false)
			if len(self.base)>3:
				for i in range(1,4):
					self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, f"editinfoText_{i}").setText(f'{self.base[i-1][0]}')
					line2 = self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, f"editinfoText_{i}_1")
					line2.setStyleSheet(f"color: #DE1E1E;")
					line2.setText(f'{self.base[i-1][1]}')
			else:
				for i in range(1, len(self.base)+1):
					self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, f"editinfoText_{i}").setText(f'{self.base[i-1][0]}')
					line2 = self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, f"editinfoText_{i}_1")
					line2.setStyleSheet(f"color: #DE1E1E;")
					line2.setText(f'{self.base[i-1][1]}')
		else:
			self.qt_self.stack.setCurrentWidget(self.qt_self.result_true)
			send_med_to_crm(self.med_data)

	# ============================================================================================================================================================================
	#											██╗███╗░░██╗░██████╗████████╗██████╗░██╗░░░██╗░█████╗░████████╗  ██████╗░░█████╗░░██████╗░███████╗
	#											██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██║░░░██║██╔══██╗╚══██╔══╝  ██╔══██╗██╔══██╗██╔════╝░██╔════╝
	#											██║██╔██╗██║╚█████╗░░░░██║░░░██████╔╝██║░░░██║██║░░╚═╝░░░██║░░░  ██████╔╝███████║██║░░██╗░█████╗░░
	#											██║██║╚████║░╚═══██╗░░░██║░░░██╔══██╗██║░░░██║██║░░██╗░░░██║░░░  ██╔═══╝░██╔══██║██║░░╚██╗██╔══╝░░
	#											██║██║░╚███║██████╔╝░░░██║░░░██║░░██║╚██████╔╝╚█████╔╝░░░██║░░░  ██║░░░░░██║░░██║╚██████╔╝███████╗
	#											╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░░╚════╝░░░░╚═╝░░░  ╚═╝░░░░░╚═╝░░╚═╝░╚═════╝░╚══════╝
	# ============================================================================================================================================================================

	def go_instructage(self):
		self.qt_self.stack.setCurrentWidget(self.qt_self.instruct_audio)

	def play_first_audio(self):
		play_m('modules/audio/first.wav')

	def play_second_audio(self):
		play_m('modules/audio/second.wav')

	def play_third_audio(self):
		play_m('modules/audio/third.wav')

	def play_fourth_audio(self):
		play_m('4.mp3')

	def play_fifth_audio(self):
		play_m('5.mp3')

	def play_sixth_audio(self):
		play_m('modules/audio/last.wav')

	def go_accept_inst_data(self):
		self.qt_self.stack.setCurrentWidget(self.qt_self.instruct_audio_done)

	def go_choose_car(self):
		self.qt_self.stack.setCurrentWidget(self.qt_self.car_choose)
		self.generate_car_page()

	# ============================================================================================================================================================================
	#																		 ░█████╗░░█████╗░██████╗░  ██████╗░░█████╗░░██████╗░███████╗
	#																		 ██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗██╔════╝░██╔════╝
	#																		 ██║░░╚═╝███████║██████╔╝  ██████╔╝███████║██║░░██╗░█████╗░░
	#																		 ██║░░██╗██╔══██║██╔══██╗  ██╔═══╝░██╔══██║██║░░╚██╗██╔══╝░░
	#																		 ╚█████╔╝██║░░██║██║░░██║  ██║░░░░░██║░░██║╚██████╔╝███████╗
	#																		 ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ╚═╝░░░░░╚═╝░░╚═╝░╚═════╝░╚══════╝
	# ============================================================================================================================================================================

	def generate_car_page(self):
		self.cars_base_count = get_cars()[0]
		self.cars_base = get_cars()[1]
		cars_base_count = self.cars_base_count
		cars_base = self.cars_base
		if cars_base_count > 0:
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_name_1").setText(f'{cars_base[0]["название"]}')
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_number_data_1").setText(f'{cars_base[0]["номер"]}')
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_color_data_1").setText(f'{cars_base[0]["цвет"]}')
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_count_data_1").setText(f'{cars_base[0]["пробег"]} км')
			img = (get_photo_one(f'{cars_base[0]["фото"]}'))
			qimg = ImageQt.ImageQt(img)
			first_car_photo = self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "car_img_1")
			first_car_photo.setIcon(QIcon(QPixmap.fromImage(qimg)))
			first_car_photo.setIconSize(QtCore.QSize(100, 100))

			if cars_base_count >= 2:
				self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_name_2").setText(f'{cars_base[1]["название"]}')
				self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_number_data_2").setText(f'{cars_base[1]["номер"]}')
				self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_color_data_2").setText(f'{cars_base[1]["цвет"]}')
				self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_count_data_2").setText(f'{cars_base[1]["пробег"]} км')
				img = (get_photo_two(f'{cars_base[1]["фото"]}'))
				qimg = ImageQt.ImageQt(img)
				second_car_photo = self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "car_img_2")
				second_car_photo.setIcon(QIcon(QPixmap.fromImage(qimg)))
				second_car_photo.setIconSize(QtCore.QSize(100, 100))
			else:
				self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_name_2").setText('')
				self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_number_data_2").setText('')
				self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_color_data_2").setText('')
				self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_count_data_2").setText('')

	def next_car_page(self):
		choose = self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "choose_button_1")
		choose.setText('Выбрать')
		choose.setStyleSheet("border-radius: 16;\nbackground-color:#F6F6F6;\ncolor: black;")
		choose2 = self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "choose_button_2")
		choose2.setText('Выбрать')
		choose2.setStyleSheet("border-radius: 16;\nbackground-color:#F6F6F6;\ncolor: black;")
		cars_base = self.cars_base
		if self.car_page+2 != self.cars_base_count:
			self.car_page += 1
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_name_1").setText(f'{cars_base[self.car_page]["название"]}')
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_number_data_1").setText(f'{cars_base[self.car_page]["номер"]}')
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_color_data_1").setText(f'{cars_base[self.car_page]["цвет"]}')
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_count_data_1").setText(f'{cars_base[self.car_page]["пробег"]} км')
			img = (get_photo_one(f'{cars_base[self.car_page]["фото"]}'))
			qimg = ImageQt.ImageQt(img)
			first_car_photo = self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "car_img_1")
			first_car_photo.setIcon(QIcon(QPixmap.fromImage(qimg)))
			first_car_photo.setIconSize(QtCore.QSize(100, 100))

			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_name_2").setText(f'{cars_base[self.car_page+1]["название"]}')
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_number_data_2").setText(f'{cars_base[self.car_page+1]["номер"]}')
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_color_data_2").setText(f'{cars_base[self.car_page+1]["цвет"]}')
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_count_data_2").setText(f'{cars_base[self.car_page+1]["пробег"]} км')
			img = (get_photo_two(f'{cars_base[self.car_page+1]["фото"]}'))
			qimg = ImageQt.ImageQt(img)
			first_car_photo = self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "car_img_2")
			first_car_photo.setIcon(QIcon(QPixmap.fromImage(qimg)))
			first_car_photo.setIconSize(QtCore.QSize(100, 100))
		QCoreApplication.processEvents()

	def back_car_page(self):
		choose = self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "choose_button_1")
		choose.setText('Выбрать')
		choose.setStyleSheet("border-radius: 16;\nbackground-color:#F6F6F6;\ncolor: black;")
		choose2 = self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "choose_button_2")
		choose2.setText('Выбрать')
		choose2.setStyleSheet("border-radius: 16;\nbackground-color:#F6F6F6;\ncolor: black;")
		cars_base = self.cars_base
		if self.car_page != 0:
			self.car_page -= 1
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_name_1").setText(f'{cars_base[self.car_page]["название"]}')
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_number_data_1").setText(f'{cars_base[self.car_page]["номер"]}')
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_color_data_1").setText(f'{cars_base[self.car_page]["цвет"]}')
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_count_data_1").setText(f'{cars_base[self.car_page]["пробег"]} км')
			img = (get_photo_one(f'{cars_base[self.car_page]["фото"]}'))
			qimg = ImageQt.ImageQt(img)
			first_car_photo = self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "car_img_1")
			first_car_photo.setIcon(QIcon(QPixmap.fromImage(qimg)))
			first_car_photo.setIconSize(QtCore.QSize(100, 100))

			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_name_2").setText(f'{cars_base[self.car_page+1]["название"]}')
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_number_data_2").setText(f'{cars_base[self.car_page+1]["номер"]}')
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_color_data_2").setText(f'{cars_base[self.car_page+1]["цвет"]}')
			self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_count_data_2").setText(f'{cars_base[self.car_page+1]["пробег"]} км')
			img = (get_photo_two(f'{cars_base[self.car_page+1]["фото"]}'))
			qimg = ImageQt.ImageQt(img)
			first_car_photo = self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "car_img_2")
			first_car_photo.setIcon(QIcon(QPixmap.fromImage(qimg)))
			first_car_photo.setIconSize(QtCore.QSize(100, 100))
		QCoreApplication.processEvents()

	def choose_first_car(self):
		choose = self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "choose_button_1")
		choose.setText('Выбрано')
		choose.setStyleSheet("border-radius: 16;\nbackground-color:#F4FFF6;\ncolor: #11A631;")
		choose2 = self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "choose_button_2")
		choose2.setText('Выбрать')
		choose2.setStyleSheet("border-radius: 16;\nbackground-color:#F6F6F6;\ncolor: black;")
		cars_base = self.cars_base
		self.car_name_data = f'{cars_base[self.car_page]["название"]}'
		self.car_num_data = f'{cars_base[self.car_page]["номер"]}'
		self.car_colors_data = f'{cars_base[self.car_page]["цвет"]}'
		self.car_counts_data = f'{cars_base[self.car_page]["пробег"]} км'
		self.choosen_car = 1

	def choose_second_car(self):
		choose = self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "choose_button_1")
		choose.setText('Выбрать')
		choose.setStyleSheet("border-radius: 16;\nbackground-color:#F6F6F6;\ncolor: black;")
		choose = self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "choose_button_2")
		choose.setText('Выбрано')
		choose.setStyleSheet("border-radius: 16;\nbackground-color:#F4FFF6;\ncolor: #11A631;")
		cars_base = self.cars_base
		self.car_name_data = f'{cars_base[self.car_page+1]["название"]}'
		self.car_num_data = f'{cars_base[self.car_page+1]["номер"]}'
		self.car_colors_data = f'{cars_base[self.car_page+1]["цвет"]}'
		self.car_counts_data = f'{cars_base[self.car_page+1]["пробег"]} км'
		self.choosen_car = 1


	# ============================================================================================================================================================================
	# 										░█████╗░░█████╗░██████╗░  ██████╗░░█████╗░████████╗░█████╗░  ██████╗░░█████╗░░██████╗░███████╗
	# 										██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗  ██╔══██╗██╔══██╗██╔════╝░██╔════╝
	# 										██║░░╚═╝███████║██████╔╝  ██║░░██║███████║░░░██║░░░███████║  ██████╔╝███████║██║░░██╗░█████╗░░
	# 										██║░░██╗██╔══██║██╔══██╗  ██║░░██║██╔══██║░░░██║░░░██╔══██║  ██╔═══╝░██╔══██║██║░░╚██╗██╔══╝░░
	# 										╚█████╔╝██║░░██║██║░░██║  ██████╔╝██║░░██║░░░██║░░░██║░░██║  ██║░░░░░██║░░██║╚██████╔╝███████╗
	# 										░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝  ╚═╝░░░░░╚═╝░░╚═╝░╚═════╝░╚══════╝
	# ============================================================================================================================================================================
	def go_car_data(self):
		if self.choosen_car == 1:
			self.qt_self.stack.setCurrentWidget(self.qt_self.car_data)
			text = self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "car_name_field")
			text.setText(f'{self.car_name_data}, {self.car_num_data}')

	def go_end(self):
		miles = self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "mileage_field").text()
		fuel = self.qt_self.stack.currentWidget().findChild(QtWidgets.QPushButton, "fuel_field").text()
		if miles != 'Текущий пробег, км':
			miles = int(miles)
			if fuel != 'Остаток топлива в литрах':
				fuel = int(fuel)
			else:
				fuel = 0
			if miles > 10000:
				send_car_to_crm([self.car_name_data, self.car_num_data, miles, fuel])
				# self.qt_self.stack.setCurrentWidget(self.qt_self.last_page)
			else:
				err_text = self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "error_text")
				err_text.setText(f'Введите корректное значение!')
		else:
			err_text = self.qt_self.stack.currentWidget().findChild(QtWidgets.QLabel, "error_text")
			err_text.setText(f'Введите корректное значение!')

	# ============================================================================================================================================================================
	# 																███████╗███╗░░██╗██████╗░  ░██╗░░░░░░░██╗░█████╗░██████╗░██╗░░██╗
	# 																██╔════╝████╗░██║██╔══██╗  ░██║░░██╗░░██║██╔══██╗██╔══██╗██║░██╔╝
	# 																█████╗░░██╔██╗██║██║░░██║  ░╚██╗████╗██╔╝██║░░██║██████╔╝█████═╝░
	# 																██╔══╝░░██║╚████║██║░░██║  ░░████╔═████║░██║░░██║██╔══██╗██╔═██╗░
	# 																███████╗██║░╚███║██████╔╝  ░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██║░╚██╗
	# 																╚══════╝╚═╝░░╚══╝╚═════╝░  ░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝
	# ============================================================================================================================================================================

	def do_end_work(self):
		print_qr()
		self.go_authorization_page()