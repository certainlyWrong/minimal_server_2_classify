import json
import requests
from rich import print


def run():
    url = "http://localhost:8000/predict"

    image_path = "/mnt/c/Users/adria/Downloads/images.jpeg"

    with open(image_path, "rb") as file:
        image_data = file.read()

    files = {"image": ("image.jpg", image_data, "image/jpeg")}
    response = requests.post(url, files=files)

    if response.status_code == 200:
        response = json.loads(response.text)
        print(response)

    else:
        print(
            "Falha ao enviar a imagem. Código de status:",
            response.status_code
        )
