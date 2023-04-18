import os
import pandas as pd

# Set the directories to search for CSV files
dirs_to_search = ["/Users/olivercustance/esp-csi/examples/get-started/tools/baba/sitting_train", "/Users/olivercustance/esp-csi/examples/get-started/tools/baba/standing_train"]
sitting = "/Users/olivercustance/esp-csi/examples/get-started/tools/baba/sitting_train"
standing = "/Users/olivercustance/esp-csi/examples/get-started/tools/baba/standing_train"

# Iterate through each directory
for dir_path in dirs_to_search:
    # Set the paths for the 'sitting_train' and 'standing_train' directories
    sitting_train_dir = os.path.join(dir_path, sitting)
    standing_train_dir = os.path.join(dir_path, standing)

    # Create a 'combined' directory in each directory if it doesn't exist
    combined_dir_sitting_train = os.path.join(sitting_train_dir, "combined")
    if not os.path.exists(combined_dir_sitting_train):
        os.makedirs(combined_dir_sitting_train)

    combined_dir_standing_train = os.path.join(standing_train_dir, "combined")
    if not os.path.exists(combined_dir_standing_train):
        os.makedirs(combined_dir_standing_train)

    # Concatenate CSV files in the 'sitting_train' directory
    dfs_sitting_train = []
    for file_name in os.listdir(sitting_train_dir):
        if file_name.endswith(".csv") and file_name.startswith("test"):
            test_num = file_name[4]  # Extract the test number from the file name
            if test_num in ["1", "2", "3", "4"]:
                csv_path = os.path.join(sitting_train_dir, file_name)
                df = pd.read_csv(csv_path)
                dfs_sitting_train.append(df)
    concatenated_df_sitting_train = pd.concat(dfs_sitting_train, ignore_index=True)
    output_path_sitting_train = os.path.join(combined_dir_sitting_train, "output.csv")
    concatenated_df_sitting_train.to_csv(output_path_sitting_train, index=False)

    # Concatenate CSV files in the 'standing_train' directory
    dfs_standing_train = []
    for file_name in os.listdir(standing_train_dir):
        if file_name.endswith(".csv") and file_name.startswith("test"):
            test_num = file_name[4]  # Extract the test number from the file name
            if test_num in ["6", "7", "8", "9"]:
                csv_path = os.path.join(standing_train_dir, file_name)
                df = pd.read_csv(csv_path)
                dfs_standing_train.append(df)
    concatenated_df_standing_train = pd.concat(dfs_standing_train, ignore_index=True)
    output_path_standing_train = os.path.join(combined_dir_standing_train, "output.csv")
    concatenated_df_standing_train.to_csv(output_path_standing_train, index=False)

