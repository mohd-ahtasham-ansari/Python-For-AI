import random

rndm_number = random.randint(1, 10)

choice = random.choice(["apple", "mango ", "banana"])

print(rndm_number, choice)

import datetime

today = datetime.date.today()
time = datetime.datetime.now()  
print(today, time)

import geocoder

location = geocoder.ip("me")
print(location.latlng)

import json

data = {"name": "dave", "age": "19"}
json_string = json.dumps(data)
print(json_string)

import os

current_dir = os.getcwd()
print(current_dir)
