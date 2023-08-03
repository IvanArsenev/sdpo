from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from pagesCode.one_authorization_page import authorization_page
from pagesCode.two_info_page import info_page
from pagesCode.three_type_view_page import type_view_page
from pagesCode.four_second_step_page import second_step_page
from pagesCode.four_one_type_report_page import type_report_page
from pagesCode.five_alcohol_check_page import alcohol_check_page
from pagesCode.six_pressure_check_page import pressure_check_page
from pagesCode.seven_temperature_check_page import temperature_check_page
from pagesCode.eight_result_page import result_page
from pagesCode.nine_result_true_page import result_true_page
from pagesCode.nine_result_false_page import result_false_page
from pagesCode.ten_instruct_audio_page import instruct_audio_page
from pagesCode.ten_instruct_audio_done_page import instruct_audio_done_page
from pagesCode.eleven_car_choose_page import car_choose_page
from pagesCode.twelve_car_data_page import car_data_page


class one_authorization_page_class(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = authorization_page()
		self.ui.setupUi(self)

class two_info_page_class(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = info_page()
		self.ui.setupUi(self)

class three_type_view_page_class(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = type_view_page()
		self.ui.setupUi(self)

class four_second_step_page_class(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = second_step_page()
		self.ui.setupUi(self)

class four_one_type_report_page_class(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = type_report_page()
		self.ui.setupUi(self)

class five_alcohol_check_page_class(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = alcohol_check_page()
		self.ui.setupUi(self)

class six_pressure_check_page_class(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = pressure_check_page()
		self.ui.setupUi(self)

class seven_temperature_check_page_class(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = temperature_check_page()
		self.ui.setupUi(self)

class eight_result_page_class(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = result_page()
		self.ui.setupUi(self)

class nine_result_true_page_class(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = result_true_page()
		self.ui.setupUi(self)

class nine_result_false_page_class(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = result_false_page()
		self.ui.setupUi(self)

class ten_instruct_audio_page_class(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = instruct_audio_page()
		self.ui.setupUi(self)

class ten_instruct_audio_done_page_class(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = instruct_audio_done_page()
		self.ui.setupUi(self)

class eleven_car_choose_page_class(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = car_choose_page()
		self.ui.setupUi(self)

class twelve_car_data_page_class(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = car_data_page()
		self.ui.setupUi(self)

class App(QApplication):
	def __init__(self, utils):
		super().__init__([])
		self.stack = QStackedWidget()

		self.authorization = one_authorization_page_class()
		self.stack.addWidget(self.authorization)

		self.info = two_info_page_class()
		self.stack.addWidget(self.info)

		self.type_view = three_type_view_page_class()
		self.stack.addWidget(self.type_view)

		self.second_step = four_second_step_page_class()
		self.stack.addWidget(self.second_step)

		self.type_report = four_one_type_report_page_class()
		self.stack.addWidget(self.type_report)

		self.alcohol_check = five_alcohol_check_page_class()
		self.stack.addWidget(self.alcohol_check)

		self.pressure_check = six_pressure_check_page_class()
		self.stack.addWidget(self.pressure_check)

		self.temperature_check = seven_temperature_check_page_class()
		self.stack.addWidget(self.temperature_check)

		self.result = eight_result_page_class()
		self.stack.addWidget(self.result)

		self.result_true = nine_result_true_page_class()
		self.stack.addWidget(self.result_true)

		self.result_false = nine_result_false_page_class()
		self.stack.addWidget(self.result_false)

		self.instruct_audio = ten_instruct_audio_page_class()
		self.stack.addWidget(self.instruct_audio)

		self.instruct_audio_done = ten_instruct_audio_done_page_class()
		self.stack.addWidget(self.instruct_audio_done)

		self.car_choose = eleven_car_choose_page_class()
		self.stack.addWidget(self.car_choose)

		self.car_data = twelve_car_data_page_class()
		self.stack.addWidget(self.car_data)




		self.stack.setCurrentWidget(self.authorization)
		utils.qt_init(self)
		self.stack.show()