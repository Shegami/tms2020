from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('f0de3615b1d2bdb301f835e326d4453f', config_dict)

mgr = owm.weather_manager()
observation = mgr.weather_at_place(input('Введите страну или город: '))
w = observation.weather
temp = w.temperature('celsius')

# Общая информация
w = w.detailed_status

# Температура
t = temp['temp']
f = temp['feels_like']

# Скорость ветра
wind = observation.weather.wind()
z = wind['speed']    # м/с

print("\nНа улице сейчас " + w + ".")
print("\nТемпература: " + str(t) + " ℃. " + "\nОщущается как: " + str(f) + " ℃.")

if f < 16 and z > 16:
    print('\nСоветуем одеться тепло. На улице прохладно и сильный ветер.')
elif f < 7:
    print('На улице холодно. Одевайтесь тепло.')
elif f < 16:
    print('Советуем одеться теплее. На улице прохладно.')
else:
    print("На улице тепло. Шорты и майка будут по погоде :)")
input()