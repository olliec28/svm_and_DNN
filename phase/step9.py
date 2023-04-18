import csv
import os
import re
import matplotlib.pyplot as plt
from math import sqrt, atan2

if __name__ == "__main__":
    """
    This script file demonstrates how to transform raw CSI out from the ESP32 into CSI-amplitude and CSI-phase.
    """

    # Define the input and output filenames
    input_filename = "/Users/olivercustance/esp-csi/examples/get-started/tools/sitting_combined/phase/sitting_ready_for_phase.csv"
    output_filename = "/Users/olivercustance/esp-csi/examples/get-started/tools/sitting_combined/phase/sitting_phase.csv"

    # Get the directory of the input file
    input_dir = os.path.dirname(os.path.abspath(input_filename))

    with open(input_filename) as f:
        f = open(os.path.join(input_dir, input_filename))

        with open(os.path.join(input_dir, output_filename), 'w', newline='') as csvfile:
            fieldnames = ['CSI_PHASE{}'.format(i) for i in range(1, 193)]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for j, l in enumerate(f.readlines()):
                imaginary = []
                real = []
                amplitudes = []
                phases = []

                # Parse string to create integer list
                csi_string = re.findall(r"\[(.*)\]", l)[0]
                csi_raw = [float(x) for x in csi_string.split(" ") if x != '']

                # Create list of imaginary and real numbers from CSI
                for i in range(len(csi_raw)):
                    if i % 2 == 0:
                        imaginary.append(csi_raw[i])
                    else:
                        real.append(csi_raw[i])

                # Transform imaginary and real into amplitude and phase
                for i in range(int(len(csi_raw) / 2)):
                    phases.append(atan2(imaginary[i], real[i]))

                # Write amplitude list to csv
                row_dict = {}
                for i in range(len(phases)):
                    row_dict['CSI_PHASE{}'.format(i + 1)] = phases[i]

                writer.writerow(row_dict)