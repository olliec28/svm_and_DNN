import csv
import os

directory = '/Users/olivercustance/esp-csi/examples/get-started/tools/ewan'

for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        with open(os.path.join(directory, filename), 'r') as csvfile:
            rows = list(csv.reader(csvfile))
        with open(os.path.join(directory, filename), 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            headers = ["CSI_DATA" + str(i) for i in range(1, 385)]  # add headers
            csvwriter.writerow(headers)
            for row in rows[1:]:
                new_row = []
                for cell in row[24:-1]:
                    if cell.startswith('[') and cell.endswith(']'):
                        new_row.extend(cell[1:-1].split(','))
                    else:
                        new_row.append(cell)
                csvwriter.writerow(new_row)




