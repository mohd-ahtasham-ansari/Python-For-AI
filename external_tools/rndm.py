import random

rndm_number = random.randint(1,10)

choice = random.choice(["apple", "mango ", "banana"])

print(rndm_number,choice)

import datetime

today = datetime.date.today()
time = datetime.datetime.now()
print(today ,time)

import geocoder

location = geocoder.ip("me")
print(location.latlng)
