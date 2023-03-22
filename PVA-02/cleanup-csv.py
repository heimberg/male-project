import os
import csv

# Define a function to correct the name column
def correct_name(name):
    name = name.replace("minus", "-")
    name = name.replace("kreuz", "x")
    name = name.replace("plus", "+")
    name = name.replace("gartenhag", "#")
    name = name.replace("kreis", "o")
    return name

# Define a function to normalize the pixel values
def normalize_pixel(pixel, max_pixel):
    return float(pixel) / float(max_pixel)

# Define a function to flip the binary values
def flip_binary(pixel):
    if int(pixel) > (n / 2):
        return pixel
    else:
        return str(1 - int(pixel))

# Define the paths to the input and output directories
input_path = "./PVA-02/Datensatz/CSVs/"
output_path = "./PVA-02/Datensatz/CSVs/corrected/"

# Create the output directory if it does not exist
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Loop through each CSV file in the input directory
for filename in os.listdir(input_path):
    if filename.endswith(".csv"):
        # Open the input CSV file and create a new output file
        with open(input_path + filename, "r") as csv_file, open(output_path + filename, "w", newline="") as out_file:
            reader = csv.reader(csv_file)
            writer = csv.writer(out_file)

            # Loop through each row in the CSV file
            for row in reader:
                # Skip empty rows or rows with fewer than 2 elements
                if not row or len(row) < 2:
                    continue

                # Correct the name column
                row[0] = correct_name(row[0])

                # Normalize the pixel values and flip binary values
                pixels = [p for p in row[1:] if p.isdigit()]
                if not pixels:
                    max_pixel = 1
                else:
                    max_pixel = max([int(p) for p in pixels])
                n = len(row) - 1
                row[1:] = [normalize_pixel(p, max_pixel) if p.isdigit() else (0 if p == "False" else 1) for p in row[1:]]
                row[1:] = [flip_binary(p) for p in row[1:]]

                # Write the row to the output file
                writer.writerow(row)
