from PIL import Image

def encrypt_image(image_path, key):
    """
    Encrypts an image by performing an XOR operation on each pixel value.

    :param image_path: Path to the image file
    :param key: Encryption key (an integer)
    :return: Encrypted image
    """
    image = Image.open(image_path)
    width, height = image.size
    encrypted_image = Image.new('RGB', (width, height))

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            encrypted_pixel = tuple(val ^ key for val in pixel)
            encrypted_image.putpixel((x, y), encrypted_pixel)

    return encrypted_image

def decrypt_image(encrypted_image, key):
    """
    Decrypts an encrypted image by performing an XOR operation on each pixel value.

    :param encrypted_image: Encrypted image
    :param key: Decryption key (an integer)
    :return: Decrypted image
    """
    width, height = encrypted_image.size
    decrypted_image = Image.new('RGB', (width, height))

    for x in range(width):
        for y in range(height):
            pixel = encrypted_image.getpixel((x, y))
            decrypted_pixel = tuple(val ^ key for val in pixel)
            decrypted_image.putpixel((x, y), decrypted_pixel)

    return decrypted_image

def main():
    while True:
        print("Image Encryption Tool")
        print("---------------------")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            image_path = input("Enter the path to the image file: ")
            key = int(input("Enter the encryption key: "))
            encrypted_image = encrypt_image(image_path, key)
            encrypted_image.save("encrypted_image.png")
            print("Encrypted image saved as encrypted_image.png")
        elif choice == "2":
            encrypted_image_path = input("Enter the path to the encrypted image file: ")
            key = int(input("Enter the decryption key: "))
            encrypted_image = Image.open(encrypted_image_path)
            decrypted_image = decrypt_image(encrypted_image, key)
            decrypted_image.save("decrypted_image.png")
            print("Decrypted image saved as decrypted_image.png")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()