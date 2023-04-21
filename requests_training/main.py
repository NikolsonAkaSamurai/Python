import requests

from My_gui import *

def get_request(text):
    response = requests.get(text)
    print(response.text)


# get_request("https://google.com")
window = my_gui(300, 400, "speed_test")
window.my_main_loop()
