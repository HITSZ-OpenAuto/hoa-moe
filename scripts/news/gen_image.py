from openai import OpenAI
import requests
from PIL import Image


def generate_image(api_key):
    """Generate a random image of abstract art using DALL-E."""
    print("Generating an ai-generated image...")
    prompt = "a random image of abstract oil painting"
    client = OpenAI(
        # This is the default and can be omitted
        api_key=api_key,
        base_url="https://api.aihubmix.com/v1/",
    )

    response = client.images.generate(prompt=prompt)

    # Extract the URL of the generated image
    image_url = response.data[0].url
    image_response = requests.get(image_url)

    # Save the image to a file
    if image_response.status_code == 200:
        with open("generated_image.png", "wb") as f:
            f.write(image_response.content)
        print("Image downloaded and saved as 'generated_image.png'")
    else:
        print("Failed to download the image")

    img = Image.open("generated_image.png")
    img = img.crop((0, 0, img.width, img.height // 2))
    img.save("generated_image_cropped.png")
