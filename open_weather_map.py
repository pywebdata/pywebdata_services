from pywebdata.baseservice import BaseService

class OpenWeatherMap(BaseService):

    name = 'open-weather-map'

    def __init__(self):
        self.add_url('http://api.openweathermap.org/data/2.5/weather?lat=$latitude&lon=$longitude')
        self.add_input('latitude', iotype='float', required=True, min=-90., max=90., incr=1.)
        self.add_input('longitude', iotype='float', required=True, min=-180., max=180., incr=1.)
        self.add_output('temp', iotype='float')
        self.add_parser(staticmethod(lambda x:x['main']))