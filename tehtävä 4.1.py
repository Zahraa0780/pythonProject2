import requests
def hae_chuck_norris_vitsi():
    try:
        pyynto = "https://api.chucknorris.io/jokes/random"
        vastaus = requests.get(pyynto)
        if vastaus.status_code == 200:
            data = vastaus.json()
            print(data['value'])
        else:
            print(f"Virhe: {vastaus.status_code}")
    except Exception as e:
        print(f"Virhe: {e}")

hae_chuck_norris_vitsi()
