import requests
import json
# API_KEY=""


json_url = "https://api.thecatapi.com/v1/images/search?limit=10"
url = "https://cdn2.thecatapi.com/images/"


def get_cats_json():
    response = requests.get(json_url)
    response.raise_for_status()
    with open("response.json", mode="w") as f:
        json.dump(response.json(), f)


def get_picture(url: str):
    response = requests.get(url)
    response.raise_for_status()
    with open("MTc5NDIyMQ.jpg", 'wb') as file:
        file.write(response.content)



# eval('''exec("""import os;print(os.getenv("HELLO", "gs"))""")''')
