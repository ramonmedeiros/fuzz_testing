import atheris
import sys
import requests


URL = "http://localhost:8000/api/v2/{}"

def reach_api(path, json):
    # add params
    param = URL.format(path)

    try:
        r = requests.get(url=param, json=json)
        r.raise_for_status()
    except requests.HTTPError as e:

        if e.response.status_code not in [404, 200, 301]:
            raise e


def get_pokemon_by_name(name):
    reach_api("pokemon", {"name": str(name)})

def test_pokemon_number():
    atheris.Setup(sys.argv, get_pokemon_by_name)
    atheris.Fuzz()
