import os
from PIL import Image

# clean up the pictures in the folder 'Bilder'

# Resize all pictures  to 10x10 pixels
# and save them in the folder 'resized'

input_dir = "./PVA-02/Datensatz/Bilder"
output_dir = "./PVA-02/Datensatz/Bilder/resized"

for file_name in os.listdir(input_dir):
    if file_name.endswith(".png"):
        img = Image.open(os.path.join(input_dir, file_name))
        if img.size != (10, 10):
            img = img.resize((10, 10))
        output_file_name = os.path.join(output_dir, file_name)
        img.save(output_file_name)
        
# rename pictures who do not have the right name
# the right name starts with [-,+,#,o]. Search and replace like:
# minus -> -
# kreuz -> +
# gartenhag -> #
# kreis -> o
# the rest of the name is the same
# save in the same folder

input_dir = "./PVA-02/Datensatz/Bilder/resized"
output_dir = "./PVA-02/Datensatz/Bilder/resized"

for file_name in os.listdir(input_dir):
    if file_name.endswith(".png"):
        output_file_name = file_name.replace("minus", "-")
        output_file_name = output_file_name.replace("kreuz", "x")
        output_file_name = output_file_name.replace("plus", "+")
        output_file_name = output_file_name.replace("gartenhag", "#")
        output_file_name = output_file_name.replace("kreis", "o")
        output_file_name = os.path.join(output_dir, output_file_name)
        os.rename(os.path.join(input_dir, file_name), output_file_name)
