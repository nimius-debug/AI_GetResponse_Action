import requests
import os
def upload_image_to_getresponse(image_path, image_name):
    url = f'https://api.getresponse.com/v3/multimedia'
    headers = {
        'X-Auth-Token': f'api-key {os.environ["GET_RESPONSE"]}',    
    }
    params = {
        'file': image_name,
    }
    with open(image_path, "rb") as image_file:
        files = {'file': (image_name, image_file, 'image/png')}
        response = requests.post(url, headers=headers, params=params, files=files)
        print(response.json())
    if response.status_code != 200:
        print(f"Error uploading image to GetResponse: {response.status_code} {response.text}")
    else:
        print(f"Image uploaded successfully to GetResponse ")
    
    return response.json()['url']