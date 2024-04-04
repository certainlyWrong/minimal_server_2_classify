import json
import requests
from rich import print
from sys import argv


def run():
    # argv[1] is the image path
    # argv[2] is the server url

    print(f"Arguments: {argv}")

    if len(argv) < 3:
        print("Usage: poetry run client <image_path> <server_url>")
        return
    elif len(argv) > 3:
        print("Too many arguments")
        return

    image_path = argv[1]
    url = argv[2]

    # url = "http://localhost:8000/predict"

    # image_path = "/mnt/c/Users/adria/Downloads/images.jpeg"

    with open(image_path, "rb") as file:
        image_data = file.read()

    files = {"image": ("image.jpg", image_data, "image/jpeg")}
    response = requests.post(f"{url}/predict", files=files)

    if response.status_code == 200:
        response = json.loads(response.text)
        print(response)

    else:
        print(
            "Falha ao enviar a imagem. Código de status:",
            response.status_code
        )
