# QuickBB - a way to quickly upload images to ImgBB right from your desktop!

QuickBB uploads images directly to your ImgBB account and copies the direct image URL to your clipboard

![Demo1](https://i.ibb.co/Cb2Cy4t/436d8e08a797.gif)

There is also an option to include it in your "Send To" context menu in Windows! This makes it even more convenient to run, and you will not have to run the script, just simply right-click on the image, and "send to" ImgBB!

![Demo2](https://i.ibb.co/0Bhz2yk/4ef630bb1834.gif)

# Set Up
1. Run ```pip install -r /path/to/requirements.txt``` to install required packages
2. Create a FREE ImgBB account at https://imgbb.com/
3. Navigate to https://api.imgbb.com/
4. Click "Get API key", copy it
5. Run ```quickbb.py```
6. A new ```api_key.yaml``` file will be created and the script will end. Open it and add your API KEY after "key:" (ex. key: apikeyhere)
7. Save the .yaml file
8. Re-run ```quickbb.py``` again
9. The image you upload will both be uploaded to your account AND the direct link will be copied to your clipboard for easy sharing!

# "Send To" Menu Set Up
1. Open the tools folder and edit the ```imgbb.cmd``` file
2. Change the file path to the file path where the ```quickbb.py``` script is located
3. Open Windows File Explorer
4. In the Address Bar, type ```shell:sendto```
5. Copy the ```imgbb.cmd``` file to this folder
6. Right-click on your image, navigate to "Send To" and then click "imgbb.cmd"!
7. The image you upload will both be uploaded to your account AND the direct link will be copied to your clipboard for easy sharing!

# Tips
- This will **only** work with image files. If you attempt to upload anything other than an image, an error will be thrown and the script will exit
