# QuickBB - a way to quickly upload images to ImgBB right from your desktop!

QuickBB uploads images directly to your ImgBB account and copies the direct image URL to your clipboard

![Demo1](https://i.ibb.co/Cb2Cy4t/436d8e08a797.gif)

There is also an option to include it in your "Send To" context menu in Windows! This makes it even more convenient to run, and you will not have to run the script, just simply right-click on the image, and "send to" ImgBB!

![Demo2](https://i.ibb.co/0Bhz2yk/4ef630bb1834.gif)

# Requirements
- Python 3.10.x+ (likely will work on earlier versions of Python 3, but was written focusing on 3.10.x+)
- [Pillow](https://pypi.org/project/pillow/)
- [Requests](https://pypi.org/project/requests/)
- The rest of the packages used are built-in that come with Python

# Set Up
1. Download source code
2. Create a FREE ImgBB account at https://imgbb.com/
3. Navigate to https://api.imgbb.com/
4. Click "Get API key"
5. Edit ```quickbb.py```
6. Add your API key to the ```api_key``` variable between the quotes (ex. api_key = '123456789')
7. Save
8. Run ```quickbb.py```
9. The image you upload will both be uploaded to your account AND the direct link will be copied to your clipboard for easy sharing!

# "Send To" Menu Set Up
1. Edit the ```imgbb.cmd``` file
2. Change the file path to the file path where the ```quickbb.py``` script is located
3. Open Windows File Explorer
4. In the Address Bar, type ```shell:sendto```
5. Copy the ```imgbb.cmd``` file to this folder
6. Right-click on your image, navigate to "Send To" and then click "imgbb.cmd"!
7. The image you upload will both be uploaded to your account AND the direct link will be copied to your clipboard for easy sharing!

# Tips
- This will **only** work with image files. If you attempt to upload anything other than an image, an error will be thrown and the script will exit
