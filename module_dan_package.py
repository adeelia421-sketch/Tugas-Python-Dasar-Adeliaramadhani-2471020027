#Menggunakan Module
import math
from random import randint
import datetime as dt

print(math.sqrt(16))
print(math.pi)
print(randint(1, 6))
print(dt.date.today().year)



#Membuat module & package sendiri
#utils/hitung
def rata_rata(data):
    return sum(data) / len(data)

nilai = [80, 90, 70]

print(rata_rata(nilai))