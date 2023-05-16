import os
import requests

GET_RESPONSE_API_KEY = os.environ["GET_RESPONSE"]

IMAGE_PATH = "img/1683572271.png"
IMAGE_NAME = "testing.png"


def upload_image_to_getresponse(image_path, image_name, api_key):
    url = f'https://api.getresponse.com/v3/multimedia'
    headers = {
        'X-Auth-Token': f'api-key {api_key}',
        
    }
    params = {
        'file': image_name,
    }
    
    with open(image_path, "rb") as image_file:
        files = {'file': (image_name, image_file, 'image/png')}
        response = requests.post(url, headers=headers, params=params, files=files)
        print(response)
    if response.status_code != 200:
        print(f"Error uploading image to GetResponse: {response.status_code} {response.text}")
    else:
        print(response.json())
        print(f"Image uploaded successfully to GetResponse ")
    return response.json()['url']


img_link = upload_image_to_getresponse(IMAGE_PATH, IMAGE_NAME, GET_RESPONSE_API_KEY)
print(img_link)
