import requests

locations = [
             "london",
             "шереметьево",
             "череповец"
]

payload = {"nTqum": "", "lang": "ru"}
base_url = "https://wttr.in/"
for location in locations:
    url = base_url + location

    response = requests.get(url, params=payload)
    response.raise_for_status()
    print(response.text)
