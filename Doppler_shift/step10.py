import csv
import numpy as np
import scipy.signal as signal

# Load CSI data from CSV file
with open('standing_combined.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader) # Skip first row
    csi_data = []
    for row in reader:
        csi_data.append([int(val) for val in row[:-1]]) # Skip last column

# Extract CSI amplitude and phase values
csi_amp = np.abs(csi_data)
csi_phase = np.angle(csi_data)

# Apply a high-pass filter to remove static phase offset
b, a = signal.butter(1, 0.1, 'highpass', fs=1000)
filtered_phase = signal.filtfilt(b, a, csi_phase)

# Compute the Doppler shift from phase change over time
doppler_shift = np.diff(filtered_phase, axis=0)

# Write Doppler shift values to CSV file
with open('doppler_shift.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(doppler_shift)

# Print the results
print(doppler_shift)
