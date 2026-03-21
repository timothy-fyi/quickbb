@echo off
cls
echo Uploading image to ImgBB...
:: update path to script after 'python' and before '%1'
python C:\path\to\quickbb\quickbb.py %1
echo Complete!