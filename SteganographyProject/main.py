from src.hide import hide_data
import src.extract

if __name__ == "__main__":
    choice = input("Choose:\n1. Hide data\n2. Extract data\n> ")

    if choice == "1":
        image = input("Enter path of the image: ")
        message = input("Enter the secret message: ")
        key = input("Enter a 16-character encryption key: ")
        if len(key) != 16:
            print("❌ Key must be exactly 16 characters long!")
        else:
            output = input("Enter output image path: ")
            hide_data(image, message, key, output)

    elif choice == "2":
        image = input("Enter the stego image path: ")
        key = input("Enter the 16-character decryption key: ")
        extracted_message = src.extract.extract_data(image, key)
        if extracted_message:
            print(f"🔓 Extracted & Decrypted Message: {extracted_message}")

    else:
        print("❌ Invalid choice!")
