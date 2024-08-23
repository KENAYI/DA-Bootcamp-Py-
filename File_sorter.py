# Automated File sorter

import os, shutil

# Provide folder path
path = (r"C:/Users/chike/OneDrive - University of Birmingham/Pictures/Wallpapers/")

file_name = os.listdir(path)

# Create folders for each file type
# folder_names = ['csv files', 'img files', 'txt files']

# if not already  in path, create folder(s)
# for loop in range(len(folder_names)):
#    if not os.path.exists(path + folder_names[loop]):
#        print(path + folder_names[loop])
#        os.makedirs(path + folder_names[loop])

# Sort and move files into respective folders, if not already in designated folder
for file in file_name:
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".jpg" and  ".png" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "img files/" + file)
    elif ".txt" in file and not os.path.exists(path + "txt files/" + file):
        shutil.move(path + file, path +"txt files/" + file)