
# Program: 			Image Obfuscator
# Description: 		Encrypts or decrypts image files using an XOR cipher with a randomly generated one time pad
# Author:			Connor Sullivan
# Date:				September 11 2017

from PIL import Image

import numpy as np

import random, sys

if len(sys.argv) == 1:
	print("""\nImage Obfuscator: by Connor Sullivan
	\nSyntax: [program] [mode] [source file] [key]""")
	sys.exit(0)

# The MODE can be any of the following: (e)ncrypt, (d)ecrypt
MODE = sys.argv[1].lower()

try:

	# read in the source image
	IMAGE_SOURCE = Image.open(sys.argv[2])
	
	# convert the image to a numpy array of pixel values
	img_arr = np.array(IMAGE_SOURCE)
	
	img_rows = img_arr.shape[0]
	img_cols = img_arr.shape[1]
	
except:

	# if there is a problem loading the source image
	print("\nError while loading source image! Did you specify a valid path?")
	sys.exit(1)

if MODE == "e" or MODE == "encrypt":
	
	# create a key to encrypt the image with
	IMAGE_KEY = Image.new("RGB", (img_cols, img_rows), "white")
	key_arr = np.array(IMAGE_KEY)
	
	# iterate through the arrays
	for i in range(img_rows):
		for j in range(img_cols):
			for k in range(3):
				
				# populate the key array with random numbers
				key_arr[i][j][k] = random.randint(0, 255)
				
				# XOR the image array with the key array
				img_arr[i][j][k] = int(img_arr[i][j][k]) ^ int(key_arr[i][j][k])
				
	# cast the image array back into an image object
	IMAGE_ENCRYPTED = Image.fromarray(img_arr)
			
	# cast the key array back into an image object
	IMAGE_KEY = Image.fromarray(key_arr)
	
	# write the encrypted image and key to the hard drive
	IMAGE_ENCRYPTED.save("encrypted.png")
	IMAGE_KEY.save("key.png")

if MODE == "d" or MODE == "decrypt":
	
	try:

		# read in the key
		IMAGE_KEY = Image.open(sys.argv[3])
		
		# convert the key to a numpy array of pixel values
		key_arr = np.array(IMAGE_KEY)
		
	except:

		# if there is a problem loading the key
		print("\nError while loading key! Did you specify a valid path?")
		sys.exit(1)
		
	# iterate through the arrays
	for i in range(img_rows):
		for j in range(img_cols):
			for k in range(3):
				
				# XOR the image array with the key array
				img_arr[i][j][k] = int(img_arr[i][j][k]) ^ int(key_arr[i][j][k])
				
	# cast the decrypted image data into an image object
	IMAGE_DECRYPTED = Image.fromarray(img_arr)
	
	# show the image to the user
	IMAGE_DECRYPTED.show()
	
	# save the image to the hard drive
	IMAGE_DECRYPTED.save("decrypted.png")
	