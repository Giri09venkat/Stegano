from Crypto.Cipher.AES import AES
import base64

def pad_message(message):
    """Pads message to be multiple of 16 bytes for AES encryption."""
    return message + (16 - len(message) % 16) * " "

def encrypt_message(secret_message, key):
    """Encrypts the message using AES."""
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    encrypted_bytes = cipher.encrypt(pad_message(secret_message).encode('utf-8'))
    return base64.b64encode(encrypted_bytes).decode('utf-8')

def decrypt_message(encrypted_message, key):
    """Decrypts the AES encrypted message."""
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    decrypted_bytes = cipher.decrypt(base64.b64decode(encrypted_message))
    return decrypted_bytes.decode('utf-8').strip()

def message_to_binary(message):
    """Converts a text message to binary."""
    return ''.join(format(ord(char), '08b') for char in message)

def binary_to_message(binary_data):
    """Converts binary data back to a text message."""
    binary_chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    return "".join([chr(int(b, 2)) for b in binary_chars])
