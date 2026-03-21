# QuickBB - A way to quickly upload images to ImgBB right from your computer!

**QuickBB** uploads images directly to your ImgBB account and copies the direct image URL to your clipboard

![Demo1](https://i.ibb.co/Cb2Cy4t/436d8e08a797.gif)

There is also an option to include it in your "Send To" context menu in Windows! This makes it even more convenient to run as you will not have to run the script. Just simply right-click on the image, and "send to" ImgBB!

![Demo2](https://i.ibb.co/0Bhz2yk/4ef630bb1834.gif)

## Requirements
- Windows 10+
- Python 3.6+
- Dependencies: ```pip install -r requirements.txt```

## Important Information
- This will **only** work with image files. If you attempt to upload anything other than an image, an error will be thrown and the script will exit

## Setup
### 1. **Run once to generate API file**

  ```python quickbb.py```

  This creates:

  ```api_key.yaml```

### 2. **Add your API key**
- Create a FREE ImgBB account at https://imgbb.com/
- Navigate to https://api.imgbb.com/
- Click "Get API key", copy it
- Open ```api_key.yaml``` and add your API key after "key:" (ex. ```key: apikeyhere```)
- Save the .yaml file

## Usage
Run the script:

```python quickbb.py```

## "Send To" Context Menu Set Up
1. Open the tools folder and edit the ```imgbb.cmd``` file
2. Change the file path to the file path where the ```quickbb.py``` script is located
3. Open Windows File Explorer
4. In the Address Bar, type ```shell:sendto```
5. Copy the ```imgbb.cmd``` file to this folder

Now, when you right-click on an image image, just navigate to "Send To" and then click "imgbb.cmd". The image you upload will both be uploaded to your account AND the direct link will be copied to your clipboard for easy sharing!

## Using as a Module
You can also import and reuse this function in your own project:

```
from quickbb.quickbb import bb_upload

api_key = 'yourapikey'
image_file = 'C:\Path\to\image\file.jpg'

bb_upload(
    api_key=api_key,
    image_file=image_file
    copy_to_clipboard=True
)
```
