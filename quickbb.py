import base64
import requests
import sys
import json
import subprocess
from PIL import Image
import time

api_key = '' 

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