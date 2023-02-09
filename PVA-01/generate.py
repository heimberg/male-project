import cv2
import numpy as np
import os

# -----------------------------------------------------------------
# PVA-01
# Script to extract symbols from a hand drawn raw image
# the script needs to be run in the same directory as the raw image
# Directory structure:
# PVA-01
#  - Bilder
#    - raw-symbols.png
#    - squares
#    - symbols
#  - generate.py
# -----------------------------------------------------------------

# Load the image
img = cv2.imread("Bilder/raw-symbols.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# set size of the square
size = 100

# set your name
name = "matthias.heimberg"

# path to store the extracted symbols
symbol_path = "Bilder/symbols/"
# path to store the resized symbols (squares)
square_path = "Bilder/squares/"

# Threshold the image to a binary image
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

# Find contours in the binary image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through each contour and draw the bounding rectangle
for i, contour in enumerate(contours):
    [x, y, w, h] = cv2.boundingRect(contour)
    symbol = img[y:y + h, x:x + w]
    cv2.imwrite(f"{symbol_path}{i:02d}.png", symbol)

# Load all symbols and put each in the middle of a square
for j, filename in enumerate(os.listdir(symbol_path)):
    prefix = '-' if j < 10 else 'x' if j < 20 else '+' if j < 30 else 'o' if j < 40 else '#'
    img = cv2.imread(f"{symbol_path}{filename}")
    h, w, _ = img.shape
    new_h, new_w = (size, int(w * (size / h))) if h > w else (int(h * (size / w)), size)
    symbol = cv2.resize(img, (new_w, new_h), cv2.INTER_AREA)
    h, w, _ = symbol.shape
    new_img = np.ones((size, size, 3), np.uint8) * 255
    start_x = int(size / 2 - w / 2)
    start_y = int(size / 2 - h / 2)
    name = filename[:-4]
    new_img[start_y:start_y + h, start_x:start_x + w] = symbol
    cv2.imwrite(f"{square_path}{prefix}-{name}-.png", new_img)
