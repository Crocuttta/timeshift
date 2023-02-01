import datetime

import requests

class Provider:

    def show_cities_list(self, cities):
        for city_name in sorted(cities):
            local_time = self.get_local_time(cities[city_name])
            print(f'{city_name}: {local_time}')


    def get_local_time(
        self,
        gmt_offset,
        current_utc_time=datetime.datetime.now(datetime.timezone.utc)
        ):
        '''
        Определение текущего времени по значению часового пояса.

        Параметры:
            'gmt_offset': смещение в часах относительно времени UTC;
            'current_utc_time': текущее время UTC.
        '''
        return (
            current_utc_time
            + datetime.timedelta(hours=gmt_offset)
        ).strftime('%H:%M')    


class Abstractapi(Provider):
    
    ABSTRACT_API_URL = (
        'https://timezone.abstractapi.com/v1/current_time/?'
        'api_key=67a70fd196da44f19184fefc7f80145f&location='
    )

    @classmethod
    def class_method(cls):        
        pass


    @staticmethod
    def static_method():
        pass    


    def find_city(self, city_name):
        '''
        Поиск города и информации о его времени с помощью abstractapi.com.
        '''
        
        city_data = requests.get(self.ABSTRACT_API_URL + city_name).json()
        print('>>>> ', city_data)
        if not city_data or city_data.get('error', False):
            return None       
        print('Текущее время: ', self.get_local_time(city_data['gmt_offset']))
        return {
            'gmt_offset' : city_data['gmt_offset'],
            'name' : city_name
        }    
    