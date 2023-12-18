###############################################################################
import subprocess

# List of required modules
required_modules = [
    'Pillow',
    # Add other modules as needed
]

def install_modules():
    for module in required_modules:
        try:
            subprocess.check_call(['pip', 'install', module])
            print(f'Successfully installed {module}')
        except subprocess.CalledProcessError:
            print(f'Error installing {module}')

# Install required modules
install_modules()

###############################################################################

print("""
IMAGE CONVERTER PROGRAM v1.0

License: Open license
Version 1.0
Email: jediros@gmail.com
https://www.researchgate.net/profile/Jedi-Rosero-Alvarado-2

IMPORTANT: This program was created to be run with specific .png or .jpg files.

For more information or program changes, please contact the author.
""")

## Libraries imported
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import os

## Create window
root = tk.Tk()
root.minsize(width=300, height=420)
root.maxsize(width=300, height=420)
root.title('Image extension converter')

canvas1 = tk.Canvas(root, width=300, height=420, bg='azure3',
                    relief='raised')
canvas1.pack()

## Create label
label1 = tk.Label(root, text="Image converter", bg='azure3')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 20, window=label1)

## Get folder and destination folder
# -----------------------------------
def getFolders():
    global source_folder, destination_folder
    source_folder = filedialog.askdirectory()
    destination_folder = filedialog.askdirectory()
    messagebox.showinfo("Information", "Source folder selected: {}\nDestination folder selected: {}".format(source_folder, destination_folder))

folder_button = tk.Button(text="Select Folders",
                          command=getFolders,
                          bg='royalblue',
                          fg='white',
                          font=('helvetica', 12, 'bold'),
                          border=0,
                          activebackground="green")
canvas1.create_window(150, 60, window=folder_button)
# -------------------------------------------------

## Convert all images in the folder to a specified format
# -------------------------------------------------------
def convertImages(image_format):
    global source_folder, destination_folder

    try:
        for filename in os.listdir(source_folder):
            if filename.endswith(('.jpg', '.jpeg', '.png', '.tif', '.tiff', '.gif', '.eps', '.bmp')):
                filepath = os.path.join(source_folder, filename)
                im = Image.open(filepath)
                export_file_path = os.path.join(destination_folder, os.path.splitext(filename)[0] + '.' + image_format)
                im.save(export_file_path)
        messagebox.showinfo("Information", "All images converted into {} format and saved to {}".format(image_format.upper(), destination_folder))
    except NameError:
        messagebox.showwarning("Warning", "Select source and destination folders first")

# Convert to jpg
jpg_button = tk.Button(text="Convert to JPG",
                       command=lambda: convertImages('jpg'),
                       bg='royalblue',
                       fg='white',
                       font=('helvetica', 12, 'bold'),
                       border=0)
canvas1.create_window(150, 100, window=jpg_button)

# Convert to jpeg
jpeg_button = tk.Button(text="Convert to JPEG",
                        command=lambda: convertImages('jpeg'),
                        bg='royalblue',
                        fg='white',
                        font=('helvetica', 12, 'bold'),
                        border=0)
canvas1.create_window(150, 140, window=jpeg_button)

# Convert to png
png_button = tk.Button(text="Convert to PNG",
                       command=lambda: convertImages('png'),
                       bg='royalblue',
                       fg='white',
                       font=('helvetica', 12, 'bold'),
                       border=0)
canvas1.create_window(150, 180, window=png_button)

# Convert to tif
tif_button = tk.Button(text="Convert to TIF",
                       command=lambda: convertImages('tif'),
                       bg='royalblue',
                       fg='white',
                       font=('helvetica', 12, 'bold'),
                       border=0)
canvas1.create_window(150, 220, window=tif_button)

# Convert to tiff
tiff_button = tk.Button(text="Convert to TIFF",
                        command=lambda: convertImages('tiff'),
                        bg='royalblue',
                        fg='white',
                        font=('helvetica', 12, 'bold'),
                        border=0)
canvas1.create_window(150, 260, window=tiff_button)

# Convert to gif
gif_button = tk.Button(text="Convert to GIF",
                       command=lambda: convertImages('gif'),
                       bg='royalblue',
                       fg='white',
                       font=('helvetica', 12, 'bold'),
                       border=0)
canvas1.create_window(150, 300, window=gif_button)

# Convert to eps
eps_button = tk.Button(text="Convert to EPS",
                       command=lambda: convertImages('eps'),
                       bg='royalblue',
                       fg='white',
                       font=('helvetica', 12, 'bold'),
                       border=0)
canvas1.create_window(150, 340, window=eps_button)

# Convert to bmp
bmp_button = tk.Button(text="Convert to BMP",
                       command=lambda: convertImages('bmp'),
                       bg='royalblue',
                       fg='white',
                       font=('helvetica', 12, 'bold'),
                       border=0)
canvas1.create_window(150, 380, window=bmp_button)
# --------------------------------------------------

root.mainloop()

