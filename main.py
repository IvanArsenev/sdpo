from utils import Utils
from init import App

utils = Utils()

if __name__ == '__main__':
	app = App(utils)
	
	app.authorization.ui.enter_button.clicked.connect(utils.make_request)

	app.info.ui.decline_button.clicked.connect(utils.go_authorization_page)
	app.info.ui.skud_button.clicked.connect(utils.add_skud_card)
	app.info.ui.next_step_button.clicked.connect(utils.go_first_step)
	app.info.ui.photo_button.clicked.connect(utils.make_photo_b)

	app.type_view.ui.before_day_button.clicked.connect(utils.go_typeEx_page_before_day)
	app.type_view.ui.after_day_button.clicked.connect(utils.go_typeEx_page_after_day)
	app.type_view.ui.before_raid_button.clicked.connect(utils.go_typeEx_page_before_raid)
	app.type_view.ui.after_raid_button.clicked.connect(utils.go_typeEx_page_after_raid)
	app.type_view.ui.back_button.clicked.connect(utils.go_info_page)

	app.second_step.ui.back_button.clicked.connect(utils.go_type_view_page)
	app.second_step.ui.skip_step_button.clicked.connect(utils.get_checking)
	app.second_step.ui.report_heal_button.clicked.connect(utils.report_page)

	app.type_report.ui.backache_button.clicked.connect(utils.go_alco_page_backache)
	app.type_report.ui.stomackache_button.clicked.connect(utils.go_alco_page_stomackache)
	app.type_report.ui.eyeache_button.clicked.connect(utils.go_alco_page_eyeache)
	app.type_report.ui.handache_button.clicked.connect(utils.go_alco_page_handache)
	app.type_report.ui.headache_button.clicked.connect(utils.go_alco_page_headache)
	app.type_report.ui.teethache_button.clicked.connect(utils.go_alco_page_teethache)
	app.type_report.ui.other_button.clicked.connect(utils.go_alco_page_other)
	app.type_report.ui.back_button.clicked.connect(utils.go_type_view_page)

	app.result.ui.decline_button.clicked.connect(utils.go_authorization_page)
	app.result.ui.accept_button.clicked.connect(utils.go_last_med_page)

	app.result_false.ui.exit_button.clicked.connect(utils.go_authorization_page)
	
	app.result_true.ui.send_data_button.clicked.connect(utils.go_instructage)

	app.instruct_audio.ui.play_audio_first_button.clicked.connect(utils.play_first_audio)
	app.instruct_audio.ui.play_audio_second_button.clicked.connect(utils.play_second_audio)
	app.instruct_audio.ui.play_audio_third_button.clicked.connect(utils.play_third_audio)
	app.instruct_audio.ui.play_audio_fourth_button.clicked.connect(utils.play_fourth_audio)
	app.instruct_audio.ui.play_audio_fifth_button.clicked.connect(utils.play_fifth_audio)
	app.instruct_audio.ui.play_audio_sixth_button.clicked.connect(utils.play_sixth_audio)
	app.instruct_audio.ui.accept_button.clicked.connect(utils.go_accept_inst_data)

	app.instruct_audio_done.ui.send_data_button.clicked.connect(utils.go_choose_car)

	app.car_choose.ui.back_button.clicked.connect(utils.back_car_page)
	app.car_choose.ui.next_buton.clicked.connect(utils.next_car_page)
	app.car_choose.ui.choose_button_1.clicked.connect(utils.choose_first_car)
	app.car_choose.ui.choose_button_2.clicked.connect(utils.choose_second_car)
	app.car_choose.ui.accept_button.clicked.connect(utils.go_car_data)

	app.car_data.ui.next_step_page.clicked.connect(utils.go_end)

	# app.end.ui.next_step_page.clicked.connect(utils.do_end_work)

	app.exec()