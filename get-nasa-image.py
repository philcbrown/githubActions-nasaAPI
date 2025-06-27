image_base_url="https://api.nasa.gov/planetary/apod?api_key"

def get_image():
    try:
        response = requests.get(f"{image_base_url}={os.environ.NASA_SECRET}" )
        if response.status_code == 200:
            hdurl = response.json().get("hdurl")
            print(f"hdurl: {hdurl}")
        else:
            print("Failed to get json")
    except Exception as e:
        print(str(e))

get_image()
