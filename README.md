
# Python-Image-Obfuscation

This is a command line program written with Python 3 that allows users to obfuscate images. It is intended for use as a proof of concept, and is therefore not optimized for speed. What is does promise, however, is a perfectly secure encryption scheme that cannot be reversed without the key.

In encryption mode, the program generates a one time pad (key) that is combined with the original image data using an XOR cipher. Both the encrypted image and the key are saved as PNG files in the program's directory.

In decryption mode, the program uses both the encrypted image and the key file to reverse the cipher and produce the original image.

Usage: python imgobf.py [e/d] [source_image] [key (if decrypting)]
