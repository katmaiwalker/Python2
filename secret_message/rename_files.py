from string import digits
import os
def rename_files():
    #(1) get file names from a folder
    # bellow "r" means (rawpack) take the string as it is and dont interpret
    # it in any other way.
    file_list = os.listdir(r"C:\Python27\MyProgramms\secret_message\prank")
    print(file_list)

    #(2) For each file, rename filename
    for filename in file_list:
        os.rename("prank\\" + filename,"prank\\"+filename.translate(None, digits))
        #print(filename)
rename_files()
