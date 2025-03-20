from Crypto.Cipher import AES
import base64

def encrypt_message(message, key):
    """Encrypts the message using AES (ECB Mode)."""
    if len(key) != 16:
        raise ValueError("❌ Error: The encryption key must be exactly 16 characters.")

    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    padding = 16 - (len(message) % 16)
    padded_message = message + (chr(padding) * padding)

    encrypted_bytes = cipher.encrypt(padded_message.encode('utf-8'))
    return base64.b64encode(encrypted_bytes).decode()

def decrypt_message(encrypted_text, key):
    """Decrypts the AES encrypted message."""
    if len(key) != 16:
        raise ValueError("❌ Error: The decryption key must be exactly 16 characters.")

    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    decrypted_bytes = cipher.decrypt(base64.b64decode(encrypted_text))
    decrypted_message = decrypted_bytes.decode('utf-8')

    padding = ord(decrypted_message[-1])
    return decrypted_message[:-padding]
