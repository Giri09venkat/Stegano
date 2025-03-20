import cv2
import base64
from src.crypto_utils import decrypt_message

def extract_data(image_path, key):
    """Extracts and decrypts the hidden message from an image."""

    # ✅ Convert JPEG to PNG to ensure correct extraction
    if image_path.lower().endswith(('.jpg', '.jpeg')):
        print("🔄 Converting JPEG to PNG for better extraction...")
        temp_png_path = image_path.replace(".jpg", ".png").replace(".jpeg", ".png")
        img = cv2.imread(image_path)
        cv2.imwrite(temp_png_path, img)
        image_path = temp_png_path

    img = cv2.imread(image_path)
    if img is None:
        print("❌ Error: Could not open image.")
        return None

    binary_data = ""
    for row in img:
        for pixel in row:
            for channel in pixel:
                binary_data += str(channel & 1)

    # ✅ Ensure EOF marker is found
    if "00000000" in binary_data:
        binary_data = binary_data[:binary_data.index("00000000")]

    # ✅ Convert binary to text safely
    extracted_bytes = [binary_data[i: i + 8] for i in range(0, len(binary_data), 8)]
    extracted_text = "".join([chr(int(byte, 2)) for byte in extracted_bytes if len(byte) == 8])

    # Debugging print
    print("🔍 Debug: Extracted Base64 (before decoding):", extracted_text)

    try:
        extracted_text = base64.b64decode(extracted_text).decode()
    except Exception:
        print("❌ Error: Extracted text is not valid Base64. Extraction may have failed.")
        return None

    decrypted_message = decrypt_message(extracted_text, key)
    return decrypted_message
