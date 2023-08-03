def download_cars_photo():
    array_of_photo = []
    i = 1
    for photo in array_of_photo:
        photo.save(f'./modules/car_photos/{i}.png')
        i+=1


def get_cars():
    download_cars_photo()
    car_list = []
    
    car_data = [
        {
            'название': 'Лада',
            'номер': 'А111АА',
            'цвет': 'Красный',
            'пробег': '111111',
            'фото': './modules/car_photos/1.png'
        },
        {
            'название': 'Жигуль',
            'номер': 'Б222ББ',
            'цвет': 'Оранжевый',
            'пробег': '222222',
            'фото': './modules/car_photos/2.png'
        },
        {
            'название': 'БМВ',
            'номер': 'В333ВВ',
            'цвет': 'Желтый',
            'пробег': '333333',
            'фото': './modules/car_photos/3.png'
        },
        {
            'название': 'Мерседес',
            'номер': 'Г444ГГ',
            'цвет': 'Зеленый',
            'пробег': '444444',
            'фото': './modules/car_photos/4.png'
        },
        {
            'название': 'Ауди',
            'номер': 'Д555ДД',
            'цвет': 'Синий',
            'пробег': '555555',
            'фото': './modules/car_photos/5.png'
        }
    ]
    
    for car in car_data:
        car_list.append(car)
    
    return [len(car_list), car_list]