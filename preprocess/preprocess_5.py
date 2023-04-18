import os

import pandas as pd

# directories containing files to concatenate
dir1 = '/Users/olivercustance/esp-csi/examples/get-started/tools/jacob/standing_train/combined'
dir2 = '/Users/olivercustance/esp-csi/examples/get-started/tools/peter/standing_train/combined'
dir3 = '/Users/olivercustance/esp-csi/examples/get-started/tools/jenna/standing_train/combined'
dir4 = '/Users/olivercustance/esp-csi/examples/get-started/tools/minsi/standing_train/combined'
dir5 = '/Users/olivercustance/esp-csi/examples/get-started/tools/simon/standing_train/combined'
dir6 = '/Users/olivercustance/esp-csi/examples/get-started/tools/monica/standing_train/combined'
dir7 = '/Users/olivercustance/esp-csi/examples/get-started/tools/saad/standing_train/combined'
dir8 = '/Users/olivercustance/esp-csi/examples/get-started/tools/baba/standing_train/combined'
dir9 = '/Users/olivercustance/esp-csi/examples/get-started/tools/ollie/standing_train/standing_complete/standing_combined'
dir10 = '/Users/olivercustance/esp-csi/examples/get-started/tools/ler/ler_standing_training/combined'
dir11 = '/Users/olivercustance/esp-csi/examples/get-started/tools/maomao/standing_train/combined'
dir12 = '/Users/olivercustance/esp-csi/examples/get-started/tools/harry/ready for processing/standing_train/combined'
dir13 = '/Users/olivercustance/esp-csi/examples/get-started/tools/liam/ready for processing/standing_train/combined'
dir14 = '/Users/olivercustance/esp-csi/examples/get-started/tools/megan/ready for processing/standing_train/combined'
dir15 = '/Users/olivercustance/esp-csi/examples/get-started/tools/ewan/standing_train/combined'

# output directory and file name
output_dir = '/Users/olivercustance/esp-csi/examples/get-started/tools/standing_combined'
output_file = 'standing_combined.csv'

# get a list of CSV files with the same name from all directories
files_to_concatenate = []
for root, dirs, files in os.walk(dir1):
    for file in files:
        if file.endswith('.csv'):
            if os.path.isfile(os.path.join(dir2, file)) and os.path.isfile(os.path.join(dir3, file)) and \
               os.path.isfile(os.path.join(dir4, file)) and os.path.isfile(os.path.join(dir5, file)) and \
               os.path.isfile(os.path.join(dir6, file)) and os.path.isfile(os.path.join(dir7, file)) and \
               os.path.isfile(os.path.join(dir8, file)) and os.path.isfile(os.path.join(dir9, file)) and \
               os.path.isfile(os.path.join(dir10, file)) and os.path.isfile(os.path.join(dir11, file)) and \
               os.path.isfile(os.path.join(dir12, file)) and os.path.isfile(os.path.join(dir13, file)) and \
               os.path.isfile(os.path.join(dir14, file)) and os.path.isfile(os.path.join(dir15, file)):
                files_to_concatenate.append(file)

# sort the list of files by name
files_to_concatenate.sort()

# concatenate the contents of the CSV files into a single dataframe
dfs = []
for filename in files_to_concatenate:
    df1 = pd.read_csv(os.path.join(dir1, filename))
    df2 = pd.read_csv(os.path.join(dir2, filename))
    df3 = pd.read_csv(os.path.join(dir3, filename))
    df4 = pd.read_csv(os.path.join(dir4, filename))
    df5 = pd.read_csv(os.path.join(dir5, filename))
    df6 = pd.read_csv(os.path.join(dir6, filename))
    df7 = pd.read_csv(os.path.join(dir7, filename))
    df8 = pd.read_csv(os.path.join(dir8, filename))
    df9 = pd.read_csv(os.path.join(dir9, filename))
    df10 = pd.read_csv(os.path.join(dir10, filename))
    df11 = pd.read_csv(os.path.join(dir11, filename))
    df12 = pd.read_csv(os.path.join(dir12, filename))
    df13 = pd.read_csv(os.path.join(dir13, filename))
    df14 = pd.read_csv(os.path.join(dir14, filename))
    df15 = pd.read_csv(os.path.join(dir15, filename))
    df_concat = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15])
    dfs.append(df_concat)
final_df = pd.concat(dfs)

# write the final dataframe to a CSV file in the output directory
final_df.to_csv(os.path.join(output_dir, output_file), index=False)