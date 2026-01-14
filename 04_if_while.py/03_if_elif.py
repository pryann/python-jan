# in real life you would validate the input here
grade = int(input("Please enter your grade (1-5): "))

if grade == 1:
    print("Elégtelen")
elif grade == 2:
    print("Elégséges")
elif grade == 3:
    print("Közepes")
elif grade == 4:
    print("Jó")
elif grade == 5:
    print("Jeles")
else:
    print("Hibás érték!")

# do not need to convert to int, we are comparing strings
# grade = input("Please enter your grade (1-5): ")

# if grade == "1":
#     print("Elégtelen")
# elif grade == "2":
#     print("Elégséges")
# elif grade == "3":
#     print("Közepes")
# elif grade == "4":
#     print("Jó")
# elif grade == "5":
#     print("Jeles")
# else:
#     print("Hibás érték!")
