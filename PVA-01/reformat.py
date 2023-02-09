import os
from PIL import Image

# path to the directory with the images
img_path = "Bilder/squares/"

# path to the directory where the processed images will be stored
processed_path = "Bilder/processed/"

# path to the csv file where the pixel values will be stored
csv_path = "Datensatz-matthias.heimberg.csv"

# function to process the images
def process_image(img_path, processed_path, csv_path, filename):
    img = Image.open(img_path + filename)
    img = img.resize((10, 10))
    img = img.convert("1")
    img.save(processed_path + filename)
    pixels = list(img.getdata())

    with open(csv_path, "a") as f:
        f.write(filename + "," + ",".join([str(p/255) for p in pixels]) + "\n")

if not os.path.exists(csv_path):
    with open(csv_path, "w") as f:
        f.write("filename,pixel_values\n")

for filename in os.listdir(img_path):
    process_image(img_path, processed_path, csv_path, filename)
