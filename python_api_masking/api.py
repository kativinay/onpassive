import requests

def call_api():
    response = requests.get("http://api.open-notify.org/astros.json")
    response.json())

call_api()