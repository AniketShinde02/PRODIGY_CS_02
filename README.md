# PRODIGY_CS_02

# Image Encryption using Pixel Manipulation

This method involves encrypting images by performing a simple XOR operation on each pixel value. The encryption key is an integer that is used to XOR each pixel value, effectively scrambling the image.

# How it works:

Encryption: Each pixel value in the original image is XORed with the encryption key, resulting in a scrambled pixel value.
Decryption: The encrypted pixel values are XORed with the decryption key (same as the encryption key) to retrieve the original pixel values.
Advantages:

Simple to implement
Fast encryption and decryption
Disadvantages:

Not secure for sensitive images, as the encryption key can be easily guessed or brute-forced
Limited to simple XOR operation, making it vulnerable to attacks
Use cases:

Basic image protection for non-sensitive images
Educational purposes to demonstrate simple encryption techniques
Code snippet:

python

Verify

Open In Editor
Edit
Run
Copy code
def encrypt_image(image, key):
    encrypted_image = Image.new('RGB', image.size)
    for x in range(image.width):
        for y in range(image.height):
            pixel = image.getpixel((x, y))
            encrypted_pixel = tuple(val ^ key for val in pixel)
            encrypted_image.putpixel((x, y), encrypted_pixel)
    return encrypted_image
This method is a basic example of image encryption using pixel manipulation. While it's not suitable for secure encryption, it can be useful for educational purposes or basic image protection.
 
