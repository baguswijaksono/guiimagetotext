import tkinter as tk
from tkinter import filedialog
from PIL import Image
import pytesseract

# Path to Tesseract executable (update this if necessary)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def browse_image():
    # Open file dialog to select an image file
    file_path = filedialog.askopenfilename()
    if file_path:
        # Update the image path in the entry widget
        entry_image_path.delete(0, tk.END)
        entry_image_path.insert(tk.END, file_path)

def extract_text_from_image():
    # Get the image path from the entry widget
    image_path = entry_image_path.get()
    
    # Open the image file
    with Image.open(image_path) as image:
        # Perform OCR and extract text
        text = pytesseract.image_to_string(image)
        
        # Update the text in the text widget
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, text)

# Create the main window
window = tk.Tk()
window.title("Image Text Extractor")

# Create a label and entry widget for the image path
label_image_path = tk.Label(window, text="Image Path:")
label_image_path.pack()

entry_image_path = tk.Entry(window, width=50)
entry_image_path.pack()

# Create a browse button to select an image file
button_browse = tk.Button(window, text="Browse", command=browse_image)
button_browse.pack()

# Create a button to extract text from the image
button_extract = tk.Button(window, text="Extract Text", command=extract_text_from_image)
button_extract.pack()

# Create a text widget to display the extracted text
text_widget = tk.Text(window, height=10, width=50)
text_widget.pack()

# Start the GUI event loop
window.mainloop()
