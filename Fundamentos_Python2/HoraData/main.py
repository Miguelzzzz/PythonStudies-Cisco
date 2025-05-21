print("Datetime")

# Obter a data local atual e criar objetos de data
from datetime import date

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)
    
# O método replace(), pode ser necessário substituir o ano, mês ou dia por um valor diferente. Você não pode fazer isso com os atributos year, month e day porque eles são somente leitura
from datetime import date

d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)

# A função ctime(), converte o tempo em segundos desde 1 de janeiro de 1970 (época Unix) para uma string
import time

timestamp = 1572879180
print(time.ctime(timestamp))

# A função strftime() no módulo time
import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))

# Exemplo pratico
from datetime import datetime

my_date = datetime(2020, 11, 4, 14, 53)

print(my_date.strftime("%Y/%m/%d %H:%M:%S"))
print(my_date.strftime("%y/%B/%d %H:%M:%S %p"))
print(my_date.strftime("%a, %Y %b %d"))
print(my_date.strftime("%A, %Y %B %d"))
print(my_date.strftime("Weekday: %w"))
print(my_date.strftime("Day of the year: %j"))
print(my_date.strftime("Week number of the year: %W"))


print("Calendario")


# Calendario
import calendar
print(calendar.calendar(2020)) # Ano especifico

import calendar
print(calendar.month(2020, 11)) # mes especifico
    