
import keras
import uvicorn
import numpy as np
from fastapi import FastAPI, UploadFile, File
from rich import print


app = FastAPI()

model = keras.applications.MobileNetV2(weights='imagenet', include_top=True)


def preprocess_image(image_path):
    img = keras.preprocessing.image.load_img(
        image_path, target_size=(224, 224))
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = keras.applications.mobilenet_v2.preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array


def classify_image(image_path):
    preprocessed_image = preprocess_image(image_path)
    predictions = model.predict(preprocessed_image)
    decoded_predictions = keras.applications.mobilenet_v2.decode_predictions(
        predictions, top=3)[0]
    return decoded_predictions


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post(
    "/predict",
)
async def predict(image: UploadFile = File(...)):
    print(image)
    try:
        with open("image.jpg", "wb") as buffer:
            buffer.write(await image.read())

        prediction = classify_image("image.jpg")

        labels = {
            label: score for (imagenet_id, label, score) in prediction
        }

        print(f"Prediction: {labels}")

        return str({"prediction": labels})

    except Exception as e:
        return "error" + str(e)


def run():
    try:
        uvicorn.run(app, host="0.0.0.0", port=8000)
    except KeyboardInterrupt:
        print("Finalizado!")
