import os
import csv

def add_activity_column(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith('.csv'):
            # get the activity name and header from the file name
            if filename.endswith('sitting.csv'):
                activity = 'ewan_sitting'
                header = 'activity'
            elif filename.endswith('standing.csv'):
                activity = 'ewan_standing'
                header = 'activity'
            else:
                continue # skip the file if it's not a sitting or standing file
            # open the file and append the activity column
            with open(os.path.join(directory_path, filename), 'r') as csvfile:
                reader = csv.reader(csvfile)
                rows = []
                for i, row in enumerate(reader):
                    if i == 0:
                        row.append(header)
                    else:
                        row.append(activity)
                    rows.append(row)
            # write the updated rows back to the file
            with open(os.path.join(directory_path, filename), 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for row in rows:
                    writer.writerow(row)

# example usage:
directory_path = '/Users/olivercustance/esp-csi/examples/get-started/tools/ewan'
add_activity_column(directory_path)
