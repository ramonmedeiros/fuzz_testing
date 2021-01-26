import atheris
import sys
import requests


URL = "http://localhost:8000/api/v2/{}"

def reach_api(params=[]):
    # add params
    param = URL.format("/".join(params))

    try:
        r = requests.get(url=param)
        r.raise_for_status()
    except requests.HTTPError as e:

        if e.response.status_code not in [404, 200, 301]:
            raise e


def get_pokemon_by_number(number):
    try:
        number = number.decode()
    except Exception:
        return

    reach_api(["pokemon", number])

def test_pokemon_number():
    atheris.Setup(sys.argv, get_pokemon_by_number)
    atheris.Fuzz()

test_pokemon_number()
