import requests

def api():
    response = requests.get("http://api.open-notify.org/astros.json")
    print(response.json())

api()