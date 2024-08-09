import requests

base_url = "https://wttr.in/"
locations = [
             "london",
             "шереметьево",
             "череповец"
]
payload = {"nTqum": "", "lang": "ru"}

def main():
    for location in locations:
        url = f"{base_url}{location}"
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print(response.text)

if __name__ == "__main__":
    main()