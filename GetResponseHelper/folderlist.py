import requests
import os

GET_RESPONSE = os.environ["GET_RESPONSE"]

url = 'https://api.getresponse.com/v3/file-library/folders'
headers = {
    'X-Auth-Token': f'api-key {GET_RESPONSE}',
    'Content-Type': 'application/json'
}
params = {

}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    folders = response.json()
    print(f'Found {folders}')
    for folder in folders:
        folder_id = folder['folderId']
        folder_name = folder['name']
        print(f'{folder_id}: {folder_name} folder)')
else:
    print(f'Error getting folders. Status code: {response.status_code}')