@echo off
rem **************************
rem List all the absolute path 
rem of all files in current dir 
rem **************************
dir *.bmp;*.png;*.jpg;*.gif /b /s /a:-D > img.txt
