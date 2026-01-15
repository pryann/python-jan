# file = open("file.txt", "r")
# content = file.read()
# print(content)

# pythonic way
# with open("file.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("file.txt", "r") as file:
#     content = file.read(5)
#     print(content)

# with open("file.txt", "r") as file:
#     # python use a pointer to keep track of the current position in the file
#     print(file.readline())
#     print(file.readline())
#     print(file.readline())
#     print(file.readline())
#     print(file.readline())

with open("file.txt", "r") as file:
    print(file.readlines())  # returns a list of lines
