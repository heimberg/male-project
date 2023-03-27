import os
import csv

# Define the correction rules for symbols
def substitute(symbol):
    symbol = symbol.replace("minus", "-")
    symbol = symbol.replace("kreuz", "x")
    symbol = symbol.replace("plus", "+")
    symbol = symbol.replace("gartenhag", "#")
    symbol = symbol.replace("kreis", "o")
    return symbol

# "normalize" to 1
def substitute(number):
    if number == "255":
        return "1"
    elif number == "True":
        return "1"
    elif number == "False":
        return "0"
    else:
        return number
    
# Define the input and output directories
input_dir = "./PVA-02/Datensatz/CSVs/"
output_dir = "./PVA-02/Datensatz/CSVs/corrected/"

# Loop through the input files
for filename in os.listdir(input_dir):
    # remove empty lines in the csv files
    if filename.endswith(".csv"):
        print("Processing file " + filename)
        with open(input_dir + filename, "r") as input_file:
            lines = input_file.readlines()
        lines = [line for line in lines if line.strip()]
        with open(input_dir + filename, "w") as output_file:
            output_file.writelines(lines)
        # correct the symbols in the csv files
        for i in range(len(lines)):
                columns = lines[i].split(",")
                columns[0] = substitute(columns[0])
                lines[i] = ",".join(columns)
        with open(input_dir + filename, "w") as output_file:
            output_file.writelines(lines)
        # normalize 255 -> 1
        for i in range(len(lines)):
            columns = lines[i].split(",")
            for j in range(len(columns)):
                columns[j] = substitute(columns[j])
            lines[i] = ",".join(columns)
        with open(input_dir + filename, "w") as output_file:
            output_file.writelines(lines)
        # count the occurence of 0 and 1
        count_0 = 0
        count_1 = 0
        for line in lines:
            columns = line.split(",")
            for column in columns:
                if column == "0":
                    count_0 += 1
                elif column == "1":
                    count_1 += 1
        # modify files with count(0) < count(1)
        if count_0 < count_1:
            for i in range(len(lines)):
                columns = lines[i].split(",")
                for j in range(len(columns)):
                    if columns[j] == "0":
                        columns[j] = "1"
                    elif columns[j] == "1":
                        columns[j] = "0"
                lines[i] = ",".join(columns)
        # write modified files to output directory
        with open(output_dir + filename, "w") as output_file:
            output_file.writelines(lines)

                    
                    
