import os
import shutil

# create a new directory
# os.mkdir("new_directory")

# rename a directory
# raise FileExistsError if the directory not exists
# os.rename("new_directory", "renamed_directory")

# get current working directory
# print(os.getcwd())

# remove an empty directory
# os.rmdir("renamed_directory")

# list all files and directories in the current directory
# print(os.listdir())

# rename or move a file
# shutil.move("file2.txt", "renamed_file2.txt")
# not often used absolute path
# shutil.move(
#     "renamed_file2.txt",
#     "C:/Users/pryan/Desktop/python-jan/11_file_handling/new_dir/newname.txt",
# )

shutil.copy("file.txt", "file_copy.txt")
