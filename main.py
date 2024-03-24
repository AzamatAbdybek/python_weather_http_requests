import requests


url_london = "https://wttr.in/london?nTqumM&lang=ru"
url_sheremetevo = "https://wttr.in/%D1%88%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D1%82%D1%8C%D0%B5%D0%B2%D0%BE?nTqumM&lang=ru"
url_cherepovec = "https://wttr.in/%D1%87%D0%B5%D1%80%D0%B5%D0%BF%D0%BE%D0%B2%D0%B5%D1%86?nTqumM&lang=ru"



for url in [url_london, url_sheremetevo, url_cherepovec]:
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)
