from PIL import Image

def get_user_login(login):
	if login == 0:
		img = None
		name = 'T T T'
		date = '11.11.1111'
		number = '+1 000 000 00-00'
		card_id = 0
		return [name, date, number, img, card_id]
	elif login == 1:
		img = Image.open("./crm/ava.png")
		name = 'Иванов Иван Иванович'
		date = '00.00.0000'
		number = '+1 111 111 11-11'
		card_id = 1432234324
		return [name, date, number, img, card_id]
	return False

def get_user_number(number):
	if number == 1111111111:
		img = None
		name = 'Иванов Иван Иванович'
		date = '00.00.0000'
		number = '+1 111 111 11-11'
		card_id = 0
		return [name, date, number, img, card_id]
	return False