import random
import time
import requests

url = "https://api.thingspeak.com/update?api_key=M7GX038RSZSOIBQY&field1={}&field2={}"

for i in range(5):
    t = random.randint(20, 30)
    h = random.randint(60, 80)
    print(t, h)
    requests.get(url.format(t, h))
    time.sleep(20)