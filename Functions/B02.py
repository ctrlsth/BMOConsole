# B02 - Magic Conch Shell
from rCSV import *; import time; import math
def kerangajaib():
    print("Apa pertanyaan mu?")
    question = input()

    gacha = [(0, 'Iya'), (1, 'Tidak'), (2, 'Bisa Jadi'), (3, 'Mungkin'),(4, 'Tidak Mungkin'),(5,'Pasti'),(6, 'Yo nda tau')]

    x = math.floor(time.time()) 
    a = 11
    c = 4
    m = 100

    x_n1 = ((a * x) + c) % m
    for (x, y) in gacha:
        if x_n1 % 7 == x:
            print(y)
kerangajaib()

