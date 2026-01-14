# 2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(matrix[0][0])
print(matrix[2][2])
print(matrix[1][1])

# matrix[0] = 0
# matrix[1][1] = "HELLOOOO"
# print(matrix)

# 1. iteration: row = [1, 2, 3],
# 2. iteration: row = [4, 5, 6],
# 3. iteration: row = [7, 8, 9],
for row in matrix:
    # 1. iteration: item = 1
    # 2. iteration: item = 2
    # 3. iteration: item = 3

    # 1. iteration: item = 4
    # 2. iteration: item = 5
    # 3. iteration: item = 6

    # 1. iteration: item = 7
    # 2. iteration: item = 8
    # 3. iteration: item = 9
    for item in row:
        print(item)


# list_3D = [
#     [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9],
#     ],
#     [
#         [10, 11, 12],
#         [13, 14, 15],
#         [16, 17, 18],
#     ],
#     [
#         [19, 20, 21],
#         [22, 23, 24],
#         [25, 26, 27],
#     ],
# ]
