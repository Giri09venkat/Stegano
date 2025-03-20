import cv2
import base64
import os
from src.crypto_utils import encrypt_message

def hide_data(image_path, message, key, output_path):
    """Hides an encrypted message inside an image (PNG recommended)."""

    # ✅ Convert JPEG to PNG to prevent compression loss
    if image_path.lower().endswith(('.jpg', '.jpeg')):
        print("🔄 Converting JPEG to PNG to avoid compression loss...")
        temp_png_path = os.path.splitext(image_path)[0] + ".png"
        img = cv2.imread(image_path)
        cv2.imwrite(temp_png_path, img)  # Save as PNG
        image_path = temp_png_path

    img = cv2.imread(image_path)
    if img is None:
        print("❌ Error: Could not open image.")
        return

    # ✅ Encrypt and encode message in Base64
    encrypted_message = encrypt_message(message, key)
    encrypted_message = base64.b64encode(encrypted_message.encode()).decode()

    # Convert text to binary with an EOF marker
    binary_message = ''.join(format(ord(char), '08b') for char in encrypted_message)
    binary_message += '00000000'  # EOF marker

    data_index = 0
    for row in img:
        for pixel in row:
            for channel in range(3):  # R, G, B channels
                if data_index < len(binary_message):
                    pixel[channel] = (pixel[channel] & 0xFE) | int(binary_message[data_index])
                    data_index += 1

    cv2.imwrite(output_path, img)
    print("✅ Data hidden successfully in", output_path)
