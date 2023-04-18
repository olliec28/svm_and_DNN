import os
import shutil

# Set the directories to search for CSV files
dirs_to_search = ["/Users/olivercustance/esp-csi/examples/get-started/tools/ewan"]

# Set the names of the new folders
new_folders = {
    "sitting_train": ["test1_", "test2", "test3", "test4"],
    "sitting_test": ["test5"],
    "standing_train": ["test6", "test7", "test8", "test9"],
    "standing_test": ["test10"]
}

# Iterate through each directory
for dir_path in dirs_to_search:
    # Create the new folders in the directory
    for folder_name in new_folders:
        folder_path = os.path.join(dir_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)
    # Move CSV files to the appropriate folders
    for file_name in os.listdir(dir_path):
        if file_name.endswith(".csv"):
            for folder_name, prefixes in new_folders.items():
                if file_name.startswith(tuple(prefixes)):
                    src_path = os.path.join(dir_path, file_name)
                    dst_path = os.path.join(dir_path, folder_name, file_name)
                    shutil.move(src_path, dst_path)
