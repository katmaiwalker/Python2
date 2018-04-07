from string import digits
import os
def rename_files():
    #(1) get file names from a folder
    # bellow "r" means (rawpack) take the string as it is and dont interpret
    # it in any other way.
    file_list = os.listdir(r"C:\Python27\MyProgramms\secret_message\prank")
    print(file_list)

    saved_path = os.getcwd()
    print("Current Working Directory is" + saved_path)

    #(2) For each file, rename filename
    for filename in file_list:
        os.rename("prank\\" + filename,"prank\\"+filename.translate(None, digits))
        #print(filename)

    #(3)Another solution with the directory issue, we can change the location
    # that our program is looking by using this: os.chdir(saved_path)
    # so the program will look inside the prank folder which contain the photos.
    # From my side i set prank file by hand in rename function.
rename_files()
