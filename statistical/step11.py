import csv
import numpy as np
import scipy.stats as stats

# Load CSI data from CSV file
with open('sitting_combined.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader) # Skip first row
    csi_data = []
    for row in reader:
        csi_data.append([int(val) for val in row[:-1]]) # Skip last column

# Extract CSI amplitude and phase values
csi_amp = np.abs(csi_data)
csi_phase = np.angle(csi_data)

# Compute statistical features for each row
mean_amp = np.mean(csi_amp[:,1:], axis=1) # Exclude first column
std_amp = np.std(csi_amp[:,1:], axis=1)
skew_amp = stats.skew(csi_amp[:,1:], axis=1)
kurtosis_amp = stats.kurtosis(csi_amp[:,1:], axis=1)
mean_phase = np.mean(csi_phase[:,1:], axis=1)
std_phase = np.std(csi_phase[:,1:], axis=1)
skew_phase = stats.skew(csi_phase[:,1:], axis=1)
kurtosis_phase = stats.kurtosis(csi_phase[:,1:], axis=1)

# Combine features into a single array
features = np.column_stack((mean_amp, std_amp, skew_amp, kurtosis_amp, mean_phase, std_phase, skew_phase, kurtosis_phase))

# Write features to CSV file
with open('csi_features.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Mean Amplitude', 'Std Amplitude', 'Skew Amplitude', 'Kurtosis Amplitude', 'Mean Phase', 'Std Phase', 'Skew Phase', 'Kurtosis Phase'])
    writer.writerows(features)

# Print the results
print(features)
