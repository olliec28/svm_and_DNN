import csv
import os

input_dir = "input_dir"
input_filename = "/Users/olivercustance/esp-csi/examples/get-started/tools/sitting_combined/amplitude/sitting_combined.csv"
input_path = os.path.join(input_dir, input_filename)

output_dir = "output_dir"
output_filename = "/Users/olivercustance/esp-csi/examples/get-started/tools/sitting_combined/amplitude/sitting_ready_for_amp.csv"
output_path = os.path.join(output_dir, output_filename)

# Open the input CSV file
with open(input_filename) as f:
    # Create a reader object
    reader = csv.reader(f)

    # Skip the first row
    next(reader, None)

    # Create a list to store the arrays
    array_list = []

    # Loop over each row in the CSV file
    for row in reader:

        # Remove the last column
        row = row[:-1]

        # Create an empty array to store the values
        arr = []

        # Convert each value in the row to an integer and append to the array
        for val in row:
            arr.append(int(float(val.replace(',', ''))))

        # Append the array to the list
        array_list.append(arr)

# Open the output CSV file and write the array list
with open(output_filename, "w", newline='') as outfile:
    # Create a writer object
    writer = csv.writer(outfile)

    # Loop over each array in the array list and write it to a separate row
    for arr in array_list:
        writer.writerow([str(arr).replace(',', '')])
