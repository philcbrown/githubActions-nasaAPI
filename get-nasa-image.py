import requests
import os

image_base_url="https://api.nasa.gov/planetary/apod?api_key"

def get_image():
    print("getting image")
    try:
        
        url = f"{image_base_url}={os.environ['NASA_SECRET']}"
        print(url)
        response = requests.get(url)
        if response.status_code == 200:
            hdurl = response.json().get("hdurl")
            print(f"hdurl: {hdurl}")
            img = requests.get(hdurl)
            if img.status_code == 200:
                with open("out/nasa.jpg", "wb") as f:
                    f.write(img.content)
                print("Image saved as nasa.jpg")
            else:
                print("Failed to download image")
            
        else:
            print("Failed to get json")
    except Exception as e:
        print(str(e))

get_image()
