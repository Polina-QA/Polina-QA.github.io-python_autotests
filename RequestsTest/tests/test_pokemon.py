import pytest
import requests

URL="https://api.pokemonbattle.me:9104"

header={"Content-Type": 'application/json'}

def test_get_traners():
    """
    KTI-1. Get traners
    """

    response=requests.get(url=f"{URL}/trainers", params={"trainer_id": "3714"},headers=header, timeout=5)
    assert response.json()['trainer_name'] == "Богомол"
    assert response.status_code == 200, "Unexpected status code"