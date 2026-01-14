for i in range(1, 4):
    print(i)

print("----")


# ciklusváltozó = kezdőérték
# while feltétel:
#     # ciklusmag
#     ciklusváltozó = frissítés

i = 1
while i < 4:
    print(i)
    i += 1

print("----")

while True:
    grade = input("Adj meg egy érdemjegyet (1-5): ")
    if grade.isdigit() and 0 < int(grade) < 6:
        print("Ez egy érdemjegy!: ", grade)
        break
    print("Ez nem érvényes érdemjegy, próbáld újra!")
