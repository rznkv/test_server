import requests
from shared.models import MathRequest

class APIClient:
    def __init__(self):
        self.base_url = 'http://127.0.0.1:8000'

    def get_root(self):
        response = requests.get(
            f"{self.base_url}/"
        )
        return response.json()

    def client_check(self):
        response = requests.get(
            f"{self.base_url}/client_check"
        )
        return response.json()

    def number_square(self, number: float):
        response = requests.get(
            f"{self.base_url}/square",
            params={"x": number}
        )
        return response.json()

    def calculate(self, data: MathRequest):
        response = requests.post(
            f"{self.base_url}/calculate",
            json=data.dict()
        )
        return response.json()

