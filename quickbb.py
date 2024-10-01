import base64
import json
import os
import subprocess
import sys
import time
import requests
import yaml
from PIL import Image

api_key_file = os.path.join(os.path.dirname(__file__), 'api_key.yaml')

try:
    with open(api_key_file, 'r') as api_key_load:
        api_key_var = yaml.safe_load(api_key_load)
except FileNotFoundError:
    with open(api_key_file, 'w+') as api_key_load:
        api_key_load.write(f'key: ')
    print(
        f'"api_key.yaml" does not exist and has been created. '
        'Please edit the newly created "api_key.yaml" file, add your ImgBB API key, and re-run quickbb.'
    )
    exit()

api_key = api_key_var['key']

# if context menu is used
try:
    image_file = sys.argv[1]
# drag and drop/manual input method if context menu isn't used
except IndexError:
    image_file = input("Enter image location: ")

# validate file is an image file
try:
    Image.open(image_file)
except OSError:
    print("This is not an image file, please close this window and try again.")
    time.sleep(7)
    sys.exit(1)

print('Uploading to ImgBB...')

with open(image_file, 'rb') as file:
    url = 'https://api.imgbb.com/1/upload'
    payload = {
        'key': api_key,
        'image': base64.b64encode(file.read()),
    }
    res = requests.post(url, payload)

if res.status_code == 400:
    print('Error communicating with ImgBB. Check your API key.')
    time.sleep(7)
    sys.exit(1)

bb_data = res.text
bb_parsed = json.loads(bb_data)

img_url = bb_parsed['data']['image']['url']

# copies to clipboard
cmd='echo '+img_url.strip()+'|clip'
subprocess.check_call(cmd, shell=True)

print('Done!')
