import requests
import time
import random

SERVER_URL = "http://192.168.0.122:5000/update"

data = {
        "temperature": random.randint(20, 40),
        "object_count": random.randint(0, 10)
    }

r = requests.post(SERVER_URL, json=data)
print("Sent:", data)