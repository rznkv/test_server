import requests

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

client = APIClient()

print(client.get_root())
print(client.client_check())