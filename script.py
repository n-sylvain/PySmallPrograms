# import math
import sys

# from os import rename

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get("https://www.google.com")
print(r.status_code)

# print(greet('World'))
# print(greet('Corey'))

# name = input("Your Name? ")
# print("Hello,", name)
