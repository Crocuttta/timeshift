'''
Программа локального времени в городах.
Содержит меню,щее из пунктов:
    1. Выод списка городом и их локального времени;
    2.Добавление нового города;
    3.Выход из программы.
Информация о часовом поясе города берется с сервиса abstractapi.com
В случае нахождения города (его корректного имени) его имя и часовой
пояс сохраняется в локальный список программы.
'''

from provider import Abstractapi


def get_show_menu():
    print(
            '\nВведите команду:\n'
            '1.Вывести список городов\n'
            '2.Добавить город\n'
            '3.Выход'
        ) 


if __name__ == '__main__':    
    cities = dict()
    while True:
        get_show_menu()
        command = input('>>> ')
        print()
        abstractapi = Abstractapi()
        # Вывод списка городов.       
        if command == '1':
            abstractapi.show_cities_list(cities)
        # Поиск и добавление нового города.
        elif command == '2':
            city_name = input('Введите имя города: ')  
            city_data = abstractapi.find_city(city_name)
            if not city_data:
                continue
            cities[city_data['name']] = city_data['gmt_offset']
        # Неизвестная комманда
        elif command == '3':        
            break
        else:
            print(f'Неизвестная команда {command}.')
