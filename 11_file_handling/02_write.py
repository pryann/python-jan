# with open("file2.txt", "w") as file:
#     # overwrite the file if it exists or create a new one
#     file.write("Hello, World!\n")

lines = ["first line\n", "second line\n", "third line\n"]

with open("file2.txt", "w") as file:
    file.writelines(lines)
