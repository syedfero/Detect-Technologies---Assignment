import os
import pytesseract
from tkinter import Tk, filedialog, Button, Label, Listbox, END, Scrollbar, RIGHT, Y
from PIL import Image, ImageTk

# Initialize the Tkinter window
root = Tk()
root.title("OCR Application")

# Function to select images
def select_images():
    filepaths = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=(("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff"), ("All files", "*.*"))
    )
    for filepath in filepaths:
        listbox.insert(END, filepath)

# Function to perform OCR on selected images
def perform_ocr():
    for filepath in listbox.get(0, END):
        image = Image.open(filepath)
        text = pytesseract.image_to_string(image)
        text_output.insert(END, f"Text from {os.path.basename(filepath)}:\n{text}\n{'-'*50}\n")

# GUI components
select_button = Button(root, text="Select Images", command=select_images)
select_button.pack(pady=10)

listbox = Listbox(root, selectmode='multiple', width=50)
listbox.pack(pady=10)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

text_output = Listbox(root, width=80, height=20, yscrollcommand=scrollbar.set)
text_output.pack(pady=10)
scrollbar.config(command=text_output.yview)

ocr_button = Button(root, text="Perform OCR", command=perform_ocr)
ocr_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
