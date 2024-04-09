import json
from random import choice
import requests
from pixlr_private_api.main import PixlrApi

pixlr_client = None
total_image_generatoions_left = 0


def promptGenerator(theme: str):
    # Example Usage:
    # prompt = promptGenerator("supercars")
    # print(prompt) 'Lexus LFA, In a Garage, Purple, Hyper Realistic Theme, Back View, Afternoon, Happiness, City Scenery'
    with open("styles/" + theme + ".json", "r") as f:
        styles = json.load(f)

    output = ""
    for index in range(0, len(styles)):
        output += choice(styles[index]) + ", "

    return output[:-2]


def generateImage(prompt: str):
    # Example Usage:
    # generateImage("Lexus LFA, In a Garage, Purple, Hyper Realistic Theme, Back View, Afternoon, Happiness, City Scenery")
    # This will generate an image based on the prompt
    global pixlr_client, total_image_generatoions_left
    if not pixlr_client or total_image_generatoions_left == 0:
        pixlr_client = PixlrApi()
        pixlr_client.register()
        pixlr_client.verify_email()
        total_image_generatoions_left = 20

    images = pixlr_client.generate_image(768, 1344, 1, prompt)
    total_image_generatoions_left -= 1
    image = images[0]
    prompt = prompt

    return image, prompt


def png_to_jpeg(inputPath: str) -> str:
    # Example Usage:
    # png_to_jpeg("input.png")
    # This will convert the input.png to input.jpg
    from PIL import Image
    from uuid import uuid4

    image_path = f"/tmp/{uuid4()}.jpg"
    im = Image.open(inputPath)
    rgb_im = im.convert("RGB")
    # Image is 1024x1792 so we want to crop it to be 9:16
    # Meaning the new image will be: 1008x1792
    rgb_im = rgb_im.crop((8, 0, 1016, 1792))
    rgb_im.save(image_path)
    return image_path
