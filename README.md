# Steganography

The purpose of this application is :

* From an image, write a text in this image by changing the lowest bits of each channel. -w switches to write mode. You can write the text directly into the command with -t, read from a file with -f, or leave nothing. You will be asked to enter a text later. You also must to specify the PNG file where you want to write
To run the build command use :
```python3 main.py [finalement] -w [-t "text" or -f filename  or nothing]```


* Read from an image the text contained in it. You must to specify the PNG file. The strings command using the subprocess module allow to delete special characters.

To run the build command use :
```python3 main.py [filename]```








