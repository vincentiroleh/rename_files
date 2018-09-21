import os

def rename_files():
    #Get files name from a folder where the files to be renamed are stored
    files_list = os.listdir(r"/home/iroleh/Desktop/prank")
    # print(files_list)
    os.chdir(r"/home/iroleh/Desktop/prank")

    #For each file, lets rename the filename
    for file_name in files_list:
        print("Old Name - " + file_name)
        print("New Name - " + file_name.translate(str.maketrans('','','0123456789')))
        os.rename(file_name,file_name.translate(str.maketrans('','','0123456789')))

rename_files()