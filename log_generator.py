# encoding: utf-8
from random import randint
from datetime import datetime

for i in range(24):
    hum = randint(75, 80)
    temp = (randint(20, 30)) / 10
    date = datetime(2018, 1, 9, i, 0, 0)
    data = ('{} / T:{}C / H:{}% \n'.format(date, temp, hum))
    with open('temp_logfile.log', 'a') as f:
        f.write(data)
print('terminé')