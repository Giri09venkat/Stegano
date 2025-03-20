import tkinter as tk
from tkinter import filedialog
from hide import hide_data
from extract import extract_data

def select_file(entry):
    filename = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, filename)

def hide_message():
    hide_data(image_entry.get(), message_entry.get(), output_entry.get())

def extract_message():
    message = extract_data(stego_entry.get())
    output_label.config(text="Extracted Message: " + message)

root = tk.Tk()
root.title("Image Steganography")

tk.Label(root, text="Original Image:").pack()
image_entry = tk.Entry(root)
image_entry.pack()
tk.Button(root, text="Browse", command=lambda: select_file(image_entry)).pack()

tk.Label(root, text="Secret Message:").pack()
message_entry = tk.Entry(root)
message_entry.pack()

tk.Label(root, text="Output Image Path:").pack()
output_entry = tk.Entry(root)
output_entry.pack()

tk.Button(root, text="Hide Message", command=hide_message).pack()

tk.Label(root, text="Stego Image:").pack()
stego_entry = tk.Entry(root)
stego_entry.pack()
tk.Button(root, text="Browse", command=lambda: select_file(stego_entry)).pack()

output_label = tk.Label(root, text="")
output_label.pack()

tk.Button(root, text="Extract Message", command=extract_message).pack()

root.mainloop()
