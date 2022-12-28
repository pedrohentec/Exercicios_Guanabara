# Conversor de Temperaturas
temperatura = input('Informe a temperatura em °C: ')
temperatura_float = float(temperatura)
fahrenheit = (temperatura_float * 9 / 5 ) + 32
kelvin = temperatura_float + 273.15

print(f'A temperatura de {temperatura_float}°C corresponde à {fahrenheit}°F')
print(f'A temperatura de {temperatura_float}°C corresponde à {kelvin}°K')
